#!/usr/bin/env python
# -*- coding: utf-8 -*-

#lambda
a = lambda x: x + 1
print a(2) #3
print a(3) #4

def lambdaconstruct(increaseval):
	return lambda x: x + increaseval

a = lambdaconstruct(1)
b = lambdaconstruct(2)
c = lambdaconstruct(3)

print a(1) #2
print b(1) #3
print c(1) #4

print a
print dir(a)

#take command line arguments
import sys

for i in sys.argv:
	print i
	
