"""
sinecosine.py
Author: Joe Richter
Credit: Joe Richter

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
from ggame import App
myapp = App()
myapp.run()
by10 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360]
ycoordb = [100+100*sin(radians(x)) for x in by10]
ycoordr = [100+100*cos(radians(x)) for x in by10]
xcoordp = [100+100*cos(radians(x)) for x in by10]
ycoordp = [400+100*sin(radians(x)) for x in by10]
#For later!
blue = Color(0x0000ff, 1.0)
red = Color(0xff0000, 1.0)
purple = Color(0x800080, 1.0)
thinlineb = LineStyle(1, blue)
thinliner = LineStyle(1, red)
thinlinep = LineStyle(1, purple)
zippedr = list(zip(by10, ycoordr))
zippedb = list(zip(by10, ycoordb))
cosine = Sprite(zippedr)
sine = Sprite(zippedb)