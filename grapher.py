from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset
import math


SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

red = Color(0xff0000, 1.0)
blue = Color(0x0000ff, 1.0)
green = Color(0x00ff00, 1.0)
black = Color(0x000000, 1.0)
pink = Color(0xff00ff, 1.0)
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
    
    asset = CircleAsset(2, thinline, pink)

    def __init__(self, position):
        super().__init__(Dot.asset, position)
        self.x = 0
        self.loop = False
        
    
    def l(self):
        return 500-k*(self.x-840)-100*b
    
    
    def t(self):
        return 500-a*100*math.sin(h*(self.x-840+100*k)/100)
        
    def p(self):
        return 500-(a*(self.x-840)**2/100+100*b*self.x+100*c)
        
    def step(self):
        if 0 <= self.l() <= 1080:
            if mode == "l":
                n = self.y-(500-k*(self.x-840+1)-100*b)
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
                n = self.y-(500-a*100*math.sin(h*(self.x-840+100*k)/100))
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
                n = self.y-(500-(a*(self.x-840)**2/100+100*b*self.x+100*c))
                if not self.loop:
                    self.y = self.p()
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
        self.x += 1     
            
            
class Grapher(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        
        
        xaxis = RectangleAsset(1920,1, thinline, black)
        yaxis = RectangleAsset(1,1080, thinline, black)
        sprite1 = Sprite(xaxis, (0, 500))
        sprite2 = Sprite(yaxis, (840, 0))
        
        Dot((0,500))
        
    def step(self):
        for dot in self.getSpritesbyClass(Dot):
            dot.step()
      
            
myapp = Grapher(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
