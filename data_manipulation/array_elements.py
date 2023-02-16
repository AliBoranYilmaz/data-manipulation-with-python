# NumPy --> Numerical Python
import numpy

def nl(): # ignore this
    print("\n")

a = numpy.random.randint(10, size=(2,3))
print(a[0,0]) # accessing elements of a matrix
nl()

b = numpy.array([[10,20,30],
                 [40,50,60],
                 [70,80,90]])

print(b[0,:]) # first row
print(b[:,0]) # first column
print(b[:,2]) # third column
print(b[1,:]) # second row

print(b[0:2 , 0:2]) # outputs [[10,20]
#                              [40,50]]

print(b[: , 0:2]) # first two columns and all rows
nl()

c = numpy.random.randint(10, size=(5,5))
sub_c = c[0:3, 0:2] # creating a sub-array from c
sub_c[0,1] = 899 # this modification will also affect the actual array, c.

# to prevent this, 'copy' method is used.
sub_c2 = c[0:3, 0:2].copy() # now this sub-array is independent from actual array.

# ---- FANCY INDEXING ----
d = numpy.arange(1,26,3) # d = [1,4,7,10,13,16,19,22,25]
indexes = [1,3,5]
print(d[indexes]) # gets d[1], d[3] and d[5]
nl()

e = numpy.arange(9).reshape((3,3))
first = numpy.array([1,1])
second = numpy.array([0,2])
print(e[first,second]) # outputs [3,5]
nl()

# ---- CONDITIONAL OPERATORS ---- 
f = numpy.array([1,2,3,4,5,6])
print(f > 5) # outputs [False, False, False, False, False, True]
print(f[f < 5]) # outputs [1,2,3,4]
print(f[f != 3]) # outputs [1,2,4,5,6]