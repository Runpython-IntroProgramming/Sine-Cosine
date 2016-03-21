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

from ggame import App, Color, LineStyle, Sprite
from ggame import CircleAsset
from math import cos, sin, radians

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

grey = Color(0x818181, 1.0)
line = LineStyle(2, black)

sprite1 = CircleAsset(75, line, grey)

Sprite1 = CircleAsset( 20, 20, line, grey )



(range(0, 360, 10))
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 
150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 
280, 290, 300, 310, 320, 330, 340, 350]

[x//5 for x in range(0, 360, 10)]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 
34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 
66, 68, 70]

sprites = [Sprite(mycircle, (x,200*sin(radians(x)))) for x in range(0, 360, 10)]

#200*sin(radians(x))
#200*cos(radians(x))
#200*cos(radians(x))
#500*sin(radians(x))


myapp = App()
myapp.run()