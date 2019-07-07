from PPlay.window import *
from PPlay.gameimage import *
import math
import random
from pontuacao import *
carregarPontuacao()
clock = pygame.time.Clock()

xJanela = 900
yJanela = 600

# comprimento e largura da tela
janela = Window(xJanela, yJanela)
janela.set_title("Space Invaders")
teclado = Window.get_keyboard()
mouse = Window.get_mouse()
background = GameImage("images/background.png")

game_over = GameImage("images/game-over.png")

frame = 0

dificuldade = 1
pontuacao = 0
pontos_matar_monstro = 1000
tempo = 0
# nave
nave = GameImage("images/nave.png")
nave.x = janela.width - janela.width * 50 / 100
nave.y = janela.height - janela.height * 10 / 100
vel_nave = 200
cont_vidas = 3
numbers = []

# posicao da imagem game over
game_over.set_position(janela.width - janela.width * 70 / 100, janela.height - janela.height * 55 / 100)
for i in range(10):
    numbers.append(GameImage("images/" + str(i) + ".png"))
    numbers[i].set_position(20 * i, 20 * i)

# vetor que guarda os tiros do personagem
tiros = []
# vetor que guarda os tiros dos monstros
tiros_monstros = []

# monstros
monstros = []
vel_monstros = 50
vel_monstros_descida = 1000
cont_monstros = 0
espacamento_x_monstro = janela.height - janela.height * 95 / 100
espacamento_y_monstro = janela.width - janela.width * 95 / 100
linha_monstros = int(janela.height / 300)
coluna_monstros = int(janela.width / 200)

# variaveis menu
x = 150
y = 200

bt_jogar = GameImage("images/play-on-hover.png")
bt_jogar.x = x
bt_jogar.y = y

bt_configuracoes = GameImage("images/configuracoes-on-hover.png")
bt_configuracoes.x = x - 55
bt_configuracoes.y = y + 50 * 2

bt_pontuacao = GameImage("images/pontuacao.png")
bt_pontuacao.x = x - 40
bt_pontuacao.y = y + 50

bt_sair = GameImage("images/sair-on-hover.png")
bt_sair.x = x + 5
bt_sair.y = y + 50 * 3


# fim variaveis menu

def getUserOptions():
    global frame
    if mouse.is_over_object(bt_jogar) and mouse.is_button_pressed(1):
        frame = 1
    if mouse.is_over_object(bt_configuracoes) and mouse.is_button_pressed(1):
        frame = 2
    if mouse.is_over_object(bt_pontuacao) and mouse.is_button_pressed(1):
        frame = 3
    if mouse.is_over_object(bt_sair) and mouse.is_button_pressed(1):
        gravarPontuacao()
        janela.close()
    if teclado.key_pressed("ENTER") or teclado.key_pressed("ESC"):
        frame = 0


def menu():
    global frame
    global pontuacao
    while True:
        if frame == 0:
            while frame == 0:
                janela.update()
                background.draw()
                bt_jogar.draw()
                bt_configuracoes.draw()
                bt_pontuacao.draw()
                bt_sair.draw()
                getUserOptions()
                janela.update()
        if frame == 1:
            main()
        # configuracoes
        # dificuldade e mais
        elif frame == 2:
            frame = 0
        # ranking
        elif frame == 3:
            while frame == 3:
                janela.update()
                background.draw()
                janela.draw_text("Pontos", janela.width - janela.width * 80 / 100,
                                 janela.height - janela.height * 85 / 100, size=30, color=(220, 220, 220),
                                 font_name="Arial", bold=True, italic=False)
                janela.draw_text("Nome", janela.width - janela.width * 40 / 100,
                                 janela.height - janela.height * 85 / 100, size=30, color=(220, 220, 220),
                                 font_name="Arial", bold=True, italic=False)
                for i in range(len(matriz_pontuacao)):
                    janela.draw_text(str(matriz_pontuacao[i][0]), janela.width - janela.width * 80 / 100,
                                     janela.height - janela.height * (75 - 7 * i) / 100, size=23, color=(220, 220, 220),
                                     font_name="Arial", bold=True, italic=False)
                    janela.draw_text(matriz_pontuacao[i][1], janela.width - janela.width * 40 / 100,
                                     janela.height - janela.height * (75 - 7 * i) / 100, size=23, color=(220, 220, 220),
                                     font_name="Arial", bold=True, italic=False)
                getUserOptions()
                janela.update()


def gameOver():
    global frame
    global cont_vidas
    global pontuacao
    global dificuldade
    global vel_nave
    global tiros
    global tiros_monstros
    global monstros
    global vel_monstros
    global vel_monstros_descida
    global cont_monstros
    global linha_monstros
    global coluna_monstros

    resp = False
    while resp == False:
        janela.update()
        background.draw()
        game_over.draw()
        getUserOptions()
        if teclado.key_pressed("SPACE"):
            resp = True
        janela.update()

    if matriz_pontuacao[9][0] < pontuacao:
        nome = input("Digite seu nome: ")
        getPontuacao(int(pontuacao), nome)
    frame = 0
    cont_vidas = 3
    pontuacao = 0
    dificuldade = 1

    vel_nave = 200
    # vetor que guarda os tiros do personagem
    tiros = []
    # vetor que guarda os tiros dos monstros
    tiros_monstros = []
    monstros = []
    vel_monstros = 50
    vel_monstros_descida = 500
    cont_monstros = 0
    linha_monstros = int(janela.height / 300)
    coluna_monstros = int(janela.width / 200)


def criarMonstro():
    global cont_monstros
    global monstros
    global dificuldade
    global linha_monstros
    global coluna_monstros
    global pontos_matar_monstro
    pontos_matar_monstro = 1000 * dificuldade
    if (dificuldade > 1 and dificuldade < 4):
        linha_monstros = linha_monstros + dificuldade - 1
        coluna_monstros = coluna_monstros + dificuldade - 1
    monstros = []
    for j in range(linha_monstros):
        linha = []
        for i in range(coluna_monstros):
            cont_monstros = cont_monstros + 1
            linha.append(GameImage("images/monstro.png"))
            linha[i].x = janela.width - janela.width * (97 - i * 10) / 100
            linha[i].y = janela.height - janela.height * (97 - j * 10) / 100
        monstros.append(linha)
    dificuldade += 1


criarMonstro()


def showMonstros():
    # if(dificuldade > 4):
    #    janela.close()
    if cont_monstros == 0:
        criarMonstro()
    for i in range(int(linha_monstros)):
        for j in range(int(coluna_monstros)):
            if monstros[i][j] is not None:
                monstros[i][j].draw()


def desceMonstros():
    global cont_vidas
    for i in range(linha_monstros):
        for j in range(coluna_monstros):
            if monstros[i][j] is not None:
                monstros[i][j].y = monstros[i][j].y + vel_monstros_descida * janela.delta_time() * (dificuldade - 1)
                if (monstros[i][j].collided(nave)) or (monstros[i][j].y + monstros[i][j].width >= nave.y + nave.width):
                    cont_vidas = 0
                    break



def funcionalidadesMonstros():
    global vel_monstros
    global cont_vidas
    # mover a matriz para a direita
    # caso chegue nas extremidades
    # andar para a esquerda e descer uma unidade para baixo
    # mover a matriz para a esquerda
    # caso chegue nas extremidades
    # andar para a direita e descer uma unidade para baixo
    for i in range(linha_monstros):
        for j in range(coluna_monstros):
            if monstros[i][j] != None:
                monstros[i][j].x = monstros[i][j].x + (vel_monstros * janela.delta_time()) * (dificuldade)
                if monstros[i][j].x > janela.width:
                    monstros[i][j].x = monstros[i][j].width*(-1)
                    monstros[i][j].y = monstros[i][j].y + vel_monstros_descida * janela.delta_time() * (dificuldade)
                    if (monstros[i][j].collided(nave)) or (monstros[i][j].y + monstros[i][j].width >= nave.y + nave.width):
                        cont_vidas = 0
                        break
                #if (monstros[i][j].x + monstros[i][j].width > janela.width):
                #   desceMonstros()

# fim dos monstros

def matarMonstro():
    global cont_monstros
    global pontuacao
    for i in range(linha_monstros):
        for j in range(coluna_monstros):
            for k in range(len(tiros)):
                if monstros[i][j] is not None:
                    if monstros[i][j].collided(tiros[k]):
                        monstros[i][j] = None
                        cont_monstros = cont_monstros - 1
                        if tempo > 20:
                            pontuacao += 100
                        pontuacao += pontos_matar_monstro / tempo
                        tiros.pop(k)


# Tiros
vel_tiros = 450
cont_tempo = tempo_recarga = 0.9
cont_tempo_monstro = 0
tempo_recarga_monstro = 2.5


def getTiros():
    elemento = GameImage("images/tiro.png")
    elemento.x = nave.x + (nave.width / 2)
    elemento.y = nave.y - (nave.height / 2)
    tiros.append(elemento)


def getTirosMonstros():
    # global tiros_monstr os

    # posicao na matriz do inimigo aleatorio
    i = int(random.random() * linha_monstros)
    j = int(random.random() * coluna_monstros)
    if monstros[i][j] is not None:
        elemento = GameImage("images/tiro.png")
        elemento.x = monstros[i][j].x + (monstros[i][j].width / 2)
        elemento.y = monstros[i][j].y - (monstros[i][j].height / 2)
        tiros_monstros.append(elemento)


def tirosFuncionalidade():
    for i in range(qtd_elementos):
        tiros[i].draw()
    for i in range(qtd_elementos):
        tiros[i].y = tiros[i].y - vel_tiros * janela.delta_time()
    for i in range(qtd_elementos - 1):
        if (tiros[i].y < 0):
            tiros.pop(i)


# fim dos tiros

def tirosMonstrosFuncionalidade():
    global cont_vidas
    for i in range(qtd_elementos_tiros_monstros):
        tiros_monstros[i].draw()
    for i in range(qtd_elementos_tiros_monstros):
        tiros_monstros[i].y = tiros_monstros[i].y + vel_tiros * janela.delta_time()

    for i in range(qtd_elementos_tiros_monstros):
        # print(tiros_monstros[i])
        if (tiros_monstros[i].collided(nave)):
            tiros_monstros.pop(i)
            cont_vidas = cont_vidas - 1

    for i in range(qtd_elementos_tiros_monstros - 1):
        if (tiros_monstros[i].y + tiros_monstros[i].height > janela.height):
            tiros_monstros.pop(i)


def getFps():
    num = int(clock.get_fps())
    if (num == 0):
        num1 = 0
        num2 = 0
    else:
        num1 = math.floor(num / 10)
        num2 = num - num1 * 10
    janela.draw_text("INIMIGOS: " + str(cont_monstros), janela.width - janela.width * (15 / 100),
                     janela.height - janela.height * (15 / 100), size=15, color=(220, 220, 220), font_name="Arial",
                     bold=True, italic=False)
    janela.draw_text("PONTUAÇÃO: " + str(int(pontuacao)), janela.width - janela.width * (95 / 100),
                     janela.height - janela.height * (15 / 100), size=15, color=(220, 220, 220), font_name="Arial",
                     bold=True, italic=False)
    janela.draw_text("VIDAS: " + str(int(cont_vidas)), janela.width - janela.width * (95 / 100),
                     janela.height - janela.height * (20 / 100), size=15, color=(220, 220, 220), font_name="Arial",
                     bold=True, italic=False)
    clock.tick(60)
    numbers[num1].set_position(15, 20)
    numbers[num2].set_position(30, 20)
    numbers[num1].draw()
    numbers[num2].draw()
    # num2 = num-
    # numbers[8].draw()


def main():
    global tempo
    global cont_tempo
    global cont_tempo_monstro
    global frame

    while frame == 1:
        global qtd_elementos_tiros_monstros
        global qtd_elementos
        tempo += janela.delta_time()
        qtd_elementos = len(tiros)
        qtd_elementos_tiros_monstros = len(tiros_monstros)
        background.draw()
        nave.draw()
        showMonstros()
        funcionalidadesMonstros()
        if (teclado.key_pressed("SPACE") and cont_tempo >= tempo_recarga):
            cont_tempo = 0
            getTiros()
        if (dificuldade > 2):
            cont_tempo += janela.delta_time() * (dificuldade - 2)
        else:
            cont_tempo += janela.delta_time() * (dificuldade - 1)

        cont_tempo_monstro += janela.delta_time()
        if (cont_tempo_monstro >= tempo_recarga_monstro):
            cont_tempo_monstro = 0
            getTirosMonstros()
        tirosFuncionalidade()
        tirosMonstrosFuncionalidade()

        # movimento da nave
        if (teclado.key_pressed("RIGHT") and nave.x + 1 + nave.width < janela.width):  # Direcional \/
            nave.x = nave.x + vel_nave * janela.delta_time() * (dificuldade - 1)
        if (teclado.key_pressed("LEFT") and nave.x - 1 > 0):  # Direcional
            nave.x = nave.x - vel_nave * janela.delta_time() * (dificuldade - 1)

        matarMonstro()
        if (cont_vidas <= 0):
            gameOver()
        getFps()
        janela.update()
menu()
gravarPontuacao()
