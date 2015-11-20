from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset
import math

SCREEN_WIDTH = 1536
SCREEN_HEIGHT = 1024

red = Color(0xff0000, 1.0)
blue = Color(0x0000ff, 1.0)
green = Color(0x00ff00, 1.0)
black = Color(0x000000, 1.0)
purple = Color(0xff00ff, 1.0)
thinline = LineStyle(0, black)

xcord = range(0, 1500, 1)

mode = input("Which type of function do you have? \nl for linear, t for Trig, p for Parabola ")
if mode == "l":
    k = float(input("f(x) = kx + b, set the value of k: "))
    b = float(input("f(x) = kx + b, set the value of b: "))
elif mode == "t":
    a = int(input("f(x) = a sin h (x + k) , set the value of a: "))
        
class Dot(Sprite):
    
    asset = RectangleAsset(2,2, thinline, blue)

    def __init__(self, position):
        super().__init__(Dot.asset, position)
        self.x = 0
    
    def l(self):
        return 450-k*(self.x-750)-100*b
        
    def step(self):
        if self.x < 1500:
            if mode == "l":
                self.y = self.l()
                sprite = Sprite(Dot.asset, (self.x, self.y))
                n = self.y-(450-k*(self.x-750+1)-100*b)
                while n > 0:
                    self.y -= 2
                    sprite1 = Sprite(Dot.asset, (self.x, self.y))
                    n -= 1
                    print(n)
                self.x += 1
                    
            elif mode == "t":
                sprite = Sprite(Dot.asset, (self.x, 450-a*100*math.tan((self.x-750)/100)))
                self.x += 1
                
            elif mode == "p":
                sprite = Sprite(Dot.asset, (self.x, 450-((self.x-750)**2/100)))
                self.x += 1
              
            
            
class Grapher(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        
        #black = Color(0x000000, 1.0)
        #thinline = LineStyle(0, black)
        xaxis = RectangleAsset(1500,1, thinline, black)
        yaxis = RectangleAsset(1,1050, thinline, black)
        sprite1 = Sprite(xaxis, (0, 450))
        sprite2 = Sprite(yaxis, (750, 0))
        
        Dot((0,450))
        #sprite0 = [Sprite(Dot.asset, (x, 450-k*(x-750)-100*b)) for x in xcord]
        
    def step(self):
        for dot in self.getSpritesbyClass(Dot):
            dot.step()
        #for dot in self.getSpritesbyClass(Dot):
            #dot.step()
            
myapp = Grapher(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
