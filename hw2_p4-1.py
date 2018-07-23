#HW2 4-(1)


import numpy as np
from numpy import *

h=6.626*10**(-34)
k=1.381*10**(-23)
c=2.998*10**(8)
a=h*c/k

def Bd(x):
	y=0.2*a/(1-e**(-(a/x)))
	return y

x0=1
n=1

while(abs(Bd(x0)-x0)>1e-11):
	x0=Bd(x0)
	n+=1

print "Using Fixed-iteration method Calculation : {:3} times, Wien displacement constant is {:.16e} ".format(n,Bd(x0))




