"""
sinecosine.py
Author: Jack Meehan
Credit: https://www.webucator.com/blog/2015/03/python-color-constants-module/ (used for colors)

Assignment:

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

from ggame import App, Sprite, Color, CircleAsset, RectangleAsset, LineStyle
from math import sin, cos, radians

red = Color(0xff0000, 1.0)
purple = Color(0x9A32CD, 1.0)
blue = Color(0x0000EE, 1.0)
black = Color(0x000000, 1.0)
line = LineStyle(2, black)
xcoordinates = range( 0, 360, 10)

bluecircle = CircleAsset(6, line, blue)
yay = [Sprite(bluecircle, (x, 100+100*sin(radians(x)))) for x in xcoordinates]

redcircle = CircleAsset(6, line, red)
yay = [Sprite(redcircle, (x, 100+100*cos(radians(x)))) for x in xcoordinates]

purplecircle = CircleAsset(6, line, purple)
yay = [Sprite(purplecircle, (100+100*cos(radians(x)), 400+100*sin(radians(x)))) for x in xcoordinates]

myapp = App()
myapp.run()
