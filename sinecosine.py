"""
sinecosine.py
Author: Kai Darrow
Credit: Me 

Assignment:
Your program must:

Import the necessary names (e.g. CircleAsset, App, etc.) from the ggame library.
Import sin, cos, and radians names from the math library.
Using the technique in the last tutorial, generate a series of blue circles, a series of red circles, and a series of purple circles, such that:
The x-coordinates of the blue and red circles will vary between 0 and 360, in steps of 10.
The y-coordinates of the blue circles will be calculated using: 100+100*sin(radians(x))), where x values come from the x-coordinates in step 4.
The y-coordinates of the red circles will be calculated using: 100+100*cos(radians(x))), where x values come from the x-coordinates in step 4.
The x-coordinates of the purple circles will be calculated using: 100+100*cos(radians(x)), where x values come from the x-coordinates in step 4.
The y-coordinates of the purple circles will be calculated using: 400+100*sin(radians(x)), where x values come from the x-coordinates in step 4.
The final result should look like sine and cosine curves in blue and red, and a circle of circles in purple.

Submit your work in the usual way.
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

from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, LineAsset
from math import sin, cos, radians
"""Colors"""
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
purple = Color(0x800080, 1.0)
blackthinline = LineStyle(1, black)
blackthickline = LineStyle(3, black)
thinline = LineStyle(1, black)
sine = CircleAsset(5, thinline, blue)
cosine = CircleAsset(5, thinline, red)
circle = CircleAsset(5, thinline, purple)


xcoordinates = range(0, 360, 10)
juoksentelisinkohan = [100+100*cos(radians(x)) for x in range(0, 360, 10)]

# Generate a list of sprites that form a line!
sprites = [Sprite(sine, (x, 100 + 100*sin(radians(x)))) for x in xcoordinates]
sprites = [Sprite(cosine, (x, 100+100*cos(radians(x)))) for x in xcoordinates]
sprites = [Sprite(circle, (x, 400+100*sin(radians(x)))) for x in juoksentelisinkohan]


myapp = App()
myapp.run()