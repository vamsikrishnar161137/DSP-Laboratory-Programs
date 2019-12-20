#SOME OF THE ARRAY OPERATIONS
import numpy as np
a=np.array([(1,4,2,6,5),(2,5,6,7,9)])#defining the array.
print '1.The predifined first array is::',a
b=np.size(a)#finding size of a array.
print '2.Size of the array is::',b
c=np.shape(a)#finding shape of an array
print '3.Shape of the array is::',c
d=np.ndim(a)
print '4.Dimension of the array is::',d
e=a.reshape(5,2)
print '5.Reshaping of an array is::\n',e
#Slicing(getting a specific digit from digit::)
f=a[0,3]
print '6.The digit is::',f
g=np.linspace(1,3,5)
print '7.The result is::',g
h=np.max(a)
print '8.Max of the array::',h
i=np.min(a)
print '9.Min of the array::',i
j=np.sum(a)#sum of the digits in a array.
print '10.The sum of the digits in the array is::',j
k=np.sqrt(a)#finding square roots of the digits in the array.
print '11.The square roots of the digits in an array is::\n',k
l=np.std(a)#finding standard deviation for digits in the array.
print '12.The standard deviation of the array::',l
#doing sum,sub,mul,div to two arraya with their respective elements.
m=np.array([(1,2,3,4,5),(4,5,6,7,8)])
n=a+m
print '13.The sum of the two arrays is::\n',n
o=a-m
print '14.The subtraction of the two arrays is::\n',o
p=a*m
print '15.The multiplication  of the two arrays is::\n',p
q=a/m
print '16.The division of the two arrays is::\n',q
#placing second array in the first array.(called as stacking processes)
r=np.vstack((a,m))#vertical stacking
print '17.The concatenation of the two arrays is::\n',r
s=np.hstack((a,m))#horizontal stacking
print '18.The concatenation of the two arrays is::\n',s
#converting all in one column
t=a.ravel()
print '19.The result is::',t
u=m.ravel()
print '20.The result is::',u
#finding data type of the array.
print '21.The data type of the array is::'
print (a.dtype)





