#for plot of Q4
import numpy as np
import matplotlib.pyplot as plt
def f(x):
	return 1/((2*np.pi)**0.5)*np.exp((-1*x*x)/4)
x=np.arange(512)
freq = np.fft.fftfreq(x.shape[-1])
ft=np.empty(len(freq))
for i in range(len(freq)):
	ft[i]=f(freq[i])
fn=np.genfromtxt("Q4data.csv")
fn=1*(512/2*np.pi)**0.5*fn

freq = np.fft.fftshift(freq)                  
ft = np.fft.fftshift(ft)                  
fn = np.fft.fftshift(fn)                  

plt.plot(freq,ft,'r',label="Analytical solution")
plt.plot(freq,fn,label="Using fftw")
plt.legend()
plt.xlabel("x")
plt.ylabel("Fourier transform")
plt.show()
