#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 11:43:47 2017

@author: xiaomengwang
"""

# Here is our class definition

from math import *

class ComplexNumbersClass: 
    
    def __init__(self, RealPart, ImagPart):
        self.Re = RealPart
        self.Im = ImagPart
    
    def PrettyPrint(self):
        print(self.Re, "+", self.Im, "i")
    
    def Add(self, AnotherNumber):
        self.Re = self.Re + AnotherNumber.Re
        self.Im = self.Im + AnotherNumber.Im
    
    def SumOf(self, ThisNum, ThatNum):
        self.Re = ThisNum.Re + ThatNum.Re
        self.Im = ThisNum.Im + ThatNum.Im
    
    def ProdOf(self, ThisNum, ThatNum):
        self.Re = (ThisNum.Re * ThatNum.Re) - (ThisNum.Im * ThatNum.Im)
        self.Im = (ThisNum.Re * ThatNum.Im) + (ThisNum.Im * ThatNum.Re)
    
    def DifferenceOf(self, ThisNum, ThatNum):
        self.Re = ThisNum.Re - ThatNum.Re
        self.Im = ThisNum.Im - ThatNum.Im
    
    def Modulus(self):
        return sqrt(self.Re ** 2 + self.Im ** 2)
    
    def InvOf(self, RealPart, ImagPart):
        self.Re = RealPart/((RealPart ** 2) + (ImagPart ** 2))
        self.Im = -ImagPart/((RealPart ** 2) + (ImagPart ** 2))
    
    def ArguOf(self):
        return atan2(self.Im, self.Re)
    
    def Copy(self, AnotherNumber):
        self.Re = AnotherNumber.Re
        self.Im = AnotherNumber.Im
    
    def Swap(self, AnotherNumber):
        self.Re = AnotherNumber.Im
        self.Im = AnotherNumber.Re