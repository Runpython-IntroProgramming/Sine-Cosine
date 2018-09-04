"""
sinecosine.py
Author: Noah Pikielny
Credit: http://www.december.com/html/spec/color4.html - for hexadecimal colors

Assignment:

In this assignment you must use *list comprehensions* to generate sprites that show the behavior
of certain mathematical functions: sine and cosine. 

The sine and cosine functions are provided in the Python math library. These functions are used
to relate *angles* to *rectangular* (x,y) coordinate systems and can be very useful in computer
game design.

Unlike the last assignment using ggame`, this one will not provide any "skeleton" code to fill
in. You should use your submission for the Picture assignment 
(https://github.com/HHS-IntroProgramming/Picture) as a reference for starting this assignment. 

See:
https://github.com/HHS-IntroProgramming/Sine-Cosine/blob/master/README.md
for a detailed list of requirements for this assignment.

https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Programmed-Graphics
for general information on using list comprehensions to generate graphics.

http://brythonserver.github.io/ggame/
for detailed information on ggame.
"""
from ggame import CircleAsset, App, Color, LineStyle, Sprite
from math import sin, cos, radians
i = 0
xVal = []

blue = Color(0x0000ff, 1.0)
red = Color(0xff0000, 1.0)
purple = Color(0x7D26CD, 1.0)
blueLine = LineStyle(1, blue)
redLine = LineStyle(1, red)
purpleLine = LineStyle(1, purple)

while i <= 360:
    xVal.append(i)
    i += 10

for k in xVal:
    circleB = CircleAsset(5, redLine, blue)
    circleR = CircleAsset(5, purpleLine, red)
    circleP = CircleAsset(5, blueLine, purple)
    Sprite(circleB, (k, 100 + 100 * sin(radians(k))))
    Sprite(circleR, (k, 100 + 100 * cos(radians(k))))
    Sprite(circleP, (100+100*cos(radians(k)), 400+100*sin(radians(k))))
myApp = App()
myApp.run()