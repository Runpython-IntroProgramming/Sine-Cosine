"""
sinecosine.py
Author: Liam A
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

Lgreen = Color (0x7CFC00, 0.95)
turqo = Color (0x40E0D0, 0.99)
Orange = Color (0xFF8600, 1)
purp = Color (0x68228B, 0.6)
brn = Color (0x5C3317, 0.9)
pale = Color (0xFFFACD, 0.4)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
crimson = Color(0xA02422, 0.97000000000000000000000000000000000000000000000000000000000000000000000001)

thinline = LineStyle(1, black)
noline = LineStyle(0.1, blue)
mycircle = CircleAsset(5, thinline, blue)
urcircle = CircleAsset(6, thinline, crimson)
arcircle = CircleAsset(6, thinline, purp)
rb_xcoord = range(100, 600, 10)
#gen_xcoor

sprites = [Sprite(mycircle, (x, 100+100*sin(radians(x)))) for x in rb_xcoord]
sprites = [Sprite(urcircle, (x, 100+100*cos(radians(x)))) for x in rb_xcoord]
#sprites = [Sprite(arcircle, (x, x*0.6 + 20)) for x in gen_xcoor]



myapp = App()
myapp.run()