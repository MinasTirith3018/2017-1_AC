e=1.0
n=0
while((1.0+0.5*e)!=1.0):
#if computer cognizes sum of 1 and 0.5*e as 1.0, it stops the loop. The reason inserting 0.5*e is that if just '1.0+e' is set in while condition, loop is stop when e is less than machine epsilon.
    e=e/2
    n=n+1
    
print n
print"{:.40e}".format(e)



    
