#Q10- To plot power spectrum

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

data= np.loadtxt('noise.txt')

x=np.arange(len(data))
plt.plot(x,data,label="Noise")
plt.legend()
plt.xlabel("x")
plt.ylabel("Noise")
plt.show()


ft=np.fft.fft(data)
freq=2*np.pi*np.fft.fftshift(np.fft.fftfreq(len(data),1))
pdg=(np.abs(ft)**2)/(len(ft)*2*np.pi)


plt.plot(freq,np.real(ft),label="Real part of DFT of data")
plt.plot(freq,np.imag((ft)),label="Imaginary part of DFT of data")
plt.legend()
plt.xlabel("x")
plt.ylabel(" Discrete Fourier Transform")
plt.show()

plt.plot(freq,pdg)
plt.xlabel("x")
plt.ylabel("Power Spectrum")
plt.show()    

k_bin, pdg_bin, binnumber= stats.binned_statistic(freq, pdg, bins=10)
final_pdg_bin=(pdg_bin[0:len(pdg_bin)-1]+pdg_bin[1:len(pdg_bin)])/2
plt.bar(final_pdg_bin, k_bin, width=pdg_bin[1]-pdg_bin[0])
plt.xlabel("x")
plt.ylabel("Histrogram of Power Spectrum")
plt.show()