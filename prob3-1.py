# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 20:28:25 2017

@author: Canopus
"""

import numpy as np
from numpy import *

n=100000
def f(x):
    return sin(x**4)

h=(4.-0.)/n
ST=(f(0)+f(4))*h/2
SS=(f(0)+f(4))*h/3
SG=0.

#(a) the composite trapezoidal rule
for i in range(1,n):
    x=0+i*h
    ST+=f(x)*h  


#(b) the composite Simpson's Rule
for i in range(1,n):
    if(i%2==1):
        x=i*h
        SS+=4*h*f(x)/3
    else:
        x=i*h
        SS+=2*h*f(x)/3
                 
#(c) Gaussian Quadrature
t, w=np.polynomial.legendre.leggauss(1000)
for i in range(1000):
    SG+=(4-0)/2*w[i]*f((t[i]*(4-0)+4)/2)
    

print "The composite trapezoidal rule : {:.6f}".format(ST)
print "The composite Simpson's rule : {:.6f}".format(SS)
print "The Gaussian Quadrature : {:.6f}".format(SG)
