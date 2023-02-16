# NumPy --> Numerical Python
import numpy

def nl(): # ignore this
    print("\n")

a = numpy.array([1,2,3,4]) # .array method creates a numpy array
b = numpy.array([5,6,7,8])

print(a*b) # outputs [5,12,21,32]
nl()

print(type(a)) # outputs 'ndarray'
nl()
# The Numpy array object in Numpy is called ndarray.

#------------------------------------------------------------------------------------
# a = [1,2,3,4]
# b = [5,6,7,8]
# ab = []

# for i in range(0 ,len(a)):
#     ab.append(a[i] * b[i])
   
# print(ab)

# This code snippet does the same job but NumPy makes it much easier as you can see.
# It also reduces the space complexity of algorithms.
#------------------------------------------------------------------------------------

print(numpy.zeros(10, dtype=int)) # dtype --> data type
# outputs [0,0,0,0,0,0,0,0,0,0]
nl()

print(numpy.ones(3, dtype=int))
# outputs [1,1,1]
nl()

print(numpy.full((3,5), 9))
# outputs
# [9,9,9,9,9
#  9,9,9,9,9
#  9,9,9,9,9]
nl()

print(numpy.arange(0, 21, 4))
# outputs [0,4,8,12,16,20]
nl()

c = numpy.random.randint(5, size=(2,4))
# generates a 2x4 array of ints between 0 and 4, inclusive
print(c)
print(c.ndim) # .ndim method returns the number of dimensions of an array
print(c.shape) # .shape method returns the dimensions of an array
print(c.size) # .size method returns the number of elements of an array
print(c.dtype) # .dtype method returns the data type of an array
nl()

d = numpy.arange(1,10).reshape(3,3)
# d = [1,2,3
#      4,5,6
#      7,8,9]
print(d)
nl()

# ----CONCATENATION----
e = numpy.array([11,12,13])
f = numpy.array([4,7,2])
print(numpy.concatenate([f,e])) # outputs [4,7,2,11,12,13]
nl()

g = numpy.array([[10,20,30],
                [40,50,60]])

print(numpy.concatenate([g,g], axis=0))
# outputs [[10,20,30]
#          [40,50,60]
#          [10,20,30]
#          [40,50,60]]
nl()

print(numpy.concatenate([g,g], axis=1))
# outputs [[10,20,30,10,20,30]
#          [40,50,60,40,50,60]]
nl()

# ----SPLITTING----
h = numpy.array([1,2,3,99,99,3,2,1])
i,j,k = numpy.split(h, [3,5]) # here 3 and 5 are indexes
print(i) # outputs [1,2,3]
print(j) # outputs [99,99]
print(k) # outputs [3,2,1]
nl()

l = numpy.arange(16).reshape(4,4)
# l = [[0,1,2,3]
#      [4,5,6,7]
#      [8,9,10,11]
#      [12,13,14,15]]
up,down = numpy.vsplit(l, [2]) # vertical splitting (row-wise)

print(up) # outputs [[0 1 2 3]
#                    [4 5 6 7]]

print(down) # outputs [[ 8  9 10 11]
#                      [12 13 14 15]]
nl()

left,right = numpy.hsplit(l, [2]) # horizontal splitting (column-wise)

print(left) # outputs [[0,1]
#                      [4,5]
#                      [8,9]
#                      [12,13]]

print(right) # outputs [[2,3]
#                       [6,7]
#                       [10,11]
#                       [14,15]]
nl()

# ----SORTING----
m = numpy.array([43,1,532,32,865,4,2,62])
print(numpy.sort(m)) # outputs the sorted array
print(m) # outputs the actual array, numpy doesn't change the actual array, it just sorts.
nl()