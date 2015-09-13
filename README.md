# Sine-Cosine
---

In this assignment you must use *list comprehensions* to generate sprites that show the behavior
of certain mathematical functions: **sine** and **cosine**. See the references at the end for a 
tutorial that introduces this technique.

Fork this repository and create your program in the ```sinecosine.py``` file.

The sine and cosine functions are provided in the Python ```math``` library. These functions are used
to relate *angles* to *rectangular* (x,y) coordinate systems and can be very useful in computer
game design.

Unlike the last assignment using ```ggame```, this one will not provide any "skeleton" code to fill
in. You should use your submission for the [Picture assignment](https://github.com/HHS-IntroProgramming/Picture)
as a reference for starting this assignment. 

Your program must:

1. Import the necessary names (e.g. CircleAsset, App, etc.) from the  ```ggame``` library.
2. Import ```sin```, ```cos```, and ```radians``` names from the ```math``` library.
3. Using the technique in the [last tutorial]
  (https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/TUTORIAL:-Programmed-Graphics),
  generate a series of blue circles, a series of red circles, and a series of **purple** circles, such
  that:
4. The x-coordinates of the blue and red circles will vary between 0 and 360, in steps of 10.
5. The y-coordinates of the **blue** circles will be calculated using: 
  ```100+100*math.sin(math.radians(x)))```, where x values come from the x-coordinates in step 4.
6. The y-coordinates of the **red** circles will be calculated using:
  ```100+100*math.cos(math.radians(x)))```, where x values come from the x-coordinates in step 4.
7. The x-coordinates of the **purple** circles will be calculated using:
  ```100+100*math.cos(math.radians(x))```, where x values come from the x-coordinates in step 4.
8. The y-coordinates of the **purple** circles will be calculated using:
  ```400+100*math.sin(math.radians(x))```, where x values come from the x-coordinates in step 4.

The final result should look like [sine and cosine curves]
(https://www.google.com/search?q=sine+and+cosine+curves&rlz=1CAZZAD_enUS644US644&espv=2&biw=1280&bih=715&tbm=isch&tbo=u&source=univ&sa=X&ved=0CCoQsARqFQoTCOfPrMn48scCFYqXgAodHWIAUg)
in blue and red, and a circle of circles in purple.

Submit your work in the usual way.

See:
* [General information on using ggame](https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/TUTORIAL:-Displaying-Graphics)
* [General information on using list comprehensions with graphics]
  (https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/TUTORIAL:-Programmed-Graphics)
* [Detailed information on ggame](http://brythonserver.github.io/ggame/)
