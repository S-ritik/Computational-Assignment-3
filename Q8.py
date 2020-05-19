#Q8-To compute 3D FT using numpy


#      THE PLOT OVERLAP EACH OTHER

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def f(x,y):
	return np.exp(0-x*x-y*y)
def ft(x,y):
	return 1/(2*np.pi)*np.exp((0-x*x-y*y)/4)
data=np.empty((256,256))
ftas=np.empty((256,256))
x=np.arange(256)
y=np.arange(256)
for i in range(len(x)):
	for j in range(len(y)):
		data[i][j]=f(x[i],y[j])
print(data)
#d=20/256
#z=-1j
xfreq = np.fft.fftfreq(x.shape[-1])
yfreq = np.fft.fftfreq(y.shape[-1])
ft2=1/(2*np.pi)*np.fft.fft2(data)
print(ft2)
for i in range(len(xfreq)):
	for j in range(len(yfreq)):
		ftas[i][j]=ft(xfreq[i],yfreq[j])
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot_surface(xfreq,yfreq,ft2.real,color='y',label="Numerical solution")
ax.plot_surface(xfreq,yfreq,ftas,color='b',label="Analytical solution")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("Fourier transform")
plt.show()
