"""
sinecosine.py
Author: Emma Tysinger
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
from ggame import App, CircleAsset, LineStyle, Sprite, Color
from math import sin, cos, radians

red1=Color(0xff0000,1.0)
black=Color(0x000000,1.0)
blue1=Color(0x0000ff,1.0)
red2=Color(0xff0000,0.5)
blue2=Color(0x0000ff,0.5)

thinline=LineStyle(1,black)
red1circle=CircleAsset(2,thinline,red1)
blue1circle=CircleAsset(2,thinline,blue1)
red2circle=CircleAsset(2,thinline,red2)
blue2circle=CircleAsset(2,thinline,blue2)

xcoordinates=range(0,360,10)
sprites1 = [Sprite(red1circle, (x, 100 + 100*sin(radians(x)))) for x in xcoordinates]
sprites2 = [Sprite(blue1circle, (x, 100 + 100*cos(radians(x)))) for x in xcoordinates]


myapp=App()
myapp.run()
