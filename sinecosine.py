"""
sinecosine.py
Author: Claire Adner
Credit: <list sources used, if any>

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

from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
from math import sin, cos, radians

# colors
red = Color(0xff0000, 1.0)
blue = Color(0x0000ff, 1.0)
purple = Color(0x800080, 1.0)
black = Color(0x000000, 1.0)
# thin black line
thinline = LineStyle(1, black)

#circles
circle_blue = CircleAsset (10, thinline, blue)
circle_red = CircleAsset (10, thinline, red)
circle_purple = CircleAsset (10, thinline, purple)

x = range(0, 360, 10)

#sprites/equations for the circles to follow
Sprite (circle_blue, ((anx),(100+100*sin(radians(anx)))))
#Sprite (circle_red, ((x),(100+100*cos(radians(x)))))
#Sprite (circle_purple, ((100+100*cos(radians(x))),(400+100*sin(radians(x)))))

sprites = [Sprite (circle_blue, ((anx),(100+100*sin(radians(anx))))) for anx in x)]









