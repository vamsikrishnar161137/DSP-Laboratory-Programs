#concatenation of the two arrays
import numpy as np
p=np.array([1,2,3])
q=np.array([2,3,4])
r=np.concatenate((p,q),axis=None)
print r
a=input("Enter the array a::")
b=input("Enter the array b::")
print "The elements in array a \n",a
d=np.append(a,b)
print "Elements of array a",d
for i in range(0,len(b)):
	if(b[i]>=0):
		a.append(b[i])
print"The resulting array is::",a
