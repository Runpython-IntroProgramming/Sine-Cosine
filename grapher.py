from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset
import math


y = 0

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
    a = float(input("f(x) = a sin h (x + k) , set the value of a: "))
    h = float(input("f(x) = a sin h (x + k) , set the value of h: "))
    k = float(input("f(x) = a sin h (x + k) , set the value of k: "))
elif mode == "p":
    a = float(input("f(x) = ax^2 + bx + c , set the value of a: "))
    b = float(input("f(x) = ax^2 + bx + c , set the value of b: "))
    c = float(input("f(x) = ax^2 + bx + c , set the value of c: "))
        
class Dot(Sprite):
    
    asset = CircleAsset(2, thinline, blue)

    def __init__(self, position):
        super().__init__(Dot.asset, position)
        self.x = 0
        self.loop = False
        
    
    def l(self):
        return 550-k*(self.x-750)-100*b
    
    
    def t(self):
        return 550-a*100*math.sin((self.x-750)/100)
        
    def step(self):
        if 0 <= self.l() <= 1080:
            if mode == "l":
                n = self.y-(550-k*(self.x-750+1)-100*b)
                if not self.loop:
                    self.y = self.l()
                    sprite = Sprite(Dot.asset, (self.x, self.y))
                    
                if n > 1:
                    self.y -= 2
                    sprite1 = Sprite(Dot.asset, (self.x, self.y))
                    self.loop = True
                    n -= 2
                else:
                    self.loop = False
                    
                    
            elif mode == "t":
                n = self.y-(550-a*100*math.sin(h*(self.x-750+100*k)/100))
                if not self.loop:
                    self.y = self.t()
                    sprite = Sprite(Dot.asset, (self.x, self.y))
                    print("1")
                    
                if n > 1:
                    self.y -= 1
                    sprite1 = Sprite(Dot.asset, (self.x, self.y))
                    self.loop = True
                    n -= 1
                    print("2")
                    
                elif n < -1:
                    self.y += 1
                    sprite1 = Sprite(Dot.asset, (self.x, self.y))
                    self.loop = True
                    n += 1
                    print("3")
                    
                else:
                    self.loop = False
                    
                    print("4")
                
            elif mode == "p":
                sprite = Sprite(Dot.asset, (self.x, 550-(a*(self.x-750)**2/100+100*b*self.x+100*c)))
                
        self.x += 1     
            
            
class Grapher(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        
        SCREEN_WIDTH = 1920
        SCREEN_HEIGHT = 1080
        
        xaxis = RectangleAsset(1920,1, thinline, black)
        yaxis = RectangleAsset(1,1080, thinline, black)
        sprite1 = Sprite(xaxis, (0, 550))
        sprite2 = Sprite(yaxis, (750, 0))
        
        Dot((0,550))
        
    def step(self):
        for dot in self.getSpritesbyClass(Dot):
            dot.step()
      
            
myapp = Grapher(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
