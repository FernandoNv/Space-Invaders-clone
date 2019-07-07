from operator import itemgetter
#from jogo import janela
matriz_pontuacao = []
#pontuacao = 1000
#nome = "Monstro"

def carregarPontuacao():
    nome_arquivo = "pontuacao.txt"
    arquivo = open(nome_arquivo, "r")
    cont_linha = 0
    for texto in arquivo:
        cont_linha += 1
        score, name = texto.split()
        matriz_pontuacao.append([int(score), name])
        if (cont_linha >= 10):
            break
    arquivo.close()

def getPontuacao(pontuacao, nome):
    if pontuacao > matriz_pontuacao[9][0]:
        matriz_pontuacao.append([pontuacao, nome])
    matriz_pontuacao.sort(key=itemgetter(0), reverse=True)
    matriz_pontuacao.pop(10)

def gravarPontuacao():
    nome_arquivo = "pontuacao.txt"
    arquivo = open(nome_arquivo, "w")
    for conteudo in matriz_pontuacao:
        score, name = conteudo[0], conteudo[1]
        arquivo.write(str(score) + " " + name + "\n")
    arquivo.close()

