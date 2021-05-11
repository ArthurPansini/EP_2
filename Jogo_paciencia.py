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

print("Aperte [Enter] para iniciar o jogo...\n")
    
        