"""
sinecosine.py
Author: <your name here>
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

blue=Color(0x528B8B, 1.0)
red=Color(0xCD0000, 1.0)
purple=Color(0xBDA0CB, 1.0)

noline=LineStyle(0, red)

bc=CircleAsset(6,noline,blue)
rc=CircleAsset(6,noline,red)
pc=CircleAsset(6,noline,purple)

xcoor=list(range(0,370,10))

bluecircles=[Sprite(bc, (x , 100+100*sin(radians(x)))) for x in xcoor]
redcircles=[Sprite(rc, (x , 100+100*cos(radians(x)))) for x in xcoor]
purple=[Sprite(pc, (100+100*cos(radians(x)), 400+100*sin(radians(x)))) for x in xcoor]

myapp=App()
myapp.run()
