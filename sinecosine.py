"""
sinecosine.py
Author: Jeff
Credit: None

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

from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
from math import sin, cos, radians

k = int(input("f(x) = kx + b, set k: "))
b = int(input("f(x) = kx + b, set b: "))

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
purple = Color(0xff00ff, 1.0)

thinline = LineStyle(0, black)

xcord = range(0, 1500, 1)
dot1 = RectangleAsset(2,2, thinline, red)
dot2 = RectangleAsset(2,2, thinline, blue)
dot3 = CircleAsset(1, thinline, purple)
xaxis = RectangleAsset(1500,1, thinline, black)
yaxis = RectangleAsset(1,1050, thinline, black)

#sprites = [Sprite(dot1, (x, 400+ampli*cos(radians(-x))))for x in xcord]
#sprites1 = [Sprite(dot2, (x, 400+100*sin(radians(-x)))) for x in xcord]
sprite2 = Sprite(xaxis, (0, 404))
sprite3 = Sprite(yaxis, (718, 0))

sprites4 = [Sprite(dot1, (x, 400-k*(x-718)-100*b)) for x in xcord]

myapp = App()
myapp.run()