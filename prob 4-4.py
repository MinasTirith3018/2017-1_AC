#HW4-4(b)

from numpy import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


n=input(" ")

def deriv(y,x):
    dydt1=y[1]
    dydt2=-2/x*y[1]-(y[0])**n
    return [dydt1,dydt2]
    


xi0=[1.0,0.0]
t=np.arange(0.000000000001,100,0.01)
y=odeint(deriv,xi0,t)

theta1=y[:,0]

plt.plot(t,theta1,label='python solution'),plt.xlabel('$xi$'),plt.ylabel('$Theta$'),plt.legend(loc=1),plt.savefig('HW4-4(b)-n.png')
plt.plot(t,(1-t**2/6),label='analytic solution,n=0')
plt.plot(t,(np.sin(t)/t),label='analytic solution,n=1')
plt.plot(t,(1+t**2/3)**(-0.5),label='analytic solution,n=5'),plt.title('n=5')


