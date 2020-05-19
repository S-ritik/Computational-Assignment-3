import time as tt
import numpy as np
import matplotlib.pyplot as plt
timedc=np.empty(97)
timenp=np.empty(97)
t=np.arange(97)
for n in range(4,100):
	f=np.arange(n)
	fdc=np.zeros(n,dtype=complex)  # For FT calculated using direct computation
	x=np.arange(n)
	z=1j
	start=tt.time()
	fnp=np.fft.fft(f,norm="ortho")
	end=tt.time()
	timenp[n-4]=end-start
	start=tt.time()
	for k in range(len(x)):
		for i in range(0,n-1):
			fdc[k]=fdc[k]+f[i]*np.exp(-z*x[i]*2*np.pi*k/n)
	end=tt.time()
	timedc[n-4]=end-start
plt.plot(t,timenp,'r',label="Time taken by nump.fft.fft")
plt.plot(t,timedc,label="Time taken by direct computation")
plt.legend()
plt.xlabel("Nth step")
plt.ylabel("Time taken(in sec)")
plt.show()
