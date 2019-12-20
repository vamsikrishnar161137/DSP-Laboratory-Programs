#program to perform operation by using linear algebra functions  in numpy
import numpy as l
a=l.array(input('Enter a matrix'))
print 'Entered matrix is',a
print 'Determinant of given matrix is:\n ',l.linalg.det(a)
print 'Eigen vector of given matrix is:\n ',l.linalg.eig(a)
print 'Eigvauels of given matrix is:\n ',l.linalg.eigvals(a)
print 'Inverse of given matrix is:\n',l.linalg.inv(a)
print 'Rank of The given martix is:\n',l.linalg.matrix_rank(a)
n=input('Enter The power of matrix')
print 'Power of The given martix is\n',l.linalg.matrix_power(a,n)
print 'The singular values of The matrix are:',l.linalg.svd(a)
#TO create matrix by using function in numpy
print"The zero matrx :\n",l.zeros((2,3))
print"The ones matrix:\n",l.ones((1,2))
print"The idintity matrix:\n",l.eye(2,2) 
print"The random values matrix:\n",l.random.random((2,2))
#To perfom operation by using numpy in numpy
print'The sqaure of The matrix :\n',l.square(a)
print 'The meadian of dian value The matrix is\n:',l.median(a)
print 'The maximum of The matrix is\n:',l.max(a)
print 'The minimum of The matrix\n:',l.min(a)
print 'The transpose of The matrix\n:',l.transpose(a)
b=l.array(input('enter matix with same dimenssion of a for addtion and substraction'))
print 'The sum of The matrix\n:',l.add(a,b)
print 'The substract afrom b\n:',l.subtract(a,b)
print 'The multiplication of The matrix\n:',l.multiply(a,b)
print 'The element by element divsion of matrices a and b is:\n',l.divide(a,b)
