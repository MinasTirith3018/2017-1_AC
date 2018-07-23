#hw2-5. Kapler problem (1)

from numpy import *
import numpy as np

P=365.25365
a=1.496e+8
e=0.0167
b=a*(1-e**2)**0.5
t1=182
t2=273


def f(t,E):
    y=E-(2*pi*t/P+e*sin(E))
    return y
def x(E):
    return a*cos(E)
def y(E):
    return b*sin(E)

#Bisection
a1=pi/180*135
b1=pi/180*225

a2=pi/180*225
b2=pi/180*315

c1=(a1+b1)/2
n1=1

while((abs(b1-c1)>1e-10)):
    if(f(t1,c1)*f(t1,b1)<0):
        a1=c1
        c1=(a1+b1)/2
        n1=n1+1
      
    if(f(t1,c1)*f(t1,a1)<0):
        b1=c1
        c1=(a1+b1)/2
        n1+=1
        
        
c2=(a2+b2)/2
n2=1
while((abs(b2-c2)>1e-10)):
    if(f(t2,c2)*f(t2,b2)<0):
        a2=c2
        c2=(a2+b2)/2
        n2=n2+1
       
    if(f(t2,c2)*f(t2,a2)<0):
        b2=c2
        c2=(a2+b2)/2
        n2+=1

print "Finding E,x,y, in the bisection way" 
print "When t={}days, {}times calculations, E={:.12}rad, x={:.12e}km, y={:.12e}km".format(t1,n1,c1,x(c1),y(c1))
print "When t={}days, {}times calculations, E={:.12}rad, x={:.12e}km, y={:.12e}km".format(t2,n2,c2,x(c2),y(c2))
print"\n"



# NR-Method
def fd(E):
	y=1-e*cos(E)
	return y
a1=pi/180*135
b1=pi/180*225

a2=pi/180*225
b2=pi/180*315

x10=a1
x1n=x10-f(t1,x10)/fd(x10)
n1=1
while(abs(x10-x1n)>1e-10):
	x10=x1n
	x1n=x10-f(t1,x10)/fd(x10)
	n1+=1


x20=a2
x2n=x20-f(t2,x20)/fd(x20)
n2=1
while(abs(x20-x2n)>1e-10):
	x20=x2n
	x2n=x20-f(t2,x20)/fd(x20)
	n2+=1
	


print "Finding E,x,y, in the NR-method" 
print "When t={}days, {}times calculations, E={:.12}rad, x={:.12e}km, y={:.12e}km".format(t1,n1,x1n,x(x1n),y(x1n))
print "When t={}days, {}times calculations, E={:.12}rad, x={:.12e}km, y={:.12e}km".format(t2,n2,x2n,x(x2n),y(x2n))

print"\n"




#fixed-iteration method
def fi(t,E):
    y=2*pi*t/P+e*sin(E)
    return y

a1=pi/180*135
b1=pi/180*315

xn=fi(t1,a1)
n1=1
while(abs(fi(t1,xn)-xn)>1e-10):
	xn=fi(t1,xn)
	n1+=1
	
a2=pi/180*225
b2=pi/180*315
xm=fi(t2,a2)
n2=1
while(abs(fi(t2,xm)-xm)>1e-10):
	xm=fi(t2,xm)
	n2+=1

print "Finding E,x,y, in the Fixed-iteration-method" 
print "When t={}days, {}times calculations, E={:.12}rad, x={:.12e}km, y={:.12e}km".format(t1,n1+1,fi(t1,xn),x(fi(t1,xn)),y(fi(t1,xn)))
print "When t={}days, {}times calculations, E={:.12}rad, x={:.12e}km, y={:.12e}km".format(t2,n2+1,fi(t2,xm),x(fi(t2,xm)),y(fi(t2,xm)))

    
