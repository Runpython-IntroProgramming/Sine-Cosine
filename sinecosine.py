"""
sinecosine.py
Author: Funjando
Credit: 

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
#Imports
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
from math import sin, cos, radians


#Colors
red=Color(0x910101, 1.0)
green=Color(0x9DE63E, 1.0)
blue=Color(0x0B1ABF, 1.0)
orange=Color(0xE35D09, 1.0)
purple=Color(0x8209AB, 1.0)
windowsheen=Color(0x74E3E3, 1.0)
hobbitgreen=Color(0x09B31D, 1.0)
leprechaungold=Color(0xD4BA15, 1.0)
black=Color(0x000000, 1.0)
yellow=Color(0xF5FC26, 1.0)
whitish=Color(0xC0EDEC, 1.0)

#colored lines
redline=LineStyle(4, red)
greenline=LineStyle(4, green)
blueline=LineStyle(1, blue)
orangeline=LineStyle(7, orange)
purpleline=LineStyle(4, purple)
blackline=LineStyle(1, black)
noline=LineStyle(0, black)


#Objects
bluecircle=CircleAsset(5, blueline, blue)
redcircle=CircleAsset(5, redline, red)
purplecircle=CircleAsset(5, purpleline, purple)

#x_coordinates
xcoordinates=range(0, 360, 10)

#y_coordinates



#sprites
[Sprite(bluecircle, (100+100*sin(radians(x)))) for x in xcoordinates]


