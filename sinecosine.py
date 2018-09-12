"""
sinecosine.py
Author: Ella Edmonds
Credit: used https://www.rapidtables.com/web/color/purple-color.html for colors

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

l = Color(0xE6E6FA, 1.0)
p = Color(0x8A2BE2, 1.0)


line1=LineStyle(1,l)
line2=LineStyle(1,p)

mycircle1 = CircleAsset(5, line1, l)
mycircle2 = CircleAsset(5, line2, p)

xcordinates=range(10,500,5)

sprites = [Sprite(mycircle1, (x, sin(radians(x))*100+100)) for x in xcordinates]
sprites = [Sprite(mycircle2, (x, cos(radians(x))*100+100)) for x in xcordinates]

myapp = App()
myapp.run()
