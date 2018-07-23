# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 11:56:36 2017

@author: Canopus
"""

import numpy as np
from numpy import *
import matplotlib.pyplot as plt

file = 'BlackHall.txt'
MBH, dMBH, sig, dsig=np.loadtxt(file,unpack=True,usecols=[0,1,2,3])


#(a) ignore Error, fit a and b
cofa, resa, _, _, _=np.polyfit(log(sig),log(MBH),1,full=True)

print cofa
print resa

#a=1.56205097
#b=3.28965514
#err=85.82221847

#(b) Consider the measurement Error
def lin_func(p,X):
    return p[0]+p[1]*X

lin_model=Model(lin_func)
data=RealData(log(sig),log(MBH),sx=log(dsig),sy=log(dMBH))
odr=ODR(data,lin_model, beta0=[0.,1.0])

out=odr.run()
pb=out.pprint
beta=out.beta
sd_beta=out.sd_beta
s_sq=out.sum_square
beta
s_sq
#a=-0.03526799
#b=3.58736461
#err=0.2817686570823044


#(c) plotting
def fa(x):
    return cofa[1]+cofa[0]*x
plt.errorbar(log(sig),log(MBH),xerr=log(dsig),yerr=log(dMBH)),plt.plot(log(sig),log(MBH),'ro'),plt.plot(log(sig),fa(log(sig)),'k-'), plt.plot(log(sig),lin_func(beta,log(sig)),'y-'),plt.xlabel('ln(sig)'),plt.ylabel('ln(MBH)'),plt.savefig('Hw3-4-(c)-1.png')
plt.plot(log(sig),log(MBH),'ro'),plt.plot(log(sig),fa(log(sig)),'k-',label='(a) without err'), plt.plot(log(sig),lin_func(beta,log(sig)),'y-',label='(b) with err'),plt.legend(loc=2),plt.xlabel('ln(sig)'),plt.ylabel('ln(MBH)'),plt.savefig('Hw3-4-(c)-2.png')


#(d) 
data=RealData(log(MBH),log(sig),sx=log(dMBH),sy=log(dsig))
odr=ODR(data,lin_model, beta0=[0.,1.0])

out=odr.run()
pd=out.pprint
betad=out.beta
sd_betad=out.sd_beta
s_sqd=out.sum_square
#c=0.00990783
#d=0.27875184
#err=0.2817686571030568

# -a/b=0.009831169961154523
# 1/b=0.27875616444315915

plt.errorbar(log(MBH),log(sig),xerr=log(dMBH),yerr=log(dsig)),plt.plot(log(MBH),log(sig),'ro'), plt.plot(log(MBH),lin_func(betad,log(MBH)),'y-'),plt.xlabel('ln(MBH)'),plt.ylabel('ln(sig)'),plt.savefig('Hw3-4-(d)-1.png')
plt.plot(log(MBH),log(sig),'ro'), plt.plot(log(MBH),lin_func(betad,log(MBH)),'y-',label='(d) with err'),plt.legend(loc=2),plt.xlabel('ln(MBH)'),plt.ylabel('ln(sig)'),plt.savefig('Hw3-4-(d)-2.png')




