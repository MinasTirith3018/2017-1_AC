# -*- coding: utf-8 -*-
"""
Created on Sun Jun 04 15:59:18 2017

@author: Canopus
"""

#HW6-2. find minimum2


import numpy as np
from numpy import *
from scipy import linalg
import scipy.optimize as opt
import matplotlib.pyplot as plt
import math
from scipy.optimize import minimize


def f(t):
    x,y,z=t[0],t[1],t[2]
    return 100*(y-x**2)**2+(1-x)**2+100*(z-y**2)**2+(1-z)**2

tol=1.e-6
x0=np.array([0.,2.,-1.])

#(a) Powell 
res1=minimize(f,x0,method='Powell',options={'xtol':tol, 'disp':True})
#powell- iteration:23, (1,1,1)
#or

def Golden2d(x,direct,Tol):
    R=(sqrt(5.)-1.)/2
    b=x+R*direct*2
    a=x-R*direct*2
    while (sqrt(sum((a-b)**2))>Tol):
        x1=b-R*(b-a)
        x2=a+R*(b-a)    
        f1=f(x1)
        f2=f(x2)
        if(f2>f1): b=x2
        else : a=x1
    if(f(a)>f(b)): xmin=b
    else: xmin=a
    return xmin

dir1=np.array([1.,0.,0.])
dir2=np.array([0.,1.,0.])
dir3=np.array([0.,0.,1.])

    x1=Golden2d(x0,dir1,tol)
    x2=Golden2d(x1,dir2,tol)
    x3=Golden2d(x2,dir3,tol)
    dir4=(x3-x0)/sqrt(sum(x3-x0)**2)
    x4=Golden2d(x3,dir4,tol)
    count=4.

while (sqrt(sum((x4-x1)**2))>tol):
    x1=Golden2d(x4,dir1,tol)
    x2=Golden2d(x1,dir2,tol)
    x3=Golden2d(x2,dir3,tol)
    dir4=(x3-x4)/sqrt(sum(x3-x4)**2)
    x4=Golden2d(x3,dir4,tol)
    count+=4
    dir1=dir2
    dir2=dir3
    dir3=dir4
    
#iteration : 40 (즉 10세트 실시)
#x4=array([ 1.        ,  1.00000011,  1.00000021])
 
#(b) CG method
x0=np.array([0.,2.,-1.])
res2=minimize(f,x0,method='CG', options={'xtol':tol,'disp':True})
#cg: iteration:68, array([ 0.9999989 ,  0.99999779,  0.99999559])

#or
def gradf(r):
    x=r[0]
    y=r[1]
    z=r[2]
    grx=-400*x*(y-x**2)-2*(1-x)
    gry=200*(y-x**2) +400*y*(y**2-z)
    grz=200*(z-y**2)+2*(z-1)
    return np.array([grx,gry,grz])


g0=-gradf(x0)
count=0.

 x1=Golden2d(x0,g0,tol)
 g1=-gradf(x1)+g0*sum((gradf(x1))**2)/sum(gradf(x0)**2)
 x2=Golden2d(x1,g1,tol)
 g2=-gradf(x2)+g1*sum((gradf(x2))**2)/sum(gradf(x1)**2)
 count+=2.

while(sqrt(sum((x2-x1)**2))>(tol)):
    x1=Golden2d(x2,g2,tol)
    g1=-gradf(x1)+g2*sum((gradf(x1))**2)/sum(gradf(x2)**2)
    x2=Golden2d(x1,g1,tol)
    g2=-gradf(x2)+g1*sum((gradf(x2))**2)/sum(gradf(x1)**2)
    count+=2.

#iteration=78
#x2:array([ 1.00002355,  1.00004486,  1.00008775])




