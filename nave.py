from PPlay.window import *
from PPlay.gameimage import *
import math
from game import janela

#nave
nave = GameImage("images/nave.png")
nave.x = janela.width - janela.width * 50/100
nave.y = janela.height - janela.height * 10/100
vel_nave = 200

#vetor para guardar os tiros da nave
tiros = []
#velocidade dos tiros
vel_tiros = 450
cont_tempo = tempo_recarga = 0.9
def getTiros(nave):
    elemento = GameImage("images/tiro.png")
    elemento.x = nave.x + (nave.width/2)
    elemento.y = nave.y - (nave.height/2)
    tiros.append(elemento)

def tirosFuncionalidade():
    for i in range(qtd_elementos):
        tiros[i].draw()
    for i in range(qtd_elementos):
        tiros[i].y = tiros[i].y - vel_tiros*janela.delta_time()
    for i in range(qtd_elementos-1):
        if (tiros[i].y < 0):
            tiros.pop(i)
#fim dos tiros
