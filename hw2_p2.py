

#Hw2-2. 
from numpy import *
import numpy as np
import matplotlib.pyplot as plt

p=(sqrt(5)-1)/2

n=np.arange(0,51)
pn1=np.ones(51)
pn2=np.ones(51)
pn2[1]=p

for i in range(1,51):
    pn1[i]=p*pn1[i-1]

for i in range(2,51):
    pn2[i]=pn2[i-2]-pn2[i-1]


plt.semilogy(n,pn1,'-',label='Equation (1)')
plt.semilogy(n,pn2,'-',label='Equation (2)')
plt.xlabel('n')
plt.legend(loc=1)
plt.savefig("hw2_p2.jpg")
plt.show()
