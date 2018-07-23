# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 04:27:08 2017

@author: Canopus
"""

import numpy as np
from numpy import *
import matplotlib.pyplot as plt

x=np.array([-2.1,-1.45,-1.3,-0.2,0.1,0.15,0.8,1.1,1.5,2.8,3.8])
y=np.array([0.012155,0.122151,0.184520,0.960789,0.990050,0.977751,0.527292,0.298197,0.105399,3.936690e-4,5.355348e-7])


from scipy.interpolate import inter1d
f1=interp1d(x,y)
f10=interp1d(x,y,kind=10)


x1=np.array([3.2,0.4,-0.128,-2.0])
n=np.arange(-1.9,3.8,0.1)
y1=f1(x1)
y10=f10(x1)


#(a) linear polation
plt.plot(x,y,'ro'),plt.plot(x,f1(x),'k--',x1,f1(x1),'bD'),plt.savefig('Hw3-3-(a)-1.png')
# x=(3.2) -> y=2.36415614e-04
# x=(0.4) -> y=8.04497538e-01
# x=(-0.128) -> y=9.67811640e-01
# x=(-2.0) -> y=2.90774615e-02



#(b) 10th order polation
plt.plot(x,y,'ro'),plt.plot(n,f10(n),'b--',x1,y10,'bD'),plt.savefig('Hw3-3-(b)-2.png')
# x=(3.2) -> y=1.09718507
# x=(0.4) -> y=0.85256479
# x=(-0.128) -> y=0.98389252
# x=(-2.0) -> y=-0.04753688


#(c)
from scipy import interpolate
result=interpolate.CubicSpline(x,y,bc_type='not-a-knot')
plt.plot(n,result(n),'y'),plt.plot(x,y,'ro'),plt.plot(x1,result(x1),'bD'),plt.savefig('Hw3-3-(c).png')
y_cubic=result(x1)
# x=(3.2) -> y=0.02091338
# x=(0.4) -> y=0.8508707
# x=(-0.128) -> y=0.98271128
# x=(-2.0) -> y=0.02681691

