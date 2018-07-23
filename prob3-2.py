# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 03:31:35 2017

@author: Canopus
"""

import numpy as np
from numpy import *
import matplotlib.pyplot as plt


n=100000
ui=np.arange(0,1.01,0.01)


def H(p,u):
    return (p*arctan(u*tan(p))/(1-p/tan(p)))


Hi=np.zeros(len(ui))
h=(0.5*pi-0)/n

#the composite Simpson's Rule

for j in range(len(ui)):
    SS=(H(0.0000001,ui[j])+H(0.4999999*pi,ui[j]))*h/3       
    for i in range(1,n):
           if(i%2==1):
               x=i*h
               SS+=4*h*H(x,ui[j])/3
           else:
               x=i*h
               SS+=2*h*H(x,ui[j])/3
    Hi[j]=exp(SS/pi)/(1+ui[j])



plt.plot(ui,Hi),plt.xlabel('u'),plt.ylabel('H(u)'),plt.savefig('Hw3-2.png')
    