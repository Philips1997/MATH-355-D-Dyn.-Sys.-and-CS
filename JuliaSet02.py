#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 13:26:55 2017

@author: xiaomengwang
"""

# this python program uses our complex numbers class to
# draw a filled Julia set for the function Z^2+C
# where Z and C are complex numbers.

# I have outlined the program here: you need to understand and fill in the
# neccesary code to complete the program:   note that there IS a fair amount of
# actual program code intact!

# NOTE: for this assignment I will allow ALL variables values to be built-in
# (assigned) in the program; don't bother with user input unless you want to


## Import math, Zelle's graphics package, and your complex
## numbers class file!

# Make a complex number MyC = -0.125 + 0.75i
# Set the maximum number of iterations allowed per point in the plane
#           to say, 30  (call this "MaxIts"?)
# Set the "escape radius" to 2.   (it was 10 in your complex-orbits program)

from DefinitionsFilesforComplexNumbersClass import *
from math import *
from graphics import *
import numpy as np

NextZ=ComplexNumbersClass(0,0)    # you may need two more variables...
CurrentZ=ComplexNumbersClass(0,0) # so create them once here
MyC = ComplexNumbersClass(-0.125, 0.75)

print("Julia set for Z^2 + C, with C equaling ", end="")
MyC.PrettyPrint()

# Window set-up:
WinSize = 200   # while working on the program, go for a small window
MyWin = GraphWin("Julia Set", WinSize, WinSize)

#  use variables (they are "good old floating point reals") named
#            LeftReal, RightReal, TopImag, and BotImag
#  in "MyWin.setCoords" below
#  to represent the region in the complex plane [-2, 2] x [-2, 2]
#            (technically, [-2, 2i] x [-2, 2i])

LeftReal = -2
RightReal = 2
TopImag = 2
BotImag = -2
Radius = 2

MyWin.setCoords(LeftReal, BotImag, RightReal, TopImag)  ## use the variables LeftReal, etc, above
MyWin.setBackground("white")

# the following variables control the step sizes for moving from point-to-point
# throughout the window in increments of a pixel:
deltaREAL = (RightReal - LeftReal) / WinSize   # horizontal step size
deltaIMAG = (TopImag - BotImag) / WinSize      # vertical step size


# At each point "CurrentZ" in the window, you need to calculate the orbit
# of CurrentZ until it either passes the "escape-to-infinity test" or
# hasn't passed this test after "MaxIts" iterates have been computed
# 
# there will be three nested while-loops for doing all this
# 1) control the REAL part of CurrentZ:  make it move from LeftReal to RightReal
#     2) control the IMAG part of CurrentZ:  it goes from BotImag to Top Imag
#         3) Calculate the orbit of CurrentZ

Tolerance = 0.0000001
MaxIts = 50
RealPart = LeftReal # initialize "RealPart" to ???????
while RealPart < RightReal:
    ImagPart = BotImag #   initialize "ImagPart" to ?????
    while ImagPart < TopImag:
        CurrentZ = ComplexNumbersClass(RealPart, ImagPart)# set CurrentZ to RealPart+ImagPart*i
        iterate = 0 # initialize "iterate" to 0 for EACH orbit!
        CurrentZReal = []
        CurrentZImag = []
        while iterate < MaxIts and CurrentZ.Modulus() < Radius: # TWO conditions!  involving the # of iterates & modulus of CurrentZ
            iterate += 1 # increment "iterate" appropriately
            NextZ.ProdOf(CurrentZ, CurrentZ) # set NextZ to the product  "CurrentZ * CurrentZ"
            NextZ.Add(MyC) # add MyC to NextZ.  Thus, NextZ = CurrentZ^2 + MyC
            CurrentZ.Copy(NextZ)  # in prep for next pass through loop
            CurrentZReal.append(CurrentZ.Re)
            CurrentZImag.append(CurrentZ.Im)
        # now the orbit calculation is done: either orbit of "CurrentZ" escaped
        # within "MaxIts" iterates or it didn't;  color the pixel at CurrentZ if it DIDN'T 
        if iterate == MaxIts: 
            for i in range(0, len(CurrentZReal)):
                CurrentZRealNo = CurrentZReal[i]
                CurrentZImagNo = CurrentZImag[i]
                SearchImagList = list(CurrentZImag[(i+1):])
                for j in range(0, len(SearchRealList)):
                    SearchReal = SearchRealList[j]
                    if (abs(CurrentZRealNo - SearchRealList[j]) <= Tolerance) and (abs(CurrentZImagNo - SearchImagList[j]) <= Tolerance):
                        RealIndex = CurrentZReal.index(SearchReal)
                        break
                ColorGradIn = (RealIndex / MaxIts) * 255
                ColorGradIn = int(round(ColorGradIn, 0))
                FatDot = Circle( Point( RealPart, ImagPart), deltaREAL)
                MyColor = color_rgb(255 - ColorGradIn, ColorGradIn, ColorGradIn)
                FatDot.setFill(MyColor)
                FatDot.setWidth(0)
                #FatDot.setOutline("red")
                FatDot.draw(MyWin)
        else:
           FatDot = Circle( Point (RealPart, ImagPart),deltaREAL)
           ColorGrad = (iterate / MaxIts) * 255
           ColorGrad = int(round(ColorGrad, 0))
           MyColorOut = color_rgb(255-ColorGrad, 255-ColorGrad, 255-ColorGrad)
           FatDot.setFill(MyColorOut)
           FatDot.setWidth(0)
           FatDot.draw(MyWin)
        # the next line prepares for the next pass through the middle while loop
        # moving CurrentZ up by a pixel:
        ImagPart += deltaIMAG
    # YOU need to add the corresponding code that moves CurrentZ to the right by
    # a pixel....
    # ...RIGHT HERE!
    RealPart += deltaREAL     
    

MyWin.getMouse()   # pause again
MyWin.close()


