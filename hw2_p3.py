#HW2 no.3

def f(j):
	j=float(j)
	y=1/(j*(j+1))
	return y


#(1) By Summing terms from largest terms first to the smallest terms last
print "#(1) By Summing terms from largest terms first to the smallest terms last"
n0=[2,4,6]

for k in n0:
	n=10**k
	Sn=0.
	for x in range(1,n+1):
		Sn=Sn+f(x)
	print "n={:.1e} Sum={:.16f}".format(n, Sn)
	
print "\n"



#(2) By Summing terms from smallest terms first to the largest terms last
print "#(2) By Summing terms from smallest terms first to the largest terms last"

n0=[2,4,6]
for k in n0:
	n=10**k
	Sn=0.
	for x in range(n,0,-1):
		Sn=Sn+f(x)
	print "n={:.1e} Sum={:.16f}".format(n, Sn)

print "\n"



#(3) Kahan Summation Formula
print "#(3) Kahan Summation Formula"

n0=[2,4,6]
for k in n0:
	n=10**k
	Sn=f(1) #setting first Sum,S1
	ci=0.   #setting C1
	for i in range(2,n+1):
		xi=f(i)-ci	#setting new xi 	
		ci=((Sn+xi)-Sn)-xi #calculating next Ci
		Sn=Sn+xi	#Adding new xi in sum
	print "n={:.1e} Sum={:.16f}".format(n, Sn)	
