#!/usr/bin/pyhon
# -*- coding:utf-8 -*-
def average(*args):
	sum = 0;
	for item in args:
		sum += item
	return sum / len(args)
print(average(1,2))
print(average(1,2,3,4))
