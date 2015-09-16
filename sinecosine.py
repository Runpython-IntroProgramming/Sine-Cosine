"""
sinecosine.py
Author: James Napier
Credit: http://www.discoveryplayground.com/computer-programming-for-kids/rgb-colors/

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

from ggame import App, Color, CircleAsset, LineStyle, Sprite
from math import sin, cos, radians
blue=Color(0x0000ff, 1.0)
red=Color(0xff0000, 1.0)
purple=Color(0xa020f0, 1.00)
black=Color(0x000000, 1.0)

thinline=LineStyle(1, black)
mycircle=CircleAsset(5, thinline, blue)
mycircle2=CircleAsset(5, thinline, red)
mycircle3=CircleAsset(5, thinline, purple)

xcoordinates=range(0, 360, 10)
ycoordinates=[100+100*sin(radians(x))for x in xcoordinates]
y2coordinates=[100+100*cos(radians(x))for x in xcoordinates]
x2coordinates=[100+100*cos(radians(x))for x in xcoordinates]
y3coordinates=[400+100*sin(radians(x))for x in xcoordinates]

sprites=[Sprite(mycircle, (x, y*100+100))for x in xcoordinates]
sprites=[Sprite(mycircle2, (x, y2*100+100))for x in xcoordinates]
sprites=[Sprite(mycircle3, (x2, y3*400+100))for x in xcoordinates]

#ask milo about cos, sin, radians and importing
myapp=App()
myapp.run()
