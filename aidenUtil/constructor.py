from aidenUtil._decoration_base import *

def constructor(func):
	def wrapper(self, *args):
		funcall(self.const, *args)
	return wrapper
