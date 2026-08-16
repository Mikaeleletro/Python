import pyxel
class Jogador:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.hp = 50
        self.direcao = ""

    def mover(self):

        if pyxel.btn(pyxel.KEY_A):
            self.x -= 2
            self.direcao = "esquerda"
        if pyxel.btn(pyxel.KEY_D):
            self.x += 2
            self.direcao = "direita"
        if pyxel.btn(pyxel.KEY_S):
            self.y += 2
            self.direcao = "baixo"
        if pyxel.btn(pyxel.KEY_W):
            self.y -= 2
            self.direcao = "cima"
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

    def atacar(self,zombies):
        if pyxel.btnp(pyxel.KEY_SPACE):
            zombies.hp -= 10
            
    def barra_vida_jogador(self):
        pyxel.rect(5,5,20*(self.hp/50),10,5)

class Zombie:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.hp = 50
        self.timer = 30
    
    def desenhar(self):
        pyxel.pset(self.x,self.y,5)

    def esta_perto(self,jogador):

        distancia_x = abs(jogador.x - self.x)
        distancia_y = abs(jogador.y - self.y)

        if distancia_x <= 15 and distancia_y <= 15:
            return True
        return False
    
    def perseguir(self,jogador):
        distancia_x = abs(jogador.x - self.x)
        distancia_y = abs(jogador.y - self.y)

        if distancia_x <= 15 and distancia_y <= 15:
            
            if jogador.x > self.x:
                self.x += 1

            if jogador.x < self.x:
                self.x -= 1

            if jogador.y > self.y:
                self.y += 1

            if jogador.y < self.y:
                self.y -= 1
    def barra_vida_zombie(self):
        pyxel.rect(self.x , self.y-3 , 4*(self.hp/50), 2,4)
        
    def zombie_atacar(self,jogador):
        if self.timer > 0:
            self.timer -=1
        if self.timer == 0:
                jogador.hp -= 1
                self.timer = 30
        
jogador = Jogador(10,10)
zombies = [
    Zombie(50,50),
    Zombie(100,100),
    Zombie(0,119)
]
def update():
    jogador.mover()
    for zombie in zombies:
        if zombie.hp > 0:
            zombie.perseguir(jogador)
            if zombie.esta_perto(jogador):
                zombie.zombie_atacar(jogador)
                jogador.atacar(zombie)
            
def draw():
    pyxel.cls(0)
    if jogador.hp > 0:
        jogador.barra_vida_jogador()
        jogador.desenhar()
    for zombie in zombies:
        if zombie.hp > 0:
            zombie.barra_vida_zombie()
            zombie.desenhar()
            if zombie.esta_perto(jogador):
                pyxel.text(0,0,"Zombie Perto!!",4)
    
            
    pyxel.text(10,10,f"{jogador.x}",5)
    
pyxel.init(160,120,fps = 30)
pyxel.run(draw,update)
pyxel.mouse(True)