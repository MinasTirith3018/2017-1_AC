# -*- coding: utf-8 -*-
"""
Created on Sat Jun 03 20:15:07 2017

@author: Canopus
"""

#HW6-1. find minimum

import numpy as np
from numpy import *
from scipy import linalg
import scipy.optimize as opt
import matplotlib.pyplot as plt
import math
from scipy.optimize import minimize


def f(t):
    x,y=t[0],t[1]
    return 2.*x**2+y**2-2.*x*y+abs(x-3.)+abs(y-2.)

def gradf(t):
    x,y=t[0],t[1]
    gx=4.*x-2.*y+abs(x-3.)/(x-3.)
    gy=2*y-2*x+abs(y-2.)/(y-2.)
    return np.array([gx,gy])

tol=1.e-6

x=np.arange(-2,3.01,0.01)
y=np.arange(-2,2.01,0.01)
X,Y=np.meshgrid(x,y)
E=np.log10(f(np.meshgrid(x,y)))
lev1=np.linspace(np.min(E),np.max(E),20)

#%%
#(1) Newton's method
def s(t):
    s0=-2*gradf(t)[1]-2*gradf(t)[0]
    s1=-2*gradf(t)[0]-4*gradf(t)[1]
    return np.array([s0/4.,s1/4.])


x1=np.array([-1,1.])
px1,py1=[x1[0]],[x1[1]]
xn=x1+s(x1)
px1.append(xn[0])
py1.append(xn[1])
while(sqrt(sum((xn-x1)**2))>tol):
    x1=xn
    xn=x1+s(x1)
    px1.append(xn[0])
    py1.append(xn[1])
     
    
x2=np.array([0.,0.])
px2,py2=[x2[0]],[x2[1]]
xn=x2+s(x2)
px2.append(xn[0])
py2.append(xn[1])
while(sqrt(sum((xn-x2)**2))>tol):
    x2=xn
    xn=x2+s(x2)
    px2.append(xn[0])
    py2.append(xn[1])


x3=np.array([2.0,0.0])
px3,py3=[x3[0]],[x3[1]]
xn=x3+s(x3)
px3.append(xn[0])
py3.append(xn[1])
while(sqrt(sum((xn-x3)**2))>tol):
    x3=xn
    xn=x3+s(x3)
    px3.append(xn[0])
    py3.append(xn[1])

#minimum point (x,y)=(1.0,1.5)

plt.figure(figsize=(10,8)),plt.contourf(X,Y,E,lev1),plt.colorbar(),plt.axis('equal'),plt.title('Newton method'),\
            plt.plot(px1,py1,'ro-',label='(-1,1)'),\
            plt.plot(px2,py2,'*-',label='(0,0)'),\
            plt.plot(px3,py3,'d-',label='(2,0)'),plt.legend(),plt.savefig('hw6-1(a).png')
        
                         

#%%
#(2) Steepest test

def Golden2d(x,direct,Tol):
    R=(sqrt(5.)-1.)/2
    b=x+R*direct*5
    a=x-R*direct*5
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



x1=np.array([-1,1.])
px1,py1=[x1[0]],[x1[1]]
def cbF1(x):
    global px1,py1
    px1.append(x[0])
    py1.append(x[1])

n1=gradf(x1)/sqrt(sum(gradf(x1)**2))
nh1=np.array([-n1[1],n1[0]])
xn=Golden2d(x1,n1,tol)
cbF1(xn)
xn_1=Golden2d(xn,nh1,tol)
cbF1(xn_1)
c1=2.
while (sqrt(sum((xn-xn_1)**2))>tol):
        if(c1%2==0 ):
            xn=Golden2d(xn_1,n1,tol)
            cbF1(xn)
            c1+=1
        else:
            xn_1=Golden2d(xn,nh1,tol)
            cbF1(xn_1)
            c1+=1 


x2=np.array([0.,0.])
px2,py2=[x2[0]],[x2[1]]
def cbF2(x):
    global px2,py2
    px2.append(x[0])
    py2.append(x[1])

n2=gradf(x2)/sqrt(sum(gradf(x2)**2))
nh2=np.array([-n2[1],n2[0]])
xn=Golden2d(x2,n2,tol)
cbF2(xn)
xn_1=Golden2d(xn,nh2,tol)
cbF2(xn_1)
c2=2.
while (sqrt(sum((xn-xn_1)**2))>tol):
        if(c2%2==0 ):
            xn=Golden2d(xn_1,n2,tol)
            cbF2(xn)
            c2+=1
        else:
            xn_1=Golden2d(xn,nh2,tol)
            cbF2(xn_1)
            c2+=1 

x3=np.array([2.0,0.0])
px3,py3=[x3[0]],[x3[1]]
def cbF3(x):
    global px3,py3
    px3.append(x[0])
    py3.append(x[1])
    
n3=gradf(x3)/sqrt(sum(gradf(x3)**2))
nh3=np.array([-n3[1],n3[0]])
xn=Golden2d(x3,n3,tol)
cbF3(xn)
xn_1=Golden2d(xn,nh3,tol)
cbF3(xn_1)
c3=2.
while (sqrt(sum((xn-xn_1)**2))>tol):
        if(c3%2==0 ):
            xn=Golden2d(xn_1,n3,tol)
            cbF3(xn)
            c3+=1
        else:
            xn_1=Golden2d(xn,nh3,tol)
            cbF3(xn_1)
            c3+=1 

plt.figure(figsize=(10,8)),plt.contourf(X,Y,E,lev1),plt.colorbar(),plt.axis('equal'),plt.title('Steepest Descent method'),\
            plt.plot(px1,py1,'ro-',label='(-1,1)'),\
            plt.plot(px2,py2,'*-',label='(0,0)'),\
            plt.plot(px3,py3,'d-',label='(2,0)'),plt.legend(),plt.savefig('hw6-1(b).png')
            
       
#c1=14, c2=18,c3=9
 #%%
#(3) Powell method


x1=np.array([-1,1.])
px1,py1=[x1[0]],[x1[1]]
def cbF1(x):
    global px1,py1
    px1.append(x[0])
    py1.append(x[1])

res1=minimize(f,x1,method='Powell',options={'xtol':tol, 'disp':True},callback=cbF1)
 


x2=np.array([0.,0.])
px2,py2=[x2[0]],[x2[1]]
def cbF2(x):
    global px2,py2
    px2.append(x[0])
    py2.append(x[1])

res2=minimize(f,x2,method='Powell',options={'xtol':tol, 'disp':True},callback=cbF2)


x3=np.array([2.0,0.0])
px3,py3=[x3[0]],[x3[1]]
def cbF3(x):
    global px3,py3
    px3.append(x[0])
    py3.append(x[1]) 
res3=minimize(f,x1,method='Powell',options={'xtol':tol, 'disp':True},callback=cbF3)

    
#iteration : all 4times
#px1[4],py1[4]    =(1.0000000022371405, 1.5000000024069642)
#px3[4],py2[4]    = (1.0000000022371405, 1.5000000011088985)
#px3[4],py3[4] =(1.0000000022371405, 1.5000000024069642)

plt.figure(figsize=(10,8)),plt.contourf(X,Y,E,lev1),plt.colorbar(),plt.axis('equal'),plt.title('Powell method'),\
            plt.plot(px1,py1,'ro-',label='(-1,1)'),\
            plt.plot(px2,py2,'*-',label='(0,0)'),\
            plt.plot(px3,py3,'d-',label='(2,0)'),plt.legend(),plt.savefig('hw6-1(c).png')
            
          
#%%
#(4) conjugate method
 

x1=np.array([-1,1.])
px1,py1=[x1[0]],[x1[1]]
def cbF1(x):
    global px1,py1
    px1.append(x[0])
    py1.append(x[1])
res1=minimize(f,x1,method='CG', options={'xtol':1.e-6,'disp':True},callback=cbF1)



x2=np.array([0.,0.])
px2,py2=[x2[0]],[x2[1]]
def cbF2(x):
    global px2,py2
    px2.append(x[0])
    py2.append(x[1])
res2=minimize(f,x2,method='CG', options={'xtol':tol,'disp':True},callback=cbF2)

x3=np.array([2.0,0.0])
px3,py3=[x3[0]],[x3[1]]
def cbF3(x):
    global px3,py3
    px3.append(x[0])
    py3.append(x[1])
res3=minimize(f,x2,method='CG', options={'xtol':tol,'disp':True},callback=cbF3)

plt.figure(figsize=(10,8)),plt.contourf(X,Y,E,lev1),plt.colorbar(),plt.axis('equal'),plt.title('CG method'),\
            plt.plot(px1,py1,'ro-',label='(-1,1)'),\
            plt.plot(px2,py2,'*-',label='(0,0)'),\
            plt.plot(px3,py3,'d-',label='(2,0)'),plt.legend(),plt.savefig('hw6-1(d).png')
            
#x1:5번,array([ 0.99999994,  1.49999992]),/ x2:12번,array([ 0.99999706,  1.49999332])/ x3:12번, array([ 0.99999706,  1.49999332])

