import pyxel
import math


class Pendulo:

    def __init__(self):

        # Ponto onde a corda está presa
        self.ponto_x = 80
        self.ponto_y = 20

        # Tamanho da corda
        self.comprimento = 4

        # Ângulo inicial
        self.angulo = 0.8

        # Velocidade angular
        self.velocidade = 0

        # Gravidade
        self.gravidade = 5

        # Posição da bola
        self.x = 0
        self.y = 0

    def fisica(self):

        # Aceleração angular
        aceleracao = -(self.gravidade / self.comprimento) * math.sin(self.angulo)

        # Atualiza a velocidade
        self.velocidade += aceleracao

        # Atualiza o ângulo
        self.angulo += self.velocidade

    def atualizar_posicao(self):

        # Calcula a posição da bola usando seno e cosseno
        self.x = self.ponto_x + self.comprimento * math.sin(self.angulo)

        self.y = self.ponto_y + self.comprimento * math.cos(self.angulo)

    def desenhar(self):

        # Ponto fixo
        pyxel.circ(
            self.ponto_x,
            self.ponto_y,
            3,
            7
        )

        # Corda
        pyxel.line(
            self.ponto_x,
            self.ponto_y,
            self.x,
            self.y,
            7
        )

        # Bola
        pyxel.circ(
            self.x,
            self.y,
            5,
            8
        )


pendulo = Pendulo()


def update():

    pendulo.fisica()
    pendulo.atualizar_posicao()


def draw():

    pyxel.cls(0)

    pendulo.desenhar()


pyxel.init(160, 120)

pyxel.run(update, draw)