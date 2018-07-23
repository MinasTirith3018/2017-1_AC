# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 01:55:16 2017

@author: Canopus
"""

#hw2-5. Kapler problem

from numpy import *
import numpy as np

P=365.25365
a=1.496e+8
e=0.0167
b=a*(1-e**2)**0.5
t1=182
t2=273

a1=pi/180*175
b1=pi/180*185

a2=pi/180*265
b2=pi/180*275

def f(t,E):
    y=E-(2*pi*t/P+e*sin(E))
    return y
def x(E):
    return a*cos(E)
def y(E):
    return b*sin(E)

#Bisection

c1=(a1+b1)/2
n=1
while((abs(b1-c1)>1e-10)):
    if(f(t1,c1)*f(t1,b1)<0):
        a1=c1
        c1=(a1+b1)/2
        n=n+1
        print "{:3}times {:.12e}".format(n,c1)
    if(f(t1,c1)*f(t1,a1)<0):
        b1=c1
        c1=(a1+b1)/2
        n+=1
        print "{:3}times {:.12e}".format(n,c1)
        
c2=(a2+b2)/2
n=1
while((abs(b2-c2)>1e-10)):
    if(f(t1,c2)*f(t1,b2)<0):
        a2=c2
        c2=(a2+b2)/2
        n=n+1
        print "{:3}times {:.12e}".format(n,c2)
    if(f(t1,c2)*f(t1,a2)<0):
        b2=c2
        c2=(a2+b2)/2
        n+=1
        print "{:3}times {:.12e}".format(n,c2)
        
print "When t={}days, E={:.12}rad, x={:.12e}km, y={:.12e}km".format(t1,c1,x(c1),y(c1))
print "When t={}days, E={:.12}rad, x={:.12e}km, y={:.12e}km".format(t2,c2,x(c2),y(c2))





#NR-Method


#fixed-iteration method
    