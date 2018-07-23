# -*- coding: utf-8 -*-
"""
Created on Sun Jun 04 17:42:20 2017

@author: Canopus
"""

#prob 6-3


import numpy as np
from numpy import *
import matplotlib.pyplot as plt

sol=np.loadtxt('sol_vel.dat')
t=sol[:,0]
vha=sol[:,1]
vca=sol[:,2]
n=len(vha)



v1=np.fft.fft(vha)
v2=np.fft.fft(vca)
freq=np.fft.fftfreq(n,1./n)
freq_s=np.fft.fftshift(freq)
v1_s=np.fft.fftshift(v1)
v2_s=np.fft.fftshift(v2)

plt.plot(t,vha,label='V_Ha'),plt.plot(t,vca,label='V_CaII'),plt.xticks(arange(0,28.2,2)),plt.xlim(0,max(t)),plt.title('Velocity'),plt.legend(),plt.savefig('Hw6-3(a).png')

plt.plot(freq_s,abs(v1_s),label='V_Ha'),plt.xlabel('k_shifted'),plt.ylabel('power'),plt.title('Velocity FFT'),plt.plot(freq_s,abs(v2_s),label='V_CaII'),plt.legend(),plt.savefig('Hw6-3(b).png')



# PART (b)
max1 = np.argmax(abs(v1_s))
max2 = np.argmax(abs(v2_s))
kmax1 = abs(freq_s[max1])
kmax2 = abs(freq_s[max2])

#kmax1=9.0
#kmax2=9.0

dt = t[n-1]-t[0]     # time interval
P1 = dt/float(kmax1) # vHa의 주기
P2 = dt/float(kmax1) # VCaII의 주기

#P1=3.1333333 min
#P2=3.1333333 min
             

#%%(c) Correalation
v=v1*v2
iff=np.fft.ifft(v)
plt.plot(t,iff),plt.xticks(arange(0,28.2,2)),plt.xlim(0,max(t)),plt.title('Corr'),plt.ylabel('Corr'),plt.xlabel('t(min)'),plt.savefig('Hw6-3(c).png')
