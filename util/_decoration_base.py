
#should overload this one too haha
def funcall(func, *args, **kwargs):
	func(*args, **kwargs)

def is_class_instance(var):
	type_list = [
		"function",
		"int",
		"float",
		"dict",
		"str",
		"list",
		"tuple",
		#add type?
	]
	return not (True in [(t in str(var.__dir__)) for t in type_list])

def type_list_from_arg_list(type_args):
	return [str(type(i)) for i in type_args]

def type_list_from_arg_dict(type_args):
	return [v for k,v in type_args.items()]

def unpack_func_data(func):
	name = str(func.__name__)
	class_fun = str(func).split(" ")[1].split(".")
	class_name = class_fun[0] if len(class_fun) > 1 else "none"
	args = func.__annotations__
	return name, class_name, args

def unpack_args(args):
	obj = args[0]
	instance = obj[0]

	new_args = []
	type_args = []
	if is_class_instance(instance): rest = obj[1:]; new_args.append(instance); new_args.append(rest); type_args = rest
	else: new_args.append(obj); type_args = obj

	types = type_list_from_arg_list(type_args)
	strtypes = str(types).replace("\"", "")

	#look at the quote marks, I feel like there should be a better way to handle arg lists to string?

	return new_args, types, strtypes

class Overload():

	functions = {}

	def __init__(self, func):
		def else_make_key(d, key, val):
			try: d[key]
			except: d[key] = val

		name, class_name, args = unpack_func_data(func)

		else_make_key(Overload.functions, class_name, {})
		else_make_key(Overload.functions[class_name], name, [])

		temp = {}
		temp[str(type_list_from_arg_dict(args))] = func
		Overload.functions[class_name][name].append(temp)

	@staticmethod
	def call_func(passed_function, *args, **kwargs):
		def key_exists(d,key):
			try: return d[key]
			except: return False

		name, class_name, fargs = unpack_func_data(passed_function)
		if not args[0] is (): new_args, types, strtypes = unpack_args(args)
		else: new_args, types, strtypes = [],[],'[]'

		function_list = key_exists(Overload.functions[class_name], name)
		for i in function_list:
			func = key_exists(i, strtypes)
			if func:
				funcall(func, *args[0], **kwargs)