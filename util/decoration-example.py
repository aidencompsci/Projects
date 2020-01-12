from aidenUtil.constructor import constructor
from aidenUtil.override import override

#--------------------------------------------------------------------#
# Name the constructors for the class 'const' and
# make sure to have data type suggestions/hints
# on the variables.
#--------------------------------------------------------------------#

class Test():

	@override
	def const(self, age: int, name: str):
		self.age = age
		self.name = name
		print("Age:", age, ". Name:", name, ".")

	@override
	def const(self, gender: str, height: int):
		self.height = height
		self.gender = gender
		print("Height:", height, ". Gender:", gender, ".")

	@constructor
	def __init__(self, *args):
		pass

test = Test("male", 72)
test2 = Test(15, "John")

#--------------------------------------------------------------------#
# Type hints again, or not. If you override name A I think to make
# a regular function you will have to have an override on the default
# of name A as well. I will have more on that later I think.
#--------------------------------------------------------------------#

@override
def test(var: str):
	print("string!")

@override
def test(var: int):
	print("integers!")

@override
def test():
	print("default")

test()
