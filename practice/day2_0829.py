import sys
import math

print("hello world")
print("python version: %s"%(sys.version))

a = 3
b = 2
c = 2.3


print("type of %s: %s"%(a, type(a)))
print("type of %s: %s"%('a', type('a')))

print("int(3.3) = %s"%(int(3.3)))
print("bool(%s) = %s"%(a, bool(a)))

print("sin %s = %s"%(a, math.sin(a)))
print("%s ** %s = %s"%(a, b, a**b))

def add(a, b):
    return a + b

print("add(%s, %s) = %s"%(a, b, add(a, b)))