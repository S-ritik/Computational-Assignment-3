#Q6- To calculate the FT of a constant function (f=2 in this code)

import numpy as np
x=np.arange(512)
fconst=f=np.full(512,2)   # Let the value of constant function be 2
fnp=1*(512/2*np.pi)**0.5*np.fft.fft(fconst,norm="ortho") #xmin=0
print(fnp)