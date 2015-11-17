from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset
import math

SCREEN_WIDTH = 1536
SCREEN_HEIGHT = 1024

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
purple = Color(0xff00ff, 1.0)
thinline = LineStyle(0, black)

xcord = range(0, 1500, 1)

mode = input("Which type of function do you have? \nL for linear, T for Trig, P for Parabola ")
if mode == "L":
    k = int(input("f(x) = kx + b, set the value of k: "))
    b = int(input("f(x) = kx + b, set the value of b: "))
elif mode == "T":
    a = int(input("f(x) = a sin h (x + k) , set the value of a: "))
        
class Dot(Sprite):
    
    asset = RectangleAsset(2,2, thinline, red)

    def __init__(self, position):
        super().__init__(Dot.asset, position)
        self.x = 0
        sprite = Sprite(self.asset, (self.x, 450-k*(self.x-718)-100*b))
        
        
    def step(self):
        self.x += 1
        sprite0 = Dot(self.x, 450-k*(self.x-718)-100*b)
        
class Grapher(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        
        black = Color(0x000000, 1.0)
        thinline = LineStyle(0, black)
        xaxis = RectangleAsset(1500,2, thinline, black)
        yaxis = RectangleAsset(2,1050, thinline, black)
        sprite1 = Sprite(xaxis, (0, 450))
        sprite2 = Sprite(yaxis, (718, 0))
        
        #sprite0 = [Sprite(Dot.asset, (x, 450-k*(x-718)-100*b)) for x in xcord]
        
    def step():
        for dot in self.getSpritesbyClass(Dot):
            dot.step()
            
myapp = Grapher(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
