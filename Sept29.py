#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 23:20:21 2017

@author: Xiaomeng Wang
"""

# Determine the ratio between following orbit terms
import math as mt

# input the C value for y=x^2+C
C = input('Please input the y-intersect: ')
C = float(C)

def f(x):
    return x**2+C

p1 = (1-mt.sqrt(1-(4*C)))*0.5
p2 = (1+mt.sqrt(1-(4*C)))*0.5

if abs(2*p1) < 1: #determine which fixed point is attracting fixed point
    p = p1
elif abs(2*p2) < 1:
    p = p2
else:
    p = 0 #if none is fixed, random choose a fixed point as 0

#input the distance between the starting point and fixed point p
d = input('Please input the distance between x and p: ')
d = float(d)
x = d+p
a = abs(x-p)

# input the number of interations for the orbit
It = int(input('Please input the number of iterations desired: '))

print('Iterate', 'Iterated Value', '       ', 'Distance', '       ', 'Ratio')
print(0, "%20.16f"%(x), "%20.16f"%(a), sep = ' ')

for i in range(1, It+1):
    fx = f(x)
    fa = abs(fx-p)
    k = fa/abs(x-p)
    print(i, "%20.16f"%(fx), "%20.16f"%(fa), "%20.16f"%(k), sep = ' ')
    x = fx