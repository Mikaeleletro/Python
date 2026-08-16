import pyxel

def update():
    global x,y
    
    x = pyxel.mouse_x
    y = pyxel.mouse_y
    
def draw():
    
    pyxel.cls(0)
    pyxel.line(x+10,y+10,10,10,7)
    

pyxel.init(101,101)
pyxel.run(update,draw)


    
    