from numpy import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def dudx(u,x):
    return (2/x-1/x**2)/(u-1/u)

#x=5 to 0.1 
#u=3,0.1,0.01 at x=5


x1=np.linspace(5,0.1,491)

y1=odeint(dudx,3,x1)
y2=odeint(dudx,0.1,x1)
y3=odeint(dudx,0.01,x1)


x2=np.arange(1.65,5,0.01)
y2p=odeint(dudx,1.000001,x2)

plt.plot(x1,y1[:,0],'b-',label='u(5)=3'),plt.plot(x1,y2[:,0],'r-',label='u(5)=0.1'),plt.plot(x2,y2p,'r-'),plt.plot(x1,y3[:,0],'g-',label='u(5)=0.01'),plt.xlabel('x'),plt.ylabel('u'),plt.legend(loc=2),plt.xlim(0.1,5),plt.savefig('HW4-3(a).png')



#(c)
t1=np.arange(0.5,5,0.01)
t2=np.arange(0.5,0.1,-0.01)
u1=odeint(dudx,1.000001,t1)
u2=odeint(dudx,1.000001,t2)

plt.plot(t1,u1,'b-',label='isothermal Parker Winds'),plt.plot(t2,1/u2,'b-'),plt.plot(t1,1/u1,'r-'),plt.plot(t2,u2,'r-',label='Bondi accretion'),plt.legend(loc=1),plt.xlim(0.1,5),plt.xticks(np.arange(0.1,5.1,0.5)),plt.xlabel('x'),plt.ylabel('u'),plt.savefig('HW4-3(c).png')
