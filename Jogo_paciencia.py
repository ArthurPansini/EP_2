import random

def cria_baralho():
    listabaralho = ['A♠','2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','Q♠','K♠','A♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥','A♦','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','Q♦','K♦','A♣','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','Q♣','K♣']
    return listabaralho

def extrai_naipe (carta):
    if '♦' in carta:
        return '♦'
    elif '♥' in carta:
        return '♥'
    elif '♣' in carta:
        return '♣'
    else:
        return '♠'

def extrai_valor(carta1):
    
    if len(carta1) == 2:
        valor = carta1[0]
        
    else:
        valor = carta1 [0] + carta1[1]
    return valor

def lista_movimentos_possiveis(listadebaralho,indice):
    cartas = []
    if indice == 0:
        return []
    else:
        if extrai_naipe(listadebaralho[indice]) in listadebaralho[indice-1] or extrai_valor(listadebaralho[indice]) in listadebaralho[indice-1]:
            cartas.append(1)

        if indice>2:
            if extrai_naipe(listadebaralho[indice]) in listadebaralho[indice-3] or extrai_valor(listadebaralho[indice]) in listadebaralho[indice-3]:
                cartas.append(3)
        
    return cartas

def empilha(lista, posO, posD):
    lista[posD] = lista[posO]
    del lista[posO]
    return lista

def possui_movimentos_possiveis(listastr):
    for indice in range(1,len(listastr)):
        if extrai_naipe(listastr[indice]) == extrai_naipe(listastr[indice-1]) or  extrai_valor(listastr[indice]) == extrai_valor(listastr[indice-1]) or indice >= 3 and (extrai_naipe(listastr[indice]) == extrai_naipe(listastr[indice-3]) or  extrai_valor(listastr[indice]) == extrai_valor(listastr[indice-3])):
            return True

    else:
        return False

print("Paciência Acordeão\n") 
print("==================\n")

print("Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.\n") 

print("Existem apenas dois movimentos possíveis:\n") 

print("1. Empilhar uma carta sobre a carta imediatamente anterior;\n") 
print("2. Empilhar uma carta sobre a terceira carta anterior.\n") 

print("Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:\n")

print("1. As duas cartas possuem o mesmo valor ou\n")
print("2. As duas cartas possuem o mesmo naipe.\n")

print("Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.\n")

#print("Aperte [Enter] para iniciar o jogo...\n")

iniciar = input("Aperte [Enter] para iniciar o jogo...")

print('O estado atual do baralho é:\n' )

resposta = 'sim'
while resposta == "sim":
    baralho = cria_baralho()
    embaralhando = (random.sample(baralho, 52))
    possivel = [1] # inicializando possivel
    while possui_movimentos_possiveis(embaralhando) != False:
        for i in range (len(embaralhando)):

            if (len(possivel)!= 0):
                print ('{0}. {1}'.format(i+1, embaralhando[i]))

        escolhercarta = input('Escolha uma carta (digite um número entre 1 e {}):'.format(len(embaralhando)))
        while escolhercarta.isnumeric() == False or int(escolhercarta) > len(embaralhando) or int(escolhercarta) < 1 :
            escolhercarta = input('Você digitou um termo inválido. Escolha uma carta (digite um número entre 1 e 52):')
        
        escolhercarta = int(escolhercarta)

        possivel = lista_movimentos_possiveis(embaralhando, escolhercarta - 1)
        if len(possivel) == 0:
            print('A carta {} não pode ser movida.'.format(embaralhando[escolhercarta - 1]))
            
        elif len(possivel) == 2:
            print('Sobre qual carta você quer empilhar o {}?'.format(embaralhando[escolhercarta - 1]))
            print('{0}. {1}'.format(1, embaralhando[escolhercarta - 2]))
            print('{0}. {1}'.format(2, embaralhando[escolhercarta - 4]))
            escolha2 = ""
            while escolha2 != '1' and escolha2 != '2':
                    escolha2 = input('Digite o número de sua escolha (1 ou 2): ')
                    if escolha2 == '1':
                        embaralhando = empilha(embaralhando, escolhercarta-1, escolhercarta-2)
                        print('o estado atual do baralho é:')
                    elif escolha2 == '2':
                        embaralhando = empilha(embaralhando, escolhercarta-1, escolhercarta-4)
                        print('o estado atual do baralho é:')
                    else:
                        print('Escolha inválida!')
                        print("Escolha sobra qual carta você que empilhar o {}".format(embaralhando[escolhercarta-1]))
                        print('{0}. {1}'.format(1, embaralhando[escolhercarta-2]))
                        print('{0}. {1}'.format(2, embaralhando[escolhercarta-4]))

        elif len(possivel) == 1:
            if possivel == [1]:
                embaralhando = empilha(embaralhando, escolhercarta-1, escolhercarta-2)
                print('o estado atual do baralho é:')
            else:
                embaralhando = empilha(embaralhando, escolhercarta-1, escolhercarta-4)
                print('o estado atual do baralho é:')

        possui_movimentos_possiveis(embaralhando) == False
    if len(embaralhando) == 1:
        print('Parabéns você ganhou!')
        resposta = input('Você quer jogar novamente? (sim ou não) ')
    else:
        print('Que pena, você perdeu!')
        resposta = input('Você quer jogar novamente? (sim ou não) ')
        





    
        