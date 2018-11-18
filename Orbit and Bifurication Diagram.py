# draw orbit and bifurication diagram
# bifurication diagram: horizontal axis: C value; verical axis: fixed point's x value
# orbit diagram: horizontal axis: C value; vertical axis: long term behavior of 0 (critical point)

from math import *
from graphics import *

cLeft = -0.1 #set the range of window to draw
cRight = 0.1

xLeft = -9
xRight = 9

print("In this program, you have 3 options:")
print("1. Draw the bifurication diagram")
print("2. Draw the orbit diagram")
print("3. Draw both")
YourChoice =  int(input("Enter your option: ")) # let the user to choose the tasks

windowsize = 501 # basic parameters of window
deltaC = (cRight - cLeft)/(windowsize-1)

HiddenIts = 0   # hide the first n iterations
DisplayIts = 40  # display m iterates afterwards


MyWin =  GraphWin ("Orbit and Bifurication Diagram", windowsize, windowsize)
MyWin.setCoords(cLeft, xLeft, cRight, xRight)
CAxis = Line(Point(cLeft, 0), Point(cRight, 0))
CAxis.setWidth(2)
CAxis.draw(MyWin)
XAxis = Line(Point(0, xLeft), Point(0, xRight))
XAxis.setWidth(2)
XAxis.draw(MyWin)  # draw the horizontal and vertical axis

GridCountxP = 0 # set the initial value for grid lines
GridCountxN = 0
GridCountcP = 0
GridCountcN = 0

# draw the grid lines: 
while GridCountxP <= xRight:
    xGridLP = Line(Point(cLeft, GridCountxP), Point(cRight, GridCountxP))
    xGridLP.setWidth(1)
    xGridLP.draw(MyWin)
    GridCountxP += 0.5

while GridCountxN >= xLeft:
    xGridLP = Line(Point(cLeft, GridCountxN), Point(cRight, GridCountxN))
    xGridLP.setWidth(1)
    xGridLP.draw(MyWin)
    GridCountxN = GridCountxN - 0.5

while GridCountcP <= cRight:
    xGridLP = Line(Point(GridCountcP, xLeft), Point(GridCountcP, xRight))
    xGridLP.setWidth(1)
    xGridLP.draw(MyWin)
    GridCountcP += 0.5

while GridCountcN >= cLeft:
    xGridLP = Line(Point(GridCountcN, xLeft), Point(GridCountcN, xRight))
    xGridLP.setWidth(1)
    xGridLP.draw(MyWin)
    GridCountcN = GridCountcN - 0.5

def FuncN(x, iterationnumber, constant): # define the (f^n)(x)
    for FuncNi in range (1, iterationnumber+1):
        x = (((x * 0.5) + constant) ** 2) + 8
        #x = constant * x * (1 - x)
    return x

OrbIte = int(input("Enter the number of iterations you would like: "))
if YourChoice == 1 or YourChoice == 3: # draw the bifurication diagram
    deltaX = deltaC
    MyC = cLeft
    while MyC <= cRight:    
        subxL =  xLeft
        while subxL <= xRight:
            yLeft = FuncN(subxL, OrbIte, MyC)
            subxR = subxL + deltaX
            yRight = FuncN(subxR, OrbIte, MyC)
            if ((yLeft - subxL)*(yRight - subxR) <= 0):
                bPoint = Point(MyC, subxL)
                subxLS = (yRight - yLeft)/deltaX
                if (subxLS > 1) or (subxLS < -1):
                    bCircle = Circle (bPoint, deltaC)
                    bCircle.setFill("red")
                else:
                    bCircle = Circle (bPoint, deltaC)
                    bCircle.setFill("green")
                bCircle.setWidth(0)
                bCircle.draw(MyWin)
            subxL = subxR
        MyC += deltaC

if YourChoice == 2 or YourChoice == 3: # draw the orbit diagram
    MyC = cLeft
    while MyC <= cRight:
        MyOrb = 0
        for i in range (1, HiddenIts + DisplayIts +1):
            MyOrb = MyOrb * MyOrb + MyC
            if (i >= HiddenIts+1) and (MyOrb < 1000):
                oPoint = Point(MyC, MyOrb)
                oPoint.setFill("blue")
                oPoint.draw(MyWin)
        MyC += deltaC

print("press 'q' to quit, any other key to continue reading mouse clicks ")
stopkey= MyWin.getKey()
while stopkey != "q":
    print("Click on the graph!")
    print(MyWin.getMouse() )  # return cursor position on mouse click
    print("press 'q' to quit, any other key to continue ")
    stopkey= MyWin.getKey()
  
MyWin.getMouse() # close the window when click on mouse
MyWin.close()
