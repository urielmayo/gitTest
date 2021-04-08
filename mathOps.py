def sum(x, y):
	return x+y

def sub(x, y):
	return x-y

def prod(x,y):
	return x*y

def div(x,y):
	return x/y

def calculate(x1,x2,operation):
	if operation == '+':
		return True, sum(x1, x2)
	elif operation == '-':
		return True, sub(x1,x2)
	elif operation == 'x':
		return True, prod(x1,x2)
	elif operation == '/':
		return True, div(x1,x2)
	else:
		return False