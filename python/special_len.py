#!/usr/bin/python
class Fib(object):
	def __init__(self,num):
		self.num = num
	def __len__(self):
		return self.num
	def __str__(self):
		a = self.num
		fib = [0,1]
		while a - 2 > 0:
			fib.append(int(fib[-1])+int(fib[-2]))
			a = a - 1
		return str(fib)
	__repr__  = __str__

f = Fib(10)
print (f)
print (len(f))
