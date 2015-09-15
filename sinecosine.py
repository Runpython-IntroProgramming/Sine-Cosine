"""
sinecosine.py
Author: Milo Wilcox
Credit: http://www.w3schools.com/tags/ref_colorpicker.asp

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
red=Color(0x0066FF,0.75)
blue=Color(0x0033CC,0.75)
purple=Color(0x6600FF,0.75)
linea=LineStyle(1,blue)
lineb=LineStyle(1,red)
linec=LineStyle(1,blue)
blucir=CircleAsset(5,linea,blue)
redcir=CircleAsset(5,lineb,red)
purcir=CircleAsset(5,linec,purple)
brxcor=range(0,360,10)
fpxcor=lambda x: 100+100*cos(radians(x))
fbycor=lambda x: 100+100*sin(radians(x))
frycor=lambda x: 100+100*cos(radians(x))
fpycor=lambda x: 400+100*sin(radians(x))
sprites=[Sprite(blucir,(x, fbycor(x))) for x in brxcor]
sprites=[Sprite(redcir,(x, frycor(x))) for x in brxcor]
sprites=[Sprite(purcir,(100+100*cos(radians(x)), fpycor(x))) for x in brxcor]
myapp=App()
myapp.run()
