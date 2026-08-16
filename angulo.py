import pyxel
import math
def update():
    global x,y
    
    x = pyxel.mouse_x
    y = pyxel.mouse_y
    
    vetor_x_a = x - 10
    vetor_y_a = (110 - y)
    vetor_x_b = (x - 10)
    vetor_y_b = 0
    
    modulo_a = (((110 - y)**2)+((x-10)**2))**0.5
    modulo_b = ((x - 10)**2)**0.5
    
    
    produto_dos_modulos = modulo_a * modulo_b
    
    produto_escalar = (vetor_x_a * vetor_x_b) + (vetor_y_a * vetor_y_b)
    if produto_dos_modulos > 0:
        angulo = math.degrees(math.acos(produto_escalar / produto_dos_modulos))
        print(angulo)
    else:
        print("90")
    
    #a.b/|a.b|
    
def draw():
    pyxel.cls(0)
    
    pyxel.line(10,110,10,y,7)
    pyxel.line(10,110,x,110,7)
    pyxel.line(10,110,x,y,7)
    
pyxel.init(160,120)
pyxel.mouse(True)
pyxel.run(update,draw)
