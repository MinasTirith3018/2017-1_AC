#prob 5-4

from numpy import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

beta=np.zeros((7,7))
beta[2][1]=0.125
beta[3][1]=0.21
beta[4][1]=0.048
beta[5][1]=0.050
beta[6][1]=0.025
beta[3][2]=0.17
beta[4][2]=0.048
beta[5][2]=0.050
beta[6][2]=0.025
beta[4][3]=0.048
beta[5][3]=0.050
beta[6][3]=0.025
beta[5][4]=-0.018

    
og1=np.zeros((7,7))
og1[2][1]=0.408
og1[3][1]=0.272
og1[4][1]=0.2934
og1[5][1]=0.0326
og1[6][1]=0.1323
og1[3][2]=1.120   
og1[4][2]=0.8803
og1[5][2]=0.0977
og1[6][2]=0.3968
og1[4][3]=1.4672
og1[5][3]=0.1628
og1[6][3]=0.6613
og1[5][4]=0.8338

A=np.zeros((7,7))
A[2][1]=2.08*10**(-6)
A[3][1]=1.16*10**(-12)
A[4][1]=5.35*10**(-7)
A[5][1]=0.
A[6][1]=0.
A[3][2]=7.46*10**(-6)
A[4][2]=1.01*10**(-3)
A[5][2]=3.38*10**(-2)
A[6][2]=4.80*10
A[4][3]=2.99*10**(-3)
A[5][3]=1.51*10**(-4)
A[6][3]=1.07*100
A[5][4]=1.12
 
 
E=np.zeros((7,7))
E[1][2]=0.00609
E[1][3]=0.01628
E[1][4]=1.89879
E[1][5]=4.05244
E[1][6]=5.80061
E[2][3]=0.01019
E[2][4]=1.89270
E[2][5]=4.04635
E[2][6]=5.79452
E[3][4]=1.88251
E[3][5]=4.03616
E[4][5]=2.15365
E[4][6]=3.90182
E[5][6]=1.74817

w=np.array([0.,1.,3.,5.,5.,1.,1.])


T=input('input the temperature : ')
ne=input('input the density of electron :')
#%%
T=20000.
ne=10000.

t=T/10**4
q=np.zeros((7,7))
for i in range(1,7):
    for j in range(i+1,7):
        q[j][i]=(8.629*10**(-8))/t**0.5*(og1[j][i]*t**(beta[j][i]))/w[j]
        q[i][j]=q[j][i]*w[j]/w[i]*e**(-1.160*E[i][j]/t)
        

p=np.zeros((7,7))
p[6]=np.array([0.,1.,1.,1.,1.,1.,1.])

for i in range(1,6):
    for k in range(1,7):
        if(k!=i):  p[i][i]+=ne*q[i][k]
    for k in range(1,i):
        p[i][i]+=ne*A[i][k]

for i in range(1,6):
    for k in range(1,7):
        if(k!=i): p[i][k]-=ne*q[k][i]
    for k in range(i+1,7):
        p[i][k]-=A[k][i]


#Gauss Jordan Elimination
a=p
b=np.zeros(7)
b[6]=1.
for k in range(1,7):
    for j in range(k+1,7):
        coef=a[j][k]/a[k][k]
        for i in range(k,7):
            a[j][i]-=coef*a[k][i]
        b[j]-=coef*b[k]

ni=np.zeros(7)
ni[6]=b[6]/a[6][6]
for k in range(5,0,-1):
    su=0.
    for i in range(k,6):
        su+=a[k][i+1]*ni[i+1]
    ni[k]=(b[k]-su)/a[k][k]

#%%
Temp=np.arange(5000.,20000,100)
R=np.zeros((len(Temp),5))

for h in range(5):
    ne=10**(h+1)
    for u in range(len(Temp)):
        T=Temp[u]
        t=T/10**4
        q=np.zeros((7,7))
        for i in range(1,7):
            for j in range(i+1,7):
                q[j][i]=(8.629*10**(-8))/t**0.5*(og1[j][i]*t**(beta[j][i]))/w[j]
                q[i][j]=q[j][i]*w[j]/w[i]*e**(-1.160*E[i][j]/t)                
        p=np.zeros((7,7))
        p[6]=np.array([0.,1.,1.,1.,1.,1.,1.])        
        for i in range(1,6):
            for k in range(1,7):
                if(k!=i):  p[i][i]+=ne*q[i][k]
            for k in range(1,i):
                p[i][i]+=ne*A[i][k]        
        for i in range(1,6):
            for k in range(1,7):
                if(k!=i): p[i][k]-=ne*q[k][i]
            for k in range(i+1,7):
                p[i][k]-=A[k][i]        
        #Gauss Jordan Elimination
        a=p
        b=np.zeros(7)
        b[6]=1.
        for k in range(1,7):
            for j in range(k+1,7):
                coef=a[j][k]/a[k][k]
                for i in range(k,7):
                    a[j][i]-=coef*a[k][i]
                b[j]-=coef*b[k]    
        ni=np.zeros(7)
        ni[6]=b[6]/a[6][6]
        for k in range(5,0,-1):
            su=0.
            for i in range(k,6):
                su+=a[k][i+1]*ni[i+1]
            ni[k]=(b[k]-su)/a[k][k]
        R[u,h]=ni[4]*A[4][3]*5755/(ni[5]*A[5][4]*6584)

plt.plot(Temp,R[:,0],label='ne=10'),plt.plot(Temp,R[:,1],label='ne=100'),plt.plot(Temp,R[:,2],label='ne=1000'),plt.plot(Temp,R[:,3],label='ne=10000'),plt.plot(Temp,R[:,4],label='ne=100000'),plt.legend(),plt.xlabel('Temperature'),plt.ylabel('R'),plt.title('ratio of R'),plt.savefig('prob5-4(c)-1.png')

plt.plot(Temp,R[:,0],label='ne=10'),plt.plot(Temp,R[:,1],label='ne=100'),plt.plot(Temp,R[:,2],label='ne=1000'),plt.plot(Temp,R[:,3],label='ne=10000'),plt.plot(Temp,R[:,4],label='ne=100000'),plt.legend(),plt.xlabel('Temperature'),plt.ylabel('R'),plt.title('ratio of R'),plt.xlim(6680,6685),plt.ylim(255,255.5),plt.savefig('prob5-4(c)-2.png')
