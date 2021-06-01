import numpy as np

from utils import conversion_db_veces

def probabilidad_error(hA, n, sigma):
  M=int(1e6)
  y_es_a = M

  for i in range(n):
    y = np.append( 
        np.random.normal(loc=hA, scale=sigma, size = y_es_a), 
        np.random.normal(loc=-hA, scale=sigma, size = M - y_es_a)
        )
    y_es_a = np.count_nonzero( y > 0 )


  return 1-y_es_a/int(1e6)

def simulacion_digital():
  '''
  Devuelve un arreglo con la salida Yn digital
  '''
  snr_veces = conversion_db_veces(np.arange(5,25))
  sigma = 1.0
  n=9
  
  hA = sigma * np.sqrt(snr_veces)

  y = np.array([])

  for hA_i, snr in zip(hA, snr_veces):
    probabilidad_error_ = probabilidad_error(hA=hA_i, n=9, sigma=sigma)
    y = np.append(y, probabilidad_error_)

  return y
