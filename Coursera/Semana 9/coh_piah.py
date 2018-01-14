"""

Introdução

John é monitor na matéria de Introdução à Produção Textual I na Penn State University (PSU). Durante esse período,
John descobriu que uma epidemia de COH-PIAH estava se espalhando pela PSU. Esses doença rara e altamente contagiosa
faz com que as pessoas contaminadas produzam textos extremamente semelhantes de forma involuntária. Após a entrega da
primeira redação, John desconfiou que alguns alunos estavam sofrendo de COH-PIAH. John, se preocupando com a saúde
da turma, resolveu buscar um método para identificar os casos de COH-PIAH. Para isso, ele necessita da sua ajuda para
desenvolver um programa que o auxilie a identificar os alunos contaminados.
Detecção de autoria

Utilizando diferentes estatísticas do texto, é possível identificar aspectos que funcionam como uma “assinatura” do
autor. Diferentes pessoas possuem diferentes estilos de escrita, algumas preferindo sentenças mais curtas, outras
preferindo sentenças mais longas.

Essas “assinatura” pode ser utilizada para detecção de plágio, evidência forense, ou nesse caso, para detectar a
grave doença COH-PIAH.
Traços linguísticos

Nesse exercício utilizaremos as seguintes estatísticas para detectar a doença:

    Tamanho médio de palavra: Média simples do número de caracteres por palavra.
    Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
    Razão Hapax Legomana: Número de palavras utilizadas uma vez dividido pelo número total de palavras.
    Tamanho médio de sentença: Média simples do número de caracteres por sentença.
    Complexidade de sentença: Média simples do número de frases por sentença.
    Tamanho médio de frase: Média simples do número de caracteres por frase.

Funcionamento do programa

Diversos estudos foram compilados e hoje se conhece precisamente a assinatura de um portador de COH-PIAH. Seu programa
deverá receber diversos textos e calcular os valores dos diferentes traços linguísticos da seguinte forma:

    Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.
    Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras. Por exemplo, na frase
    "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 4 diferentes
    (o, gato, caçava, rato). Nessa frase, a relação Type-Token vale 45=0.8
    Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras. Por
    exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 3 que
    aparecem só uma vez (gato, caçava, rato). Nessa frase, a relação Hapax Legomana vale 35=0.6
    Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de
    sentenças (os caracteres que separam uma sentença da outra não devem ser contabilizados como parte da sentença).
    Complexidade de sentença é o número total de frases divido pelo número de sentenças.
    Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto
    (os caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase).

Após calcular esses valores para cada texto, você deve comparar com a assinatura fornecida para os infectados por
COH-PIAH. O grau de similaridade entre dois textos, a e b, é dado pela fórmula:

Sab=∑i=16||fi,a−fi,b||6

Onde:

    Sab é o grau de similaridade entre os textos a e b;
    fi,a é o valor de cada traço linguístico i no texto a; e
    fi,b é o valor de cada traço linguístico i no texto b.

Perceba que quanto mais similares a e b forem, menor Sab será. Para cada texto, você deve calcular o grau de
similaridade com a assinatura do portador de COH-PIAH e no final exibir qual o texto que mais provavelmente foi
escrito por algum aluno infectado.

Funções de suporte

As seguintes funções devem ser utilizadas no seu programa; algumas já estão implementadas, outras devem ser
implementadas por você. Sinta-se livre para criar funções adicionais, caso necessário. Utilize este esqueleto
como base para começar o seu programa.

Dica: aproveite as funções pré-prontas do esqueleto, como "separa_sentenca", "separa_frase"etc.! Como há mais de
uma maneira de pensar a separação entre frases/palavras/sentenças, usando essas funções você vai fazer o cálculo
da maneira esperada pelo corretor automático.

Cuidado: A função le_textos() considera que um "texto" é uma linha de texto, ou seja, não é possível inserir
parágrafos separados. Se você digitar algum "enter", a função vai entender que você está começando um novo texto.
Preste especial atenção a isso se usar "copiar/colar" para inserir os textos! Note também que, no cálculo de
similaridade, é preciso encontrar o valor absoluto de cada uma das diferenças.

import re

def le_assinatura():
  '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os
   textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas
    assinaturas.'''
    pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    pass

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior
     probabilidade de ter sido infectado por COH-PIAH.'''
    pass

"""

import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada
    com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade
    nas assinaturas.'''
    valorLinguistico = 0

    for i in range(0, 6):
        valor = as_a[i] - as_b[i]

        if (valor < 0):
            valor *= -1

        valorLinguistico += valor

    return valorLinguistico / 6



def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    conjSentencas = separa_sentencas(texto)

    conjFrases = extrai_frases(conjSentencas)

    conjPalavras = extrai_palavras(conjFrases)


    wal = calcula_tamanho_medio_palavra(conjPalavras)
    ttr = calcula_typen_token(conjPalavras)
    hlr = calcula_Hapax_Legomana(conjPalavras)

    sal = calcula_tamanho_medio_sentencas(conjSentencas)
    sac = calcula_complexidade_sentenca(conjFrases, len(conjSentencas))
    pal = calcula_tamanho_medio_frase(conjFrases)

    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior
    probabilidade de ter sido infectado por COH-PIAH.'''

    assinaturas = []
    for te in textos:
        assinaturas.append(calcula_assinatura(te))


    grauSimilaridade = 1000.0
    numTex = -1

    for i in range(0, len(assinaturas)):

        similaridade = compara_assinatura(ass_cp, assinaturas[i])



        if (similaridade < grauSimilaridade):
            grauSimilaridade = similaridade
            numTex = i + 1

    return numTex


def extrai_frases(sentencas):
    frases = []

    for sentenca in sentencas:
        frases += separa_frases(sentenca)

    return frases



def extrai_palavras(sentencas):
    palavras = []

    frases = extrai_frases(sentencas)

    for frase in frases:
        palavras += separa_palavras(frase)

    return palavras



def calcula_tamanho_medio_palavra(palavras):
    tamanho = 0

    for pal in palavras:
        tamanho += len(pal)

    return tamanho / len(palavras)



def calcula_typen_token(palavras):
    numPalavrasDif = n_palavras_diferentes(palavras)

    return numPalavrasDif / len(palavras)



def calcula_Hapax_Legomana(palavras):
    numPalavasUnicas = n_palavras_unicas(palavras)

    return numPalavasUnicas / len(palavras)



def calcula_tamanho_medio_sentencas(sentencas):
    # delimitadores = .!?

    tamanho = 0

    for sentenca in sentencas:
        s = re.sub(r'[.!?]+', "", sentenca)
        tamanho += len(s)

    return tamanho / len(sentencas)



def calcula_complexidade_sentenca(frases, numeroSentencas):
    numFrases = len(frases)

    return numFrases / numeroSentencas



def calcula_tamanho_medio_frase(frases):
    tamanho = 0

    for frase in frases:
        f = re.sub(r'[,:;]+', "", frase)
        tamanho += len(f)

    return tamanho / len(frases)


def main():

    assinaturaPadrao = le_assinatura()

    textos = le_textos()

    numSimilar = avalia_textos(textos, assinaturaPadrao)

    print("O autor do texto {} esta infectado com COH-PIAH".format(numSimilar))


main()