#Q9- To plot convolution of box function
import numpy as np
import matplotlib.pyplot as plt
def f(x):
	if x < 1 and x > -1:
		return 1
	else:
		return 0
x = np.linspace(-5,5,512) 
fbox = np.zeros(512)
for i in range(len(x)):
	fbox[i]=f(x[i])
print(fbox)
ft = np.fft.fft(fbox,norm="ortho")**2
d=10/512
con = np.sqrt(512)*d*np.fft.fftshift(np.fft.ifft(ft,norm="ortho"))

plt.plot(x,fbox,'r',label="Box Function")
plt.plot(x, np.real(con), label="Convolution with itself")
plt.xlabel("x")
plt.ylabel("Fourier transform")
plt.legend()
plt.show()
