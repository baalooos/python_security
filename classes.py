#!/usr/bin/env python
# -*- coding: utf-8 -*-

class MyClass(object):
	def __init__(self, msg, integer):
		self.msg = msg
		self.integer = integer
		print self.msg
		print self.integer
		return

class MyOtherClass(MyClass):
	b = 2

class CustomError(Exception):
	def __init__(self, error):
		super(CustomError, self).__init__(error)
		self.errormessage = error
		print error
	
	#def __str__(self):
	#	return "Error: %s" % self.msg

MyclassExample = MyClass('toto', 'titi')

print MyclassExample.msg
		
SentinelBool = True
if SentinelBool:
	raise CustomError("Uhoh") 
