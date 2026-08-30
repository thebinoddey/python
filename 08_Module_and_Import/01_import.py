'''What is a Module?
Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.

Create a Module
To create a module just save the code you want in a file with the file extension .py'''

#Some general modules:
'''math - This module provides access to the mathematical functions defined by the C standard.
random - This module implements pseudo-random number generators for various distributions.
datetime - This module supplies classes for manipulating dates and times.
os - This module provides a portable way of using operating system dependent functionality.'''


import math

x = math.sqrt(64)
print(x)

#-------------------

from math import pi, sqrt
x = sqrt(64)
print(x)
print(pi)

#-------------------