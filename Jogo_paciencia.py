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