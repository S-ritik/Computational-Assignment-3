# Q1- Calculating FT using np.fft.fft. Also definition of FT and DFT is same as that of sir. Also later part of this code contain code to plot Q2 and Q3 also.                   

import numpy as np
import matplotlib.pyplot as plt

#Analytical solution of function
def f(x):
	if(x>2*np.pi and x<2*np.pi):
		return (2*np.pi)**0.5
	else:
		return 0

x=np.arange(512)
d=1  # for defining del
func=np.empty(512)  #for defining values of given function sinc
ft=np.empty(512)	#array for plotting values of analytical solution of FT
for i in range(len(x)):
	if(x[i]==0):
		func[i]=1
	else:
		func[i]=np.sin(x[i])/x[i]
freq = np.fft.fftfreq(x.shape[-1])
for i in range(len(freq)):
	ft[i]=f(freq[i])
fnp=d*(512/2*np.pi)**0.5*np.fft.fft(func,norm="ortho") #xmin=0
freq = np.fft.fftshift(freq)        
ft = np.fft.fftshift(ft)
fnp = np.fft.fftshift(fnp)                
plt.plot(freq,ft,'r',label="Analytical solution")
plt.plot(freq,fnp,label="Using np.fft.fft")

#Now to plot Q2
ftfftw=np.generatefromtxt("Q4data.csv")
ftfftw=d*(512/2*np.pi)**0.5*ftfftw
ftfftw = np.fft.fftshift(ftfftw)        
plt.plot(freq,ftfftw,'o',label="Using fftw library")

#Now to plot Q3
ftgsl=np.generatefromtxt("Q4data.csv")
ftgsl = np.fft.fftshift(ftgsl)        
ftgsl=d*(1/2*np.pi)**0.5*ftgslplt.plot(freq,ftgsl,'g',label="Using gsl library")

plt.legend()
plt.xlabel("x")
plt.ylabel("Fourier transform")
plt.show()
