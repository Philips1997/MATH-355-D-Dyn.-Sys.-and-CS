#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 13:11:23 2017

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

NextZ=ComplexNumbersClass(0,0)    # you may need two more variables...
CurrentZ=ComplexNumbersClass(0,0) # so create them once here
MyC = ComplexNumbersClass(0.285, 0.535)

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

Refpt = ComplexNumbersClass(0, 0)
RefptCurrent = ComplexNumbersClass(0, 0)
for RefIte in range (0, 1000):
    RefptCurrent.ProdOf(Refpt, Refpt)
    RefptCurrent.Add(MyC)
    Refpt.Copy(RefptCurrent)
MaxIts = 50
RealPart = LeftReal # initialize "RealPart" to ???????

Tolerance = 0.00001
while RealPart < RightReal:
    ImagPart = BotImag #   initialize "ImagPart" to ?????
    while ImagPart < TopImag:
        CurrentZRealList = []
        CurrentZImagList = []
        CurrentZ = ComplexNumbersClass(RealPart, ImagPart)# set CurrentZ to RealPart+ImagPart*i
        iterate = 0 # initialize "iterate" to 0 for EACH orbit!
        while iterate < MaxIts and CurrentZ.Modulus() < Radius: # TWO conditions!  involving the # of iterates & modulus of CurrentZ
            iterate += 1 # increment "iterate" appropriately
            NextZ.ProdOf(CurrentZ, CurrentZ) # set NextZ to the product  "CurrentZ * CurrentZ"
            NextZ.Add(MyC) # add MyC to NextZ.  Thus, NextZ = CurrentZ^2 + MyC
            CurrentZ.Copy(NextZ)  # in prep for next pass through loop
            CurrentZRealList.append(CurrentZ.Re)
            CurrentZImagList.append(CurrentZ.Im)
        # now the orbit calculation is done: either orbit of "CurrentZ" escaped
        # within "MaxIts" iterates or it didn't;  color the pixel at CurrentZ if it DIDN'T 
        if iterate == MaxIts:
            for ExamThrough in range (0, len(CurrentZRealList)):
                DiffZ = ComplexNumbersClass(0, 0)
                CurrentZZ = ComplexNumbersClass(CurrentZRealList[ExamThrough], CurrentZImagList[ExamThrough])
                DiffZ.DifferenceOf(CurrentZZ, Refpt)
                DiffZMod = DiffZ.Modulus()
                if DiffZMod < Tolerance:
                    ExIte = ExamThrough
                    print(ExIte)
                    break
                else:
                    ExIte = ExamThrough
            FatDot = Circle( Point( RealPart, ImagPart), deltaREAL)
            MyColorGrad = (ExIte/MaxIts) * 255
            MyColorGradin = int(round(MyColorGrad, 0))
            MyColor = color_rgb(MyColorGradin, 128, 0)
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


