#!/usr/bin/python
for i in range(1,10):
	for j in range(1,i+1):
		print("%sx%s=%s "%(j,i,j*i),end='')
	print()
