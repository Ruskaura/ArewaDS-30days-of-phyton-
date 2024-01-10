# 1. Check the python version you are using
import sys
print(sys.version)

# 2. Open the python interactive shell and do the following operations. The operands are 3 and 4.
print(3+4)   # addition
print(3-4)   # subtraction
print(3*4)   # multiplication
print(3/4)   # division
print(3**4)  # exponential
print(3 % 4) # modulus
print(3//4)  # floor division

# 3. write strings on the python interactive shell.
print('Musa isah')
print('yusuf')
print('Nigeria')
print('i love being with arewaDS')

# 4. Check the data types of the following data:
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh','Python','Finland']))
print(type('Musa'))
print(type('Yusuf'))
print(type('Nigeria'))

# Level 3 exercise
# Python data types
# Number: integer, float, complex
a = 7 # integer
print(type(a))

b = 7.14 # float
print(type(b))

c = 7+8j # complex
print(type(c))

# String:
d = 'Musa' # string
print(type(d))

# Boolean:
e = True # boolean
print(type(e))

# List:
f = ['pie', '89', 'Car'] #square brackets
print(type(f))

# Tuple:
g = ('north','south') #round brackets
print(type(g))

# Set:
h = {2,4,6} #curly brackets
print(type(h))

# Dictionary:
i = {'Nigeria':'Abuja', 'Kenya':'Nairobi'} 
print(type(i))

# Euclidian distance
import math
print(math.dist([2,3],[10,8]))
