#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 11:38:04 2017

@author: xiaomengwang
"""

# First Python program with complex numbers

from DefinitionsFilesforComplexNumbersClass import *

MyZ = ComplexNumbersClass (3.0, 4.0)
# uses the __init__ method in the ComplexNumbersClass class
# to make the complex number 3+4i
MyZ.PrettyPrint()

CopyZ = MyZ # Make a copy of MyZ ?
print("MyZ and its copy are ")
MyZ.PrettyPrint()
CopyZ.PrettyPrint()

SafeCopyZ = ComplexNumbersClass(MyZ.Re, MyZ.Im)
# Not good, because it requires the author of this program to know how to make the complex numbers

SafeCopyOfZ = ComplexNumbersClass(0, 0)
SafeCopyOfZ.Copy(MyZ)
print("This is another safe copy of Z: ")
SafeCopyOfZ.PrettyPrint()

YourNumber = ComplexNumbersClass(10, 20)
MyZ.Add(YourNumber) # Add your number to MyZ and store in MyZ
print('Now, MyZ is: ')
MyZ.PrettyPrint()
CopyZ.PrettyPrint()
print("SafeCopyZ is ")
SafeCopyZ.PrettyPrint()

YourSum = ComplexNumbersClass(0, 0)
YourSum.SumOf(MyZ, YourNumber)
YourSum.PrettyPrint()

YourProd = ComplexNumbersClass(1, 0)
YourProd.ProdOf(MyZ, YourNumber)
YourProd.PrettyPrint()

print(MyZ.Modulus())