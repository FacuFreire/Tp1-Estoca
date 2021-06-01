import numpy as np

from scipy import stats as st

from utils import conversion_db_veces, _sum

def digital_error_avg(snr, n):
  '''
  Recibe una lista de snr y el valor de n (cant de antenas)
  Devuelve resultado del error promedio digital
  '''
  return 0.5 * (1-((1-2* st.norm.sf(np.sqrt(snr)))**n))

def analogic_error_avg(snr, n):
  '''
  Recibe una lista de snr y el valor de n (cant de antenas)
  Devuelve resultado del error promedio analogico
  '''

  numerador = snr

  input_sum = [(x+1)/x for x in snr]

  divisor = _sum(input_sum, n)

  cociente=[]

  for num, div in zip(numerador,divisor):
    cociente.append(num/div)

  return st.norm.sf(np.sqrt(cociente)) 

def setup_error_avgs():
  '''
  Devuelve una tupla con los arreglos pertenecientes al promedio de error analogico y al digital
  '''
  result_digital = []
  result_analogic = []

  snr_db = np.arange(-5,31)
  n_min = 1
  n_max = 25+1
  n_paso = 4

  snr_hz = conversion_db_veces(snr_db)

  for i in range(n_min, n_max, n_paso):
    result_digital.append(np.array(digital_error_avg(snr_hz, i)))
    result_analogic.append(np.array(analogic_error_avg(snr_hz, i)))

  result_digital = np.asarray(result_digital)
  result_analogic = np.asarray(result_analogic)

  return result_analogic, result_digital