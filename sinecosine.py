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
#from ggame import GFX
from ggame import App
#sprite = Sprite + GFX
blue = Color(0x0000ff, 1.0)
red = Color(0xff0000, 1.0)
purple = Color(0x800080, 1.0)
by10 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000]
thinliner = LineStyle(1, red)
thinlineb = LineStyle(1, blue)
thinlinep = LineStyle(1, purple)
circleb = CircleAsset(13, thinlineb, blue)
circler = CircleAsset(13, thinliner,red)
circlep = CircleAsset(7, thinlinep, purple)
ycoordb = [100+100*sin(radians(x)) for x in by10]
ycoordr = [100+100*cos(radians(x)) for x in by10]
xcoordp = [100+100*cos(radians(x)) for x in by10]
ycoordp = [400+100*sin(radians(x)) for x in by10]
circlecoordp = (400+100*sin(radians(x)))
zippedp = list(zip(by10, ycoordp))
s = [Sprite(circlep, circlecoordp) for circlecoordp in zippedp]
zippedr = list(zip(by10, ycoordr))
zippedb = list(zip(by10, ycoordb))
cosine = [Sprite(circler, ycoordr) for ycoordr in zippedr]
sine = [Sprite(circleb, ycoordb) for ycoordb in zippedb]
#^ [Sprite(circle, coord) for coord in zippedb] 
myapp = App()
myapp.run()
