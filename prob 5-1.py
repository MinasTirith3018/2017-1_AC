#Prob 5-1

from numpy import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

h=0.0001
t=np.arange(0.,50.,h)

r1=np.zeros((len(t),2))
r2=np.zeros((len(t),2))

r1[0,0]=-0.5
r1[0,1]=0.
r2[0,0]=1.0
r2[0,1]=0.


v1=np.zeros((len(t),2))
v2=np.zeros((len(t),2))
v1[0,0]=0.01
v1[0,1]=0.05
v2[0,0]=0.02
v2[0,1]=0.2


#half
hv1=np.zeros((len(t),2))
hv2=np.zeros((len(t),2))

def a1(a,b):
    r=((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
    a1x=-0.5*(a[0]-b[0])/r**3
    a1y=-0.5*(a[1]-b[1])/r**3
    return np.array([a1x,a1y])

def a2(a,b):
    r=((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
    a2x=-(b[0]-a[0])/r**3
    a2y=-(b[1]-a[1])/r**3
    return np.array([a2x,a2y])

hv1[0]=v1[0]+h/2*a1(r1[0],r2[0])
hv2[0]=v2[0]+h/2*a2(r1[0],r2[0])
mg=np.zeros((len(t),2))
mg[0]=r1[0]*1/1.5+r2[0]*0.5/1.5

for n in range(1,len(t)):
    r1[n]=r1[n-1]+h*hv1[n-1]
    r2[n]=r2[n-1]+h*hv2[n-1]
    v1[n]=hv1[n-1]+h/2*a1(r1[n],r2[n])
    v2[n]=hv2[n-1]+h/2*a2(r1[n],r2[n])
    hv1[n]=hv1[n-1]+h*a1(r1[n],r2[n])
    hv2[n]=hv2[n-1]+h*a2(r1[n],r2[n])
    mg[n]=r1[n]*1/1.5+r2[n]*0.5/1.5

plt.plot(r1[:,0],r1[:,1],label='S1'),plt.plot(r2[:,0],r2[:,1],label='S2'),plt.plot(mg[:,0],mg[:,1],label='MC'),plt.legend(),plt.xlabel('x'),plt.ylabel('y'),plt.title('Orbit of Binary star'),plt.grid(),plt.savefig('Prob5-1-(a).png')



#(c) 0~1000s plotting L and E
t2=np.arange(0,1000,h)
L=np.zeros(len(t2))
E=np.zeros(len(t2))


r1=np.zeros((len(t2),2))
r2=np.zeros((len(t2),2))
r1[0]=[-0.5,0.]
r2[0]=[1.0,0.]
v1=np.zeros((len(t2),2))
v2=np.zeros((len(t2),2))
v1[0]=[0.01,0.05]
v2[0]=[0.02,0.2]
hv1=np.zeros((len(t2),2))
hv2=np.zeros((len(t2),2))
hv1[0]=v1[0]+h/2*a1(r1[0],r2[0])
hv2[0]=v2[0]+h/2*a2(r1[0],r2[0])
mg=np.zeros((len(t2),2))
mg[0]=r1[0]*1/1.5+r2[0]*0.5/1.5

  
L[0]=(r1[0][0]*v1[0][1]-r1[0][1]*v1[0][0])+0.5*(r2[0][0]*v2[0][1]-r2[0][1]*v2[0][0])
E[0]=0.5*(v1[0][0]**2+v1[0][1]**2)+0.25*(v2[0][0]**2+v2[0][1]**2)-0.5/((r1[0][0]-r2[0][0])**2+(r1[0][1]-r2[0][1])**2)**0.5

for n in range(1,len(t2)):
    r1[n]=r1[n-1]+h*hv1[n-1]
    r2[n]=r2[n-1]+h*hv2[n-1]
    v1[n]=hv1[n-1]+h/2*a1(r1[n],r2[n])
    v2[n]=hv2[n-1]+h/2*a2(r1[n],r2[n])
    hv1[n]=hv1[n-1]+h*a1(r1[n],r2[n])
    hv2[n]=hv2[n-1]+h*a2(r1[n],r2[n])
    mg[n]=r1[n]*1/1.5+r2[n]*0.5/1.5
    L[n]=(r1[n][0]*v1[n][1]-r1[n][1]*v1[n][0])+0.5*(r2[n][0]*v2[n][1]-r2[n][1]*v2[n][0])
    E[n]=0.5*(v1[n][0]**2+v1[n][1]**2)+0.25*(v2[n][0]**2+v2[n][1]**2)-0.5/((r1[n][0]-r2[n][0])**2+(r1[n][1]-r2[n][1])**2)**0.5
   
plt.plot(t2,L,label='L'),plt.xlabel('t'),plt.title('Angluar momentum'),plt.savefig('prob5-1-(d)L.png')
plt.plot(t2,E,label='E'),plt.xlabel('t'),plt.title('Energy'),plt.savefig('prob5-1-(d)E.png')
