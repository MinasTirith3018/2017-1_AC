#HW4-1
from numpy import *
import numpy as np
import matplotlib.pyplot as plt



n=10**7

#d=3
d3=np.zeros(100)
for i in range(100):
    x=2*np.random.rand(n)-1
    y=2*np.random.rand(n)-1
    z=2*np.random.rand(n)-1
    count=0.
    for j in range(n):
        if (x[j]**2+y[j]**2+z[j]**2)<=1. :
            count+=1.
    d3[i]=count


md3=np.average(d3)*8
std3=np.std(d3*8)

#Mean of d3=4.1889158959999993
#Std 0f d3=0.0011562630934108314

#d=4
d4=np.zeros(100)
for i in range(100):
    x=2*np.random.rand(n)-1
    y=2*np.random.rand(n)-1
    z=2*np.random.rand(n)-1
    v=2*np.random.rand(n)-1
    count=0.
    for j in range(n):
        if (x[j]**2+y[j]**2+z[j]**2+v[j]**2)<=1. :
            count+=1.
    d4[i]=count/n

md4=np.average(d4*(16.))
std4=np.std(d4*(16.))


#d=5
d5=np.zeros(100)
for i in range(100):
    x=2*np.random.rand(n)-1
    y=2*np.random.rand(n)-1
    z=2*np.random.rand(n)-1
    v=2*np.random.rand(n)-1
    w=2*np.random.rand(n)-1
    count=0.
    for j in range(n):
        if (x[j]**2+y[j]**2+z[j]**2+v[j]**2+w[j]**2)<=1. :
            count+=1.
    d5[i]=count/n

md5=np.average(d5*(32.))
std5=np.std(d5*(32.))


#gamma func(5/2)=sqrt(pi)*3/4, V3=4.1887902047863905
#gamma func(3)=2 V4=(pi)**2/2=4.934802200544679
#gamma func(7/2)=sqrt(pi)*15/8  V5=(pi**2)*8/15=5.263789013914324  <-Calculate by Wolfram alpha
