import pyxel
class Jogador:
    def __init__(self,x,y,velocidade):
        
        self.x = x
        self.y = y
        self.hp = 50
        self.direcao = ""
        self.novo_x = x
        self.novo_y = y
        self.velocidade = velocidade
        
    def mover(self):
        
        self.novo_x = self.x
        self.novo_y = self.y
        if pyxel.btn(pyxel.KEY_SHIFT):
            self.velocidade = 5
        
        if pyxel.btn(pyxel.KEY_A):
            self.novo_x -= self.velocidade 
            self.direcao = "esquerda"
            
        if pyxel.btn(pyxel.KEY_D):
            self.novo_x += self.velocidade
            self.direcao = "direita"
            
        if pyxel.btn(pyxel.KEY_S):
            self.novo_y += self.velocidade
            self.direcao = "baixo"
            
        if pyxel.btn(pyxel.KEY_W):
            self.novo_y -= self.velocidade
            self.direcao = "cima"

        if  self.novo_x <= 0:
            self.novo_x = 0
            
        if self.novo_x >= 159:   
            self.novo_x = 159
            
        if self.novo_y <= 0:
            self.novo_y = 0
            
        if self.novo_y >= 119:
            self.novo_y = 119
            
    def desenhar(self):

        pyxel.pset(self.x,self.y,5)
        if self.direcao == "direita":
            pyxel.pset(self.x+1,self.y,6)
            
        if self.direcao == "esquerda":
            pyxel.pset(self.x-1,self.y,6)
            
        if self.direcao == "baixo":
            pyxel.pset(self.x,self.y+1,6)
            
        if self.direcao == "cima":
            pyxel.pset(self.x,self.y-1,6)
            
    def barra_vida_jogador(self):
        pyxel.rect(5,5,20*(self.hp/50),10,5)

class Parede:
    def __init__(self,x,y,tipo):
        self.x = x
        self.y = y
        self.tipo = tipo
        
        
    def desenhar(self):
        pyxel.rect(self.x,self.y,10,10, self.tipo)
        
    def colicao(self,jogador):
        
        if (jogador.novo_x >= self.x and
            jogador.novo_x <= self.x + 10 and
            jogador.y >= self.y and
            jogador.y <= self.y + 10):

            jogador.novo_x = jogador.x

        if (jogador.novo_y >= self.y and
            jogador.novo_y <= self.y + 10 and
            jogador.x >= self.x and
            jogador.x <= self.x + 10):

            jogador.novo_y = jogador.y
            
    def esta_dentro(self, jogador):
        
        if (jogador.x >= self.x and
            jogador.x <= self.x + 10 and
            jogador.y >= self.y and
            jogador.y <= self.y + 10):

            return True

        return False
    
    
paredes = []
jogador = Jogador(70,70,1)
tipo = 1
tipo_bloco = 1
def update():
    global tipo, tipo_bloco
    tipo_bloco = 1
    
    jogador.velocidade = 1
    for parede in paredes:
        if parede.esta_dentro(jogador):
            if parede.tipo == 3:
                tipo_bloco = 3
                jogador.velocidade = 0.5
            if parede.tipo == 2:
                tipo_bloco = 2
                
    if pyxel.btnp(pyxel.KEY_1):
        tipo = 1
    if pyxel.btnp(pyxel.KEY_2):
        tipo = 2
    if pyxel.btnp(pyxel.KEY_3):
        tipo = 3
        
    if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
        existe = False
        
        x_mouse = pyxel.mouse_x // 10 * 10
        y_mouse = pyxel.mouse_y // 10 * 10
        
        for parede in paredes:
            
            if parede.x == x_mouse and parede.y == y_mouse:
                existe = True
            
        if existe == False:
            
            paredes.append(Parede(x_mouse,y_mouse,tipo))
        
    if pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT):

        for parede in paredes:

            if (pyxel.mouse_x >= parede.x and
                pyxel.mouse_x <= parede.x + 10 and
                pyxel.mouse_y >= parede.y and
                pyxel.mouse_y <= parede.y + 10):

                paredes.remove(parede)
                break
            
    jogador.mover()
    for parede in paredes:
        if parede.tipo == 1:
            parede.colicao(jogador)
        
    jogador.x = jogador.novo_x
    jogador.y = jogador.novo_y
            
def draw():
    existe = False
    pyxel.cls(0)
    
    for parede in paredes:
        parede.desenhar ()
        
    if jogador.hp > 0:
        jogador.desenhar()
    
    x = pyxel.mouse_x // 10 * 10
    y = pyxel.mouse_y // 10 * 10
    
    
    for parede in paredes:
        
        if parede.x == x and parede.y == y:
            existe = True
            
    if existe == True:
        pyxel.rectb(x,y,10,10,8)
    else:
        pyxel.rectb(x,y,10,10,tipo)
    if tipo_bloco == 2:
        pyxel.text(5,5,"grama",3)
    if tipo_bloco == 3:
        pyxel.text(5,5,"agua",3)
        
pyxel.init(160,120,fps = 30)
pyxel.mouse(True)
pyxel.run(draw,update)