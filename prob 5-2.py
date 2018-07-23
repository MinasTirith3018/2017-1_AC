#Prob 5-2

from numpy import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#(1) Q=r lamda =?

Q=5
yini=np.array([1.,0.])
x=np.linspace(0.,pi,100)

l1=5.
l2=-5.

def deriv1(y,x):
    dydt1=y[1]
    dydt2=-(l1-2*Q*cos(2*x))*y[0]
    return [dydt1,dydt2]

def deriv2(y,x):
    dydt1=y[1]
    dydt2=-(l2-2*Q*cos(2*x))*y[0]
    return [dydt1,dydt2]


y1=odeint(deriv1,yini,x)
y2=odeint(deriv2,yini,x)
B1=y1[99,1]
B2=y2[99,1]

lnew=l2+(l2-l1)*(0.-B2)/(B2-B1)


while(abs(lnew-l2)>10**(-8)):
    l2=l1
    l1=lnew
    y1=odeint(deriv1,yini,x)
    y2=odeint(deriv2,yini,x)
    B1=y1[99,1]
    B2=y2[99,1]
    lnew=l2+(l2-l1)*(0.-B2)/(B2-B1)

# lnew=11.54883171536912
# lnew=-5.80004600546176
# lnew=7.4491098578413242

#(2) 0=<Q=<10 lambda ?
q=np.linspace(0.,10.,501) 
lam=np.zeros(len(q))

for i in arange(len(q)):
    l1=5
    l2=-5
    def deriv1(y,x):
      dydt1=y[1]
      dydt2=-(l1-2*q[i]*cos(2*x))*y[0]
      return [dydt1,dydt2]

    def deriv2(y,x):
        dydt1=y[1]
        dydt2=-(l2-2*q[i]*cos(2*x))*y[0]
        return [dydt1,dydt2]

    y1=odeint(deriv1,yini,x)
    y2=odeint(deriv2,yini,x)
    B1=y1[99,1]
    B2=y2[99,1]
    lnew=l2+(l2-l1)*(0.-B2)/(B2-B1)

    while(abs(lnew-l2)>10**(-8)):
        l2=l1
        l1=lnew
        y1=odeint(deriv1,yini,x)
        y2=odeint(deriv2,yini,x)
        B1=y1[99,1]
        B2=y2[99,1]
        lnew=l2+(l2-l1)*(0.-B2)/(B2-B1)

    lam[i]=lnew

plt.plot(q,lam),plt.xlabel('Q'),plt.xlim(0,10),plt.xticks(np.arange(0.,10.5,1.)),plt.ylabel('lamda'),plt.savefig('prob5-2.png')

