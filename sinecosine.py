"""
sinecosine.py
Author: James Eiler
Credit: Mr Dennison's Tutorials

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
from ggame import App, Color, LineStyle, Sprite, CircleAsset
from math import sin, cos, radians
app=App()
app.run()
xcoords = [x for x in range(0, 360, 10)]
x=list(range(0, 360, 10))
red = Color(0xff0000, 1.0)
blue = Color(0x0000ff, 1.0)
print('Its Purple If I Say it is!')
purple = Color(0x000000, 1.0)
#Blue Circles
x = list(range(0, 360, 10))
#y = 100+100**sin(radians(x))
myline = LineStyle(1, blue)
Mycircle = CircleAsset(5, myline, blue)
sprites = [Sprite(Mycircle, (x, 100+100*sin(radians(x)))) for x in xcoords]
#Red Circles 
Myline2 = LineStyle(1, red)
Mycircle2 = CircleAsset(5, Myline2, red)
sprites = [Sprite(Mycircle2, (x, 100+100*cos(radians(x)))) for x in xcoords]
#PurpleCircles
Myline3 = LineStyle(1, purple)
Mycircle3 = CircleAsset(5, Myline3, purple)
sprites = [Sprite(Mycircle3, (100+100*cos(radians(x)), 400+100*sin(radians(x)))) for x in xcoords]
