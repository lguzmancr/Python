
import random

Deck = [['H','2'],['H','3'],['H','4'],['H','5'],['H','6'],['H','7'],['H','8'],['H','9'],['H','10'],['H','J'],['H','Q'],['H','K'],['H','A'],
 ['D','2'],['D','3'],['D','4'],['D','5'],['D','6'],['D','7'],['D','8'],['D','9'],['D','10'],['D','J'],['D','Q'],['D','K'],['D','A'],
 ['C','2'],['C','3'],['C','4'],['C','5'],['C','6'],['C','7'],['C','8'],['C','9'],['C','10'],['C','J'],['C','Q'],['C','K'],['C','A'],
 ['S','2'],['S','3'],['S','4'],['S','5'],['S','6'],['S','7'],['S','8'],['S','9'],['S','10'],['S','J'],['S','Q'],['S','K'],['S','A']
 ]

Suit = {'H':'Hearts', 'D':'Diamonds', 'C':'Clovers', 'S':'Spades'}

manoPlayer = []
contPlayer = 0
manoDealer = []
contDealer = 0
cardsLeft = 52
while True:
    
    if cardsLeft == 0:
        break
    else:
        pos = random.randint(0,cardsLeft-1)
        carta = Deck.pop(pos)
       # print "popping card pos", pos
        if cardsLeft % 2 == 0:
            manoPlayer.append(carta)
        #    print 'cardsLeft is',cardsLeft,'assigned to Player\n'
        else:
            manoDealer.append(carta)
         #   print 'cardsLeft is',cardsLeft,'assigned to Dealer\n'
    
    cardsLeft -= 1
        


# In[85]:

for card in manoPlayer:
    if card in manoDealer:
        msg = 'sí'
    else:
        msg = 'no'
        
    print "Carta ", card, msg, "existe en manoDealer"
    
    palo = Suit[card[0]]
    valor = card[1]
    if valor in ['J','Q','K']:
        num = 10
    elif valor == 'A':
        num = 11
    else:
        num = int(valor)
    
    print "La carta tiene valor de", num, "y es el palo",palo,"\n"

print len(manoPlayer)
print len(manoDealer)
