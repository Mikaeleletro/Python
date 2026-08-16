import pyxel
class Bola:
    
    def __init__(self,x,y):
        
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.gravidade = 0.9
        self.arrasto = 0.1
        
    def desenhar(self):
        pyxel.pset(self.x,self.y,7)
        
    def queda(self):
            
        self.vy += self.gravidade
        self.y += self.vy
        if self.vx > 0:
            self.vx -= self.arrasto
            if self.vx == 0:
                self.x = 0
                
        if self.vx < 0:
            self.vx += self.arrasto
            if self.vx > 0:
                self.vx = 0
        self.x += self.vx
        
    def quique(self):
        
        if self.y >= 119:
            self.vy = -(self.vy / 1.5)
        if self.x >= 159:
            self.vx = -(self.vx/1.5)
        if self.x <= 0:
            self.vx = -(self.vx/1.5)
            
        
    def colicao(self):
        if self.x <= 0:
            self.x = 0
        if self.x >= 159:
            self.x = 159
        if self.y <= 0:
            self.y = 0
        if self.y >= 119:
            self.y = 119
            
pedra = Bola(0,61)
pedra.vx = 10
pedra.vy = -10

def update():
    
    pedra.queda()
    pedra.quique()
    pedra.colicao()

    
def draw():
    pedra.desenhar()

pyxel.init(161,121,fps = 30)
pyxel.run(update,draw)

    
        
        
