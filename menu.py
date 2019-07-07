
from jogo import janela
from jogo import frame





def menu():

    while True:
        background.draw()
        if mouse.is_over_object(bt_jogar):
            bt_jogar = GameImage("images/play-on-hover.png")
            bt_jogar.x = x
            bt_jogar.y = y
        else:
            bt_jogar = GameImage("images/play.png")
            bt_jogar.x = x
            bt_jogar.y = y
        bt_jogar.draw()

        if mouse.is_over_object(bt_dificuldade):
            bt_dificuldade = GameImage("images/dificuldade-on-hover.png")
            bt_dificuldade.x = x - 40
            bt_dificuldade.y = y + 50
        else:
            bt_dificuldade = GameImage("images/dificuldade.png")
            bt_dificuldade.x = x - 40
            bt_dificuldade.y = y + 50
        bt_dificuldade.draw()

        if mouse.is_over_object(bt_configuracoes):
            bt_configuracoes = GameImage("images/configuracoes-on-hover.png")
            bt_configuracoes.x = x - 55
            bt_configuracoes.y = y + 50*2
        else:
            bt_configuracoes = GameImage("images/configuracoes.png")
            bt_configuracoes.x = x - 55
            bt_configuracoes.y = y + 50*2
        bt_configuracoes.draw()

        if mouse.is_over_object(bt_sair):
            bt_sair = GameImage("images/sair-on-hover.png")
            bt_sair.x = x + 5
            bt_sair.y = y + 50*3
        else:
            bt_sair = GameImage("images/sair.png")
            bt_sair.x = x + 5
            bt_sair.y = y + 50*3
        bt_sair.draw()
        getUserOptions()
        janela.update()
