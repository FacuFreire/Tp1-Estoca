import numpy as np
from scipy import stats
import matplotlib.pyplot as plt



def plot_error_probability(result_analogic, result_digital):
  '''
  Grafica los errores analogico y digital
  '''
  
  # result_analogic = result
  snr_db = np.arange(-5,31)
  
  plt.figure(figsize=(6,3))
  for i in range(len(result_digital)):
   plt.semilogy(snr_db,result_digital[i],'-', label='n={}'.format(i*4+1))


  for i in range(len(result_analogic)):
    plt.semilogy(snr_db,result_analogic[i],'--', label='n={}'.format(i*4+1))

  plt.ylabel('$P_e(SNR)$')
  plt.xlabel('SNR [dB]')
  plt.legend()
  plt.ylim(top=1, bottom=10**(-6)) 
  plt.grid(True)
  plt.show()

def plot_monte_carlo(simulacion_digital, simulacion_analogica, teo_digital, teo_analogica):

  snr_db = np.arange(5,25)

  plt.figure(figsize=(6,3))
  plt.semilogy(snr_db,simulacion_analogica,'-',label='$P_{e,sim}^a$')
  plt.semilogy(snr_db,simulacion_digital,'-',label='$P_{e,sim}^d$')
  plt.semilogy(snr_db,teo_analogica,'*',label='$P_{e,teo}^a$')
  plt.semilogy(snr_db,teo_digital,'*',label='$P_{e,teo}^d$')
  plt.ylabel('$P_e(SNR)$')
  plt.xlabel('SNR [dB]')

  # for i in range(len(result_analogic)):
    # plt.semilogy(snr_db,result_analogic[i],'--', label='n={}'.format(i*4+1))

  # plt.ylabel('Probabilidad de error sistema digital')
  # plt.xlabel('SNR')
  plt.legend()
  plt.ylim(top=1, bottom=10**(-5)) 
  plt.xlim(left=5, right=25) 
  plt.grid(True)
  plt.show()



def plot_histograma(realiz, snr, mu, arr_cociente_snr):
  i= 19
  realiz_positivo = realiz + mu[i]
  realiz_negativo = realiz - mu[i]

  sigma = 1
  n=9

  A = arr_cociente_snr(snr[i], n, sigma)
  A = np.square(A) * sigma
  scale = A.sum()

  plt.figure(figsize=(6,3))

  _, bins, _ = plt.hist(x=realiz_positivo,density=True, bins=70, color='#0504aa', rwidth=0.7)
  plt.plot(bins, stats.norm.pdf(bins, loc = mu[i], scale=np.sqrt(scale)), color='g')

  _, bins, _ = plt.hist(x=realiz_negativo,density=True, bins=70, color='#0504aa', rwidth=0.7)
  plt.plot(bins, stats.norm.pdf(bins, loc = -mu[i], scale=np.sqrt(scale)), color='r')


  plt.grid(True)
  plt.xlabel('$Y_n$')
  plt.ylabel('$f_Y$')
  plt.title('Histogramas')


