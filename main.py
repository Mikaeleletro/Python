import pyxel

class Objeto:
    
    def __init__(self,x,y):
        
        self.x = x
        self.y = y
        self.vx = 5
        self.vy = 0
        self.gravidade = 0.9
        self.arrasto = 0.1
        
        
    def colisao(self):
        
        if self.x <= 0:
            self.x = 0
        if self.x >= 158:
            self.x = 158
        if self.y <= 0:
            self.y = 0
        if self.y >= 118:
            self.y = 118
            
    def quique(self):
        
        if self.y >= 118:
            self.vy = -(self.vy / 1.5)
        if self.x >= 159:
            self.vx = -(self.vx / 1.5)
            
    def velocidade(self):
    
        self.vy += self.gravidade
        self.y += self.vy
        if self.vx > 0:
            self.vx -= self.arrasto
            self.x += self.vx
        
    def desenhar(self):
        
        pyxel.rect(self.x,self.y,2,2,7)
        

objeto = Objeto(51,0)

def update():
    objeto.velocidade()
    objeto.colisao()
    objeto.quique()
            
        
     
def draw():
    
    pyxel.cls(0)
    objeto.desenhar()
    
pyxel.init(160,120)
pyxel.run(update,draw)
            
            
    