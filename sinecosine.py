"""
sinecosine.py
Author: Andrew Chen
Credit:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Programmed-Graphics
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Lists-and-sequences-using-Runpython-Console

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
from ggame import CircleAsset, App, Color, LineStyle, Sprite
from math import sin, cos, radians
blue = Color(0x0000ff, .5)
red = Color(0xff0000, .5)
purple = Color(0xae00ff, .5)
black = Color(0x000000, 1.0)

thinline = LineStyle(1, black)

deg = 0
deglist = []

bluecircle = CircleAsset(10, thinline, blue)
redcircle = CircleAsset(10, thinline, red)
purplecircle = CircleAsset(10, thinline, purple)

while deg <= 360:
    deglist.append(deg)
    deg += 10
for x in deglist:
    bluey = 100+100*sin(radians(x))
    redy = 100+100*cos(radians(x))
    purplex = 100+100*cos(radians(x))
    purpley = 400+100*sin(radians(x))
    Sprite(bluecircle, (x, bluey))
    Sprite(redcircle, (x, redy))
    Sprite(purplecircle, (purplex, purpley))

myapp = App()
myapp.run()
