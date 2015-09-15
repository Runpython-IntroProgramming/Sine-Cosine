"""
sinecosine.py
Author: Sarah Dunbar
Credit: none

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
from math import sin, cos, radians
from ggame import App, Color, LineStyle, Sprite, CircleAsset

purple = Color(0xcc00ff, 1.0)
blue = Color(0x0000ff, 1.0)
red = Color(0xff0000, 1.0)
black = Color(0x000000, 1.0)

line = thinline = LineStyle(1, black)
sincircle = CircleAsset(5, thinline, blue)
coscircle = CircleAsset(5, thinline, red)
pcircle = CircleAsset(5, thinline, purple)

xcoords = range(0, 360, 10)

sinline = [Sprite(sincircle, (x, (100+100*sin(radians(x))))) for x in xcoords]
cosline = [Sprite(coscircle, (x, (100+100*cos(radians(x))))) for x in xcoords]
xvaluecircle = [(100+100*cos(radians(x))) for x in xcoords]
circle = [Sprite(pcircle, (x, (400+100*sin(radians(x))))) for x in xcoords]

myapp = App()
myapp.run()







