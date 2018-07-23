#Prob 5-3.

from numpy import *
import numpy as np
import matplotlib.pyplot as plt

n=256
a=np.zeros((n,n))
b=np.zeros(n)

for i in range(1,n-1):
    a[i][i]=-2
    a[i][i-1]=1
    a[i][i+1]=1
    b[i]=-(2*pi/n)**2*cos(2*pi*(i+1)/n)

a[0][0]=-2
a[0][1]=1
a[255][255]=-2
a[255][254]=1
b[0]=-(2*pi/n)**2*cos(2*pi*1/n)
b[255]=-(2*pi/n)**2*cos(2*pi*256/n)

#(a)Gordon jordan elimination
for k in range(n):
    for j in range(k+1,n):
        coef=a[j][k]/a[k][k]
        for i in range(k,n):
            a[j][i]-=coef*a[k][i]
        b[j]-=coef*b[k]

g=np.zeros(n)
g[n-1]=b[n-1]/a[n-1][n-1]
for k in range(n-2,-1,-1):
    su=0.
    for i in range(k,n-1):
        su+=a[k][i+1]*g[i+1]
    g[k]=(b[k]-su)/a[k][k]
    
plt.plot(g),plt.xlim(1,256),plt.xticks(np.arange(0,257.,32)),plt.title('GJ Elimination method'),plt.xlabel('i'),plt.ylabel('ui'),plt.savefig('Prob5-3(a).png')


#forward and Backward substitution method

n=256
u=np.zeros((n,n))
v=np.zeros(n)
for i in range(1,n-1):
    u[i][i]=-2
    u[i][i-1]=1
    u[i][i+1]=1
    v[i]=-(2*pi/n)**2*cos(2*pi*(i+1)/n)

u[0][0]=-2
u[0][1]=1
u[255][255]=-2
u[255][254]=1
v[0]=-(2*pi/n)**2*cos(2*pi*1/n)
v[255]=-(2*pi/n)**2*cos(2*pi*256/n)

bet=u[0][0]
rho=np.zeros(n)
rho[0]=v[0]/bet
for i in range(1,n):
    u[i-1][i]=u[i-1][i]/bet
    bet=u[i][i]-u[i][i-1]*u[i-1][i]
    rho[i]=(v[i]-u[i][i-1]*rho[i-1])/bet
    
    
x=np.zeros(n)
x[n-1]=rho[n-1]
for i in range(n-2,-1,-1):x[i]=rho[i]-u[i][i+1]*x[i+1]
plt.plot(x),plt.xlim(1,256),plt.xticks(np.arange(0,257.,32)),plt.xlabel('i'),plt.ylabel('ui'),plt.title('Forward and Backward method'),plt.savefig('prob5-3(b).png')
#np.linspace(0.,2*pi,9)

## comparing
t=np.zeros(n)
for i in range(n): t[i]=2*pi*(i+1)/n
gc=g-cos(t)
xc=x-cos(t)
plt.plot(gc),plt.xlabel('i'),plt.title('ui-cos(x),GJ'),plt.savefig('prob5-3(c)-1.png')
plt.plot(xc),plt.xlabel('i'),plt.title('ui-cos(x),FB'),plt.savefig('prob5-3(c)-2.png')
