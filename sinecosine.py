"""
sinecosine.py
Author: Eamon
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

from ggame import CircleAsset, Color, Sprite, App, LineStyle, RectangleAsset
import math

black = Color(0x000000, 1.0)
thinline = LineStyle(1, black)

yaxis = RectangleAsset(1, 250, thinline, black)
Sprite((yaxis), (250,0))
xaxis = yaxis = RectangleAsset(500, 1, thinline, black)
Sprite((xaxis), (0,125))
n = 360
k = 0
x = 10*k for k in range(0,n)
#pi = 4.0*sum([((-1.0)**k)/(2*k+1) for k in range(0,n)])
y = 100+100*sin(radians(x)))
point = CircleAsset(1, thinline, black)
Sprite((point), (x,y))



app = App(500,500) 
myapp = App()
myapp.run()


