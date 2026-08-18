#survival vampire
import pyxel
class Personagem():
    def __init__(self):
        
        self.x = 80
        self.y = 60
        self.direcao = "esquerda"
        
    def movimento(self):
        
        if pyxel.btn(pyxel.KEY_W):
            self.y -= 2
            self.direcao = "cima"
            
        if pyxel.btn(pyxel.KEY_S):
            self.y += 2
            self.direcao = "baixo"
            
        if pyxel.btn(pyxel.KEY_A):
            self.x -= 2
            self.direcao = "esquerda"
            
        if pyxel.btn(pyxel.KEY_D):
            self.x += 2
            self.direcao = "direita"
            
    def desenhar(self):
        x = pyxel.mouse_x
        y = pyxel.mouse_y
        
        pyxel.rect(self.x,self.y,2,2,7)
        if pyxel.btn(pyxel.KEY_SPACE):
            pyxel.line(self.x,self.y,x,y,7)
        
        if self.direcao == "cima":
            pyxel.rect(self.x,self.y-2,2,2,8)
            
        if self.direcao == "baixo":
            pyxel.rect(self.x,self.y+2,2,2,8)
            
        if self.direcao == "direita":
            pyxel.rect(self.x+2,self.y,2,2,8)
            
        if self.direcao == "esquerda":
            pyxel.rect(self.x-2,self.y,2,2,8)
            
    def colicao(self):
        
        if self.x <= 0:
            self.x = 0
            
        if self.x >= 158:
            self.x = 158
            
        if self.y >= 118:
            self.y = 118
            
        if self.y <= 0:
            self.y = 0
    
jogador = Personagem()

def update():
    
    jogador.movimento()
    jogador.colicao()
    
def draw():
    
    pyxel.cls(0)
    jogador.desenhar()
    pyxel.text(0,0,f"{jogador.direcao}",7)
    
pyxel.init(160,120)
pyxel.run(update,draw)
        
