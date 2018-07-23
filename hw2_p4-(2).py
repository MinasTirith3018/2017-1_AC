# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 12:38:37 2017

@author: Canopus
"""

#Prob2 4-(2)


import numpy as np
from numpy import *

h=6.626*10**(-34)
k=1.381*10**(-23)
c=2.998*10**(8)
T=10**4

def B(l):
    y=(2*h*c**2/l**5)/(e**(h*c/(l*k*T))-1)
    return y

print "B(200nm) = {:.14e}".format(B(200e-9))
print "B(100nm) = {:.14e}".format(B(100e-9))

print "B(1500nm) = {:.14e}".format(B(1500e-9))
print "B(1400nm) = {:.14e}".format(B(1400e-9))

def B1(l):
    y=B(l)-10**13
    return y

a1=1500e-9
a2=1400e-9
a3=a2-B1(a2)*((a1-a2)/(B1(a1)-B1(a2)))
count=2

while(abs(a3-a2)>1e-14):
    a1=a2
    a2=a3
    a3=a2-B1(a2)*((a1-a2)/(B1(a1)-B1(a2)))
    count+=1
    print "{:3} {:.14e} {:.10e} {:.14e}".format(count,a3,B(a3),a3-a2)
    
b1=200e-9
b2=100e-9
b3=b2-B1(b2)*((b1-b2)/(B1(b1)-B1(b2)))
count=2

while(abs(b3-b2)>1e-14):
    b1=b2
    b2=b3
    b3=b2-B1(b2)*((b1-b2)/(B1(b1)-B1(b2)))
    count+=1
    print "{:3} {:.14e} {:.10e} {:.14e}".format(count,b3,B(b3),b3-b2)
    
print "Wavelengths which correspond to B(T)=10^13 J/s/m^3 are {:.10f}nm {:.10f}nm".format(b3*1e+9,a3*1e+9)
    