#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:15:13 2017

@author: Xiaomeng Wang
"""

# Prelude to writing a program that finds all the points of period n
# For a function in some given interval

# Here we will write a program to locate the roots of y=sin(x^2)
# In an interval [xLeft, xRight]

import math as mt # Give access to common math functions

xLeft = 0.0
xRight = 5.0
deltaX = 0.01

SxL = set() #Store the LH endpoint of subintervals containing root
LxL=[]

#xLeft = float(input('Please input the left hand end of interval: '))
#xRight = float(input('Please input the right hand end of interval: '))
#deltaX = float(input('Please input the step size of test interval: '))

# while [this condition is True do the following indented statements]

subxL = xLeft # this is the LH endpoint of the first tested subinterval
while subxL < xRight: 
    subxR = subxL + deltaX
    subyL = mt.sin(subxL*subxL)
    subyR = mt.sin(subxR*subxR)
    if ((subyL <= 0) and (subyR > 0)) or ((subyL >= 0) and (subyR < 0)):
        print (" %12.8f %12.8f" %(subxL, subxR))
        SxL.add(subxL)
        LxL.append(subxL)
    subxL = subxR

print("Here is the set:")
for sxl in SxL:
    print(" %12.8f"%(sxl))
    
print("Here is the list:")
for lxl in LxL:
    print(" %12.8f"%(lxl))