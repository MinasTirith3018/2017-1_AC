# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 16:37:45 2017

@author: Canopus
"""

import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from scipy.odr import *

file = 'hw3p5.dat'
x, y=np.loadtxt(file,unpack=True,usecols=[0,1])
n=np.arange(min(x),max(x),0.1)




#(a) fit Gauss function

 def Gaussf(p,t):
     tc=t-p[2]
     sig2=p[3]**2
     return p[0]+p[1]*exp(-0.5*tc**2/sig2)
 
model=Model(Gaussf)
data=RealData(x,y)
odr=ODR(data,model,beta0=[1.,1.,10.,1.])
out=odr.run() 
G_p=out.pprint
G_beta=out.beta
G_sd_beta=out.sd_beta
G_sq=out.sum_square

#p0=2.24597071, p1=1.21002339, p2=9.85323186, p3=3.2682955
#G_sq=7.6927121533619935


#(b) fit lorentz
def Lorf(q,t):
    tc=t-q[3]
    return q[0]+q[1]/(q[2]+tc**2)

model=Model(Lorf)
data=RealData(x,y)
odr=ODR(data,model, beta0=[1.,1.,2.,10.])
out=odr.run() 
L_p=out.pprint
L_beta=out.beta
L_sd_beta=out.sd_beta
L_sq=out.sum_square
 
# q0=1.98483518, q1=28.60639057, q2=19.0576559, q3=9.8159773
#L_sq=7.770760814699901


 #(c) plotting
 plt.plot(x,y,'ro'),plt.plot(n,Gaussf(G_beta,n),'k-',label='Gaussian'),plt.plot(n,Lorf(L_beta,n),'b--',label='Lorentz'),plt.xlabel('X'),plt.ylabel('Y'),plt.legend(loc=2),plt.savefig('Hw3-5.png')
