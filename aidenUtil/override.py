from aidenUtil._decoration_base import *

# not sure if there is a different way to do this
# but this is how I thought of it

def override(func):
	Override(func)
	def wrapper(*args, **kwargs):
		Override.call_func(func, args, kwargs)
	return wrapper
