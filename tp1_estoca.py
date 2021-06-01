import numpy as np

from scipy import special as sp
from scipy import stats as st
import time

from my_plots import plot_error_probability, plot_monte_carlo
from errores_promedio import setup_error_avgs
from simulacion_analogica import simulacion_analogica
from simulacion_digital import simulacion_digital


if __name__ == "__main__":
  result_analogic, result_digital = setup_error_avgs()

  
  simulacion_analogica = simulacion_analogica()

  start_time = time.time()
  simulacion_digital = simulacion_digital()
  print("--- %s seconds ---" % (time.time() - start_time))

  plot_error_probability(result_analogic, result_digital)
  plot_monte_carlo(simulacion_digital, simulacion_analogica,
                   result_digital[2, 10:30], result_analogic[2, 10:30] )
