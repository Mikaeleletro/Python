import pyxel


class Bola:
    
    def __init__(self,vx,vy,cor):
        
        self.x = 10
        self.y = 60
        self.vx = vx
        self.vy = vy
        self.gravidade = 0.9
        self.arrasto = 0.1
        self.cor = cor
        
    def desenhar(self):
        pyxel.pset(self.x,self.y,self.cor)
        
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
            
quantidade = int(input("quantos objetos quer?(máximo 15)"))
i = 1
lista = []
while i <= quantidade:
    
    a = int(input(f"qual velocidade vx{i}:..."))
    b = int(input(f"qual velocidade vy{i}:..."))
    
    if i <= 15:
        lista.append(Bola(a,b,i))
        i += 1
    elif i <= 0:
        print("numero inválido...")
    else:
        print("numero maximo: 15")
        
def update():
    for objeto in lista:
        objeto.queda()
        objeto.colicao()
        objeto.quique()
    
def draw():
    
    for objeto in lista:
        objeto.desenhar()
        
pyxel.init(161,121,fps = 30)
pyxel.run(update,draw)

    
        
        
