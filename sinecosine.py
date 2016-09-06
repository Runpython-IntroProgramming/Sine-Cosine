"""
sinecosine.py
Author: Peter Bynum
Credit: None

Assignment: Sine-Cosine Challenge

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
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

blue = Color(0x07608f, 1.0)
purple = Color(0x993299, 1.0)
red = Color(0xf41844, 1.0)
bline = LineStyle(1, blue)
pline = LineStyle(1, purple)
rline = LineStyle(1, red)

xcoords = range(0, 360, 10)
bcircle = CircleAsset(4, bline, blue)
rcircle = CircleAsset(4, rline, red)
pcircle = CircleAsset(4, pline, purple)

sine_sprites = [Sprite(bcircle, (x,100+100*sin(radians(x)))) for x in xcoords]
cos_sprites = [Sprite(rcircle, (x,100+100*cos(radians(x)))) for x in xcoords]
purple_sprites = [Sprite(pcircle, (100+100*cos(radians(x)),400+100*sin(radians(x)))) for x in xcoords]



myapp = App()
myapp.run()