"""
sinecosine.py
Author: Alice Frederick
Credit: <list sources used, if any>

Assignment: Plotting Sine and Cosine 

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
from math import sin, cos, radians

purple = Color(0xd98cd9, 1.0)
red = Color(0xff6666, 1.0)
blue = Color(0x80dfff, 1.0)
black = Color(0x000000, 0.5)

line = LineStyle(0.5,black)

sincircle = CircleAsset(5, line, blue)
coscircle = CircleAsset(5, line, red)
circle = CircleAsset(5, line, purple)
coords = list(range(0, 360, 10))

sines = [Sprite(sincircle, (400+x,100+100*sin(radians(x)))) for x in coords]
cosines = [Sprite(coscircle, (400+x,100+100*cos(radians(x)))) for x in coords]
circles = [Sprite(circle, (400+100*cos(radians(x)),400+100*sin(radians(x)))) for x in coords]

myapp = App()
myapp.run()