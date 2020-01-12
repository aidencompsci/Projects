from Projects.util._decoration_base import *

def overload(func):
	Overload(func)
	def wrapper(*args, **kwargs):
		Overload.call_func(func, args, kwargs)
	return wrapper

def constructor(func):
	def wrapper(self, *args):
		funcall(self.const, *args)
	return wrapper
