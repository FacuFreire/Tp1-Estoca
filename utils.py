import numpy as np

def conversion_db_veces(snr):
  '''
  Recibe arreglo de SNR en db.
  Devuelve arreglo de SNR en veces
  '''
  db_to_hz_converter = lambda x: 10**(0.1*x) 
  snr_hz = [db_to_hz_converter(x) for x in snr] #armo una lista con los steps de niveles
  return np.asarray(snr_hz)

def _sum(input_sum, n):
  '''
  Recibe un arreglo de elementos a ser sumados y devuelve un arreglo con la sumatoria de valores^n
  '''
  out_sum = []

  for val in input_sum:
    aux=0
    for i in range(n-1):
      aux += val**i
    out_sum.append(aux)
    
  return out_sum
