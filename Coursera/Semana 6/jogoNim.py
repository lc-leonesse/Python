"""

Você deverá escrever um programa na linguagem Python, versão 3, que permita a uma "vítima" jogar o NIM contra o
computador. O computador, é claro, deverá seguir a estratégia vencedora descrita acima.

Sejam n o número de peças inicial e m o número máximo de peças que é possível retirar em uma rodada. Para garantir que
o computador ganhe sempre, é preciso considerar os dois cenários possíveis para o início do jogo:

    Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o jogador a iniciar a partida;
    Caso contrário, o computador toma a inciativa de começar o jogo.

Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste em deixar sempre um número de peças que seja
múltiplo de (m+1) ao jogador. Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.

Seu trabalho, então, será implementar o Jogo e fazer com que o computador se utilize da estratégia vencedora.

Com o objetivo do EP já definido, uma dúvida que deve surgir nesse momento é como modelar o jogo de forma que possa ser
implementado em Python 3 correspondendo rigorosamente às especificações descritas até agora.

Para facilitar seu trabalho e permitir a correção automática do exercício, apresentamos a seguir um modelo, isto é, uma
descrição em linhas gerais de um conjunto de funções que resolve o problema proposto neste EP. Embora sejam possíveis
outras abordagens, é preciso atender exatamente o que está definido abaixo para que a correção automática do trabalho
funcione corretamente.

O programa deve implementar:

    Uma função computador_escolhe_jogada que recebe, como parâmetros, os números n e m descritos acima e devolve um
    inteiro correspondente à próxima jogada do computador de acordo com a estratégia vencedora.
    Uma função usuario_escolhe_jogada que recebe os mesmos parâmetros, solicita que o jogador informe sua jogada e
    verifica se o valor informado é válido. Se o valor informado for válido, a função deve devolvê-lo; caso contrário,
    deve solicitar novamente ao usuário que informe uma jogada válida.
    Uma função partida que não recebe nenhum parâmetro, solicita ao usuário que informe os valores de n e m e inicia o
    jogo, alternando entre jogadas do computador e do usuário (ou seja, chamadas às duas funções anteriores). A escolha
    da jogada inicial deve ser feita em função da estratégia vencedora, como dito anteriormente. A cada jogada, deve
    ser impresso na tela o estado atual do jogo, ou seja, quantas peças foram removidas na última jogada e quantas
    restam na mesa. Quando a última peça é removida, essa função imprime na tela a mensagem "O computador ganhou!"
    ou "Você ganhou!" conforme o caso.

Observe que, para isso funcionar, seu programa deve sempre "lembrar" qual é o número de peças atualmente no tabuleiro e
qual é o máximo de peças a retirar em cada jogada.

"""


def partida():

    # Solicita ao usuário os valores de n e m:
    n = int(input("Quantas peças? "))
    m = int(input("\nLimite de peças por jogada? "))

    # Define uma variável para controlar a vez do computador:
    vez_computador = True

    # Decide quem iniciará o jogo:
    if n % (m+1) == 0:
        vez_computador = False
        print("\nVocê começa!")
    else:
        vez_computador = True
        print("\nComputador começa!")

    # Execute enquanto houver peças no jogo:
    while n > 0:

        if vez_computador:
            jogada = computador_escolhe_jogada(n, m)
            vez_computador = False
            print("\nComputador retirou", m, "peça(s).")
        else:
            jogada = usuario_escolhe_jogada(n, m)
            vez_computador = True
            print("\nVocê retirou", m, "peça(s).")

        # Retira as peças do jogo:
        n = n - jogada

        # Mostra o estado atual do jogo:
        print("\nAgora resta(m)", n, "peça(s) no tabuleiro")

    # Fim de jogo, verifica quem ganhou:
    if vez_computador:
        print("\nVocê ganhou!")
        return 1
    else:
        print("\nO computador ganhou!")
        return 0


def usuario_escolhe_jogada(n, m):

    # Define o número de peças do usuário:
    jogada = 0

    # Enquanto o número não for válido
    while jogada == 0:

        # Solicita ao usuário quantas peças irá tirar:
        jogada = int(input("\nQuantas peças você vai tirar? "))

        # Condições: jogada < n, jogada < m, jogada > 0
        if jogada > n or jogada < 1 or jogada > m:
            print("Oops! Jogada inválida! Tente de novo.\n")


            # Valor inválido, continue solicitando ao usuário:
            jogada = 0

    # Número de peças válido, então retorne-o:
    return jogada

def computador_escolhe_jogada(n, m):

    # Pode retirar todas as peças?
    if n <= m:

        # Retira todas as peças e ganha o jogo:
        return n

    else:

        # Verifica se é possível deixar uma quantia múltipla de m+1:
        quantidade = n % (m+1)

        if quantidade > 0:
            return quantidade

        # Não é, então tire m peças:
        return m

def campeonato():

    # Pontuações:
    usuario = 0
    computador = 0
    rodada = 1

    while rodada <= 3:
        # Executa a partida:
        print("\n********** Rodada", rodada, "**********\n")
        vencedor = partida()

        # Verifica o resultado, somando a pontuação:
        if vencedor == 1:
            # Usuário venceu:
            usuario = usuario + 1
        else:
            # Computador venceu:
            computador = computador + 1

        rodada = rodada + 1
    # Exibe o placar final:
    print("\n**** Final do campeonato! ****")
    print("\nPlacar: Você", usuario, "X", computador, "Computador")


print("Bem-vindo ao jogo do NIM! Escolha:\n")
escolha = int(input("1 - para jogar uma partida isolada \n2 - para jogar um campeonato "))

if escolha != 1 and escolha != 2:
    print("Escolha inválida. Tente novamente.\n")
    escolha = int(input("1 - para jogar uma partida isolada \n2 - para jogar um campeonato "))
if escolha == 1:
    partida()
elif escolha == 2:
    campeonato()


