# NumPy --> Numerical Python
import numpy

a = numpy.array([21,41,512,76,2,567,32,1])
print(a*5/4) # i can do whatever i want to every element of an array.

# ufunc
numpy.subtract(a,1) # equals (a-1)
numpy.add(a,4) # equals (a+4)
numpy.power(a,3) # equals (a**3)
numpy.mod(a,2) # equals (a%2)
numpy.absolute(a) # absolute value function
numpy.sin(90) # sinus function
numpy.tan(45) # tangent function
numpy.log(a) # logarithm function
numpy.log2(a) # logarithm function with base modification

# solving an equation with two variables
# 5x + y = 12
# x - 3y = 7

coefficients = numpy.array([[5,1], [1,-3]])
results = numpy.array([12,7])

b = numpy.linalg.solve(coefficients,results)
print(b) # outputs x and y, respectively.
