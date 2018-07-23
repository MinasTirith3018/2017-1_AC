import numpy as np
import matplotlib.pyplot as plt

hw=np.loadtxt('hw1_p4.dat')
x=hw[:,0]
a=hw[:,1]
b=hw[:,2]

file=open('hw1_p4_fourth.dat','w')

for i in range(1,len(hw)):
	if ((i+1)%4==0):
		txt=str(x[i])+'\t'+str(a[i])+'\t'+str(b[i])+'\n'
		file.write(txt)
file.close()

plt.plot(x,a*x,'k-',label='a*x')
plt.plot(x,b*x,'b:',label='b*x')
plt.plot(x,a*x*b,'r--',label='a*b*x')
plt.legend(loc=2, numpoints=1)
plt.xlabel('time')
plt.ylabel('value')

hwf=np.loadtxt('hw1_p4_fourth.dat')
print len(hwf)
print np.shape(hwf)

plt.savefig('hw1-4.pdf')

plt.show()



