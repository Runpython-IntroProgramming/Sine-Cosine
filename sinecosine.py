"""
sinecosine.py
Author: Nick Lee
Credit: Mr. D for adding two parentheses 

Assignment: Sine and cosine

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

from ggame import App, CircleAsset, RectangleAsset, Color, LineStyle, Sprite
from math import sin, cos, radians

xcoordinates = range(0, 1120, 10)

red = Color(0xff0000, 1.0)
blue = Color(0x0000ff, 1.0)
purple = Color(0xa301cd, 1.0)
black = Color(0x000000, 1.0)

thinline = LineStyle(1, black)

bluecircle = CircleAsset(7, thinline, blue)
redcircle = CircleAsset(7, thinline, red)
purplecircle = CircleAsset(7, thinline, purple)

reds = [Sprite (redcircle, (x, 100+100*cos(radians(x))))for x in xcoordinates]
blues = [Sprite (bluecircle, (x, 100+100*sin(radians(x))))for x in xcoordinates]
purples = [Sprite (purplecircle, (100+100*cos(radians(x)), 400+100*sin(radians(x))))for x in xcoordinates] 

myapp = App()
myapp.run()






