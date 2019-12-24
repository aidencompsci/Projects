from aidenUtil._decoration_base import *

def constructor(func):
	def wrapper(self, *args):
		# honestly, I forgot this call was in here.
		# I forgot what it does and if I need it...
		# That will be fixed in a few minutes hopefully
		func(self, *args)
		funcall(self.const, *args)
	return wrapper
