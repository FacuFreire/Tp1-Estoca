import numpy as np
import matplotlib.pyplot as plt

from utils import conversion_db_veces
from my_plots import plot_histograma

def mu_y(snr, n, sigma):
  '''
  Devuelve un arreglo numpy del primer sumando de la salida analogica.
  '''
  exponente = (n-1)/2
  cociente_snr = np.asarray([(x/(x+1))**exponente for x in snr])
  hA = sigma*np.sqrt(snr)
  return  hA * cociente_snr


def arr_cociente_snr(snr_hz, n, sigma):
  '''
  Devuelve un arreglo con el cociente (SNR/SNR+1)^n-i. Es parte del segundo sumando de la salida analogica.
  '''
  snr = snr_hz/(snr_hz+1)

  arr_snr = []

  for i in range(1,n+1):
    arr_snr.append ( snr**(n-i) )

  return arr_snr



def simulacion_analogica ():
  '''
  Devuelve un arreglo con la salida Yn analogica
  '''
  snr_veces = conversion_db_veces(np.arange(5,25))
  sigma = 1.0
  M = int(1e6)
  n=9
  y = np.array([])

  mu = mu_y(snr_veces, n=9, sigma=sigma)
  
  w = np.random.normal(size = M, scale= sigma)
  w.resize( (1, M) )
  for _ in range(1, n):  #arma array random de n x M
    w_i = np.random.normal(size = M, scale= sigma)
    w_i.resize( (1,M) )
    w = np.append( w, w_i, axis = 0)
  

  for mu_i, snr in zip(mu, snr_veces):
    arr_snr = arr_cociente_snr(snr, n, sigma) #devuelve vector de 9
    realiz = np.dot(arr_snr, w)
    probabilidad_error = np.count_nonzero( realiz > mu_i )/M #cuenta los verdaderos, entonces doy vuelta la condicion
    y = np.append(y, probabilidad_error)

  plot_histograma(realiz, snr_veces, mu, arr_cociente_snr)
  return y