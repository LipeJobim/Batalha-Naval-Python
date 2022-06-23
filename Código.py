from random import *
import time

# Mostra Tabuleiro Aberto
def mostrartabuleiro(abrir):
    print(             )
    print("  |",1,2,3,4,5,6,7)
    print("--+--------------")
    for i in range(0, 7):
        print(i +1,"| ",end="")
        for j in range(0, 7):
            if abrir:
                print( str(matriz[i][j]) + " ", end="")
            else:
                if matriz[i][j] == "N":
                    print("0" + " ", end="")
                else:
                    print(str(matriz[i][j]) + " ", end="")
        print("")

# Sorteia navios
def inserirNavios():
    cont = 1
    while (cont <= 10):
        lin = randint (0, 6)
        col = randint (0, 6)
        if matriz[lin][col] != "N":
            matriz[lin][col] = "N"
            cont += 1

# Verificar jogada
def atirar(lin, col):
    if matriz[lin - 1][col - 1] == 0:
        matriz[lin - 1][col - 1] = "X"
        return "0"
    elif matriz[lin - 1][col - 1] == "N":
        matriz[lin - 1][col - 1] = "*"
        return "1"
    else:
        return "2"

def jaAcertou():
    print("Você já atirou neste espaço atire novamente")

# BLOCO PRINCIPAL
JogarNovamente = "s"
while (JogarNovamente == "s"):

    numeros = ["1", "2", "3", "4", "5", "6", "7"]
    tiros = 25
    navios = 10
    acertos = 0
    matriz = [[0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0]]

    print("=" * 20)
    print("BATALHA NAVAL")
    print("=" * 20)
    print("REGRAS:")
    print("A: O jogo é composto por 7 linhas ( _ ) e 7 colunas ( | ), escolha valores de (1 a 7).")
    print("B: O jogo acaba ao destruir os 10 navios ou terminar os 25 tiros.")
    print("=" * 20)

    print("BOA SORTE!!!")
    print("vc tem", tiros, "tiros para acertar ", navios, "navios")

    time.sleep(0.5)

    inserirNavios()
    mostrartabuleiro(True)

    time.sleep(0.5)

    while tiros > 0:

        tiro = ""
        while tiro == "":

            linha = int
            coluna = int

            resp1 = ""
            while resp1 == "" or 0:
                resp1 = (input("selecionar linha: "))
                if resp1 in numeros:
                    linha = int(resp1)
                else:
                    print("valor nao encontrado, tente novamente")
                    resp1 = ""

            resp2 = ""
            while resp2 == "" or 0:
                resp2 = (input("selecionar coluna: "))
                if resp2 in numeros:
                    coluna = int(resp2)
                else:
                    print("valor nao encontrado, tente novamente")
                    resp2 = ""

            tiro = atirar(linha, coluna)

        if tiro == "2":
            jaAcertou()

        if tiro =="0":
            tiros -= 1
            print("Você acertou a água, restaram", tiros, "tiros e",navios,"navios")

        elif tiro == "1":
            tiros -= 1
            navios -= 1
            acertos += 1
            print("Você acertou um návio, você tem", acertos, "acertos")
            print("restaram", tiros, "tiros", "e", navios, "navios")

        if tiros == 0:
            print("="*20)
            print("GAME OVER")
            print("Seus tiros acabaram, você destruiu", acertos, "navios de 10.")
            print("=" * 20)
            break
        elif navios == 0:
            print("="*20)
            print("Você destruiu todos os návios, PARABÉNS")
            print("="*20)
            break

        # novo jogo
        mostrartabuleiro(False)

    JogarNovamente = str(input("Para jogar novamnete clique (s) se não quiser mais jogar clique (n):"))
