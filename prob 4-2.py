#HW4-2
from numpy import *
import numpy as np
import matplotlib.pyplot as plt

tmax=[0.01,0.1,1,10]
zmax=1.
n=10000
xn=np.zeros((n,4))
yn=np.zeros((n,4))
zn=np.zeros((n,4))

sin=1
#initial position=>
for j in range(4):
    for i in range(n):
        xi1=np.random.rand()
        xi2=np.random.rand()
        u=sqrt(xi1)
        sin=sqrt(1-u**2)
        p=2*pi*xi2
        xi3=np.random.rand()
        ta=-log(xi3)
        L=ta/tmax[j]
        x=L*si*cos(p)
        y=L*si*sin(p)
        z=L*u
        while (z<=1 and z>=0):
            xi4=np.random.rand()
            xi5=np.random.rand()
            p=2*pi*xi4
            u=2*xi5-1
            si=sqrt(1-u**2)
            xi3=np.random.rand()
            ta=-log(xi3)
            L=ta/tmax[j]
            x=x+L*si*cos(p)
            y=y+L*si*sin(p)
            z=z+L*u      
        xn[i,j]=x
        yn[i,j]=y
        zn[i,j]=z


#4-(a) #1000개의 photon으로 통계를 낸 결과
count_tra=np.zeros(4)
count_ref=np.zeros(4)
for j in range(4):
    for i in range(n):
        if(1<=zn[i,j]):
            count_tra[j]+=1.
        else:
            count_ref[j]+=1.


#경로 그리기


x001=[0.]
y001=[0.]
z001=[0.]
        xi1=np.random.rand()
        xi2=np.random.rand()
        u=sqrt(xi1)
        si=sqrt(1-u**2)
        p=2*pi*xi2
        xi3=np.random.rand()
        ta=-log(xi3)
        L=ta/tmax[0]
        x=L*si*cos(p)
        y=L*si*sin(p)
        z=L*u
        x001.append(x)
        y001.append(y)
        z001.append(z)
        while (z<=1 and z>=0):
            xi4=np.random.rand()
            xi5=np.random.rand()
            p=2*pi*xi4
            u=2*xi5-1
            si=sqrt(1-u**2)
            xi3=np.random.rand()
            ta=-log(xi3)
            L=ta/tmax[0]
            x=x+L*si*cos(p)
            y=y+L*si*sin(p)
            z=z+L*u      
            x001.append(x)
            y001.append(y)
            z001.append(z)

plt.plot(x001,z001),plt.xlabel('x'),plt.ylabel('z'),plt.title('path of poton when t=0.01'),plt.savefig('HW4-2(b)-p0.01.png')



x01=[0.]
y01=[0.]
z01=[0.]
xi1=np.random.rand()
xi2=np.random.rand()
u=sqrt(xi1)
si=sqrt(1-u**2)
p=2*pi*xi2
xi3=np.random.rand()
ta=-log(xi3)
L=ta/tmax[1]
x=L*si*cos(p)
y=L*si*sin(p)
z=L*u
x01.append(x)
y01.append(y)
z01.append(z)
        while (z<=1 and z>=0):
            xi4=np.random.rand()
            xi5=np.random.rand()
            p=2*pi*xi4
            u=2*xi5-1
            si=sqrt(1-u**2)
            xi3=np.random.rand()
            ta=-log(xi3)
            L=ta/tmax[1]
            x=x+L*si*cos(p)
            y=y+L*si*sin(p)
            z=z+L*u      
            x01.append(x)
            y01.append(y)
            z01.append(z)

plt.plot(x01,z01),plt.xlabel('x'),plt.ylabel('z'),plt.title('path of poton when t=0.1'),plt.savefig('HW4-2(b)-p0.1.png')


x1=[0.]
y1=[0.]
z1=[0.]
xi1=np.random.rand()
xi2=np.random.rand()
u=sqrt(xi1)
si=sqrt(1-u**2)
p=2*pi*xi2
xi3=np.random.rand()
ta=-log(xi3)
L=ta/tmax[2]
x=L*si*cos(p)
y=L*si*sin(p)
z=L*u
x1.append(x)
y1.append(y)
z1.append(z)
        while (z<=1 and z>=0):
            xi4=np.random.rand()
            xi5=np.random.rand()
            p=2*pi*xi4
            u=2*xi5-1
            si=sqrt(1-u**2)
            xi3=np.random.rand()
            ta=-log(xi3)
            L=ta/tmax[2]
            x=x+L*si*cos(p)
            y=y+L*si*sin(p)
            z=z+L*u      
            x1.append(x)
            y1.append(y)
            z1.append(z)

plt.plot(x1,z1),plt.xlabel('x'),plt.ylabel('z'),plt.title('path of poton when t=1.'),plt.savefig('HW4-2(b)-p1.png')

x10=[0.]
y10=[0.]
z10=[0.]
xi1=np.random.rand()
xi2=np.random.rand()
u=sqrt(xi1)
si=sqrt(1-u**2)
p=2*pi*xi2
xi3=np.random.rand()
ta=-log(xi3)
L=ta/tmax[3]
x=L*si*cos(p)
y=L*si*sin(p)
z=L*u
x10.append(x)
y10.append(y)
z10.append(z)
        while (z<=1 and z>=0):
            xi4=np.random.rand()
            xi5=np.random.rand()
            p=2*pi*xi4
            u=2*xi5-1
            si=sqrt(1-u**2)
            xi3=np.random.rand()
            ta=-log(xi3)
            L=ta/tmax[3]
            x=x+L*si*cos(p)
            y=y+L*si*sin(p)
            z=z+L*u      
            x10.append(x)
            y10.append(y)
            z10.append(z)

plt.plot(x10,z10),plt.xlabel('x'),plt.ylabel('z'),plt.title('path of poton when t=10.'),plt.savefig('HW4-2(b)-p10.png')








plt.plot(xn[:,0],zn[:,0],'bo'),plt.xlabel('x'),plt.ylabel('z'),plt.title('t=0.01'),plt.savefig('HW4-2(b)-0.01.png')
plt.plot(xn[:,1],zn[:,1],'bo'),plt.xlabel('x'),plt.ylabel('z'),plt.title('t=0.1'),plt.savefig('HW4-2(b)-0.1.png')
plt.plot(xn[:,2],zn[:,2],'bo'),plt.xlabel('x'),plt.ylabel('z'),plt.title('t=1'),plt.savefig('HW4-2(b)-1.png')
plt.plot(xn[:,3],zn[:,3],'bo'),plt.xlabel('x'),plt.ylabel('z'),plt.title('t=10.'),plt.savefig('HW4-2(b)-10.png')
