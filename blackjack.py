import random
import os

class Card:

    def __init__(self, cardFace, value, symbol):
        self.cardFace = cardFace
        self.value = value
        self.symbol = symbol

    
def showCards(cards, hidden):
    s = ''
    for card in cards:
        s = s + '\t ________________'
    if hidden:
        s += '\t ________________'
    print(s)
    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|                |'
    print(s)
    s = ''
    for card in cards:
        if card.cardFace in ['J', 'Q', 'K', 'A']:
            s = s + '\t|  {}             |'.format(card.cardFace)
        elif card.value == 10:
            s = s + '\t|  {}            |'.format(card.value)
        else:
            s = s + '\t|  {}             |'.format(card.value)
    if hidden:
        s += '\t|                |'
    print(s)
    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|      * *       |'
    print(s)
    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|    *     *     |'
    print(s)
    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|   *       *    |'
    print(s)
    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|   *       *    |'
    print(s)
    s = ''
    for card in cards:
        s = s + '\t|       {}        |'.format(card.symbol)
    if hidden:
        s += '\t|          *     |'
    print(s)
    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|         *      |'
    print(s)
    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|        *       |'
    print(s)
    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|                |'
    print(s)
    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|                |'
    print(s)
    s = ''
    for card in cards:
        if card.cardFace in ['J', 'Q', 'K', 'A']:
            s = s + '\t|            {}   |'.format(card.cardFace)
        elif card.value == 10:
            s = s + '\t|           {}   |'.format(card.value)
        else:
            s = s + '\t|            {}   |'.format(card.value)
    if hidden:
        s += '\t|        *       |'
    print(s)
    s = ''
    for card in cards:
        s = s + '\t|________________|'
    if hidden:
        s += '\t|________________|'
    print(s)
    print()

def dealCard(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card, deck
def playBlackjack(deck):
    playerCards = []
    dealerCards = []
    playerScore = 0
    dealerScore = 0
    os.system('clear')
    while len(playerCards) < 2:
        playerCard, deck = dealCard(deck)
        playerCards.append(playerCard)
        playerScore += playerCard.value
        #if dealt a 2nd ace adjust player score
        if len(playerCards) == 2:
            if playerCards[0].value == 11 and playerCards[1].value == 11:
                playerCards[0].value = 1
                playerScore -= 10
        
        print('PLAYER CARDS: ')
        showCards(playerCards, False)
        print("PLAYER SCORE: ", playerScore)

        input("Continue...")

        dealerCard, deck = dealCard(deck)
        dealerCards.append(dealerCard)
        dealerScore += dealerCard.value

        #if dealt a second ace, adjust dealer score
        # Note: asjust 2nd card to hide that the dealer has an ace
        if len(dealerCards) == 2:
            if dealerCards[0].value == 11 and dealerCards[1].value == 11:
                dealerCards[1].value = 1
                dealerScore -= 10
        
        print("DEALER CARDS: ")
        if len(dealerCards) == 1:
            showCards(dealerCards, False)
            print("DEALER SCORE = ", dealerScore)
        else:
            showCards(dealerCards[:-1], True)
            print('DEALER SCORE = ', dealerScore - dealerCards[-1].value)
        
        input("Continue...")

        if playerScore == 21:
            print("PLAYER HAS A BLACKJACK!!!")
            print("PLAYER WINS!!!")
            quit()
        os.system('clear')

        print('DEALER CARDS: ')
        showCards(dealerCards[:-1], True)
        print('DEALER SCORE = ', dealerScore - dealerCards[-1].value)
        print()
        print('PLAYER CARDS: ')
        showCards(playerCards, False)
        print('PLAYER SCORE = ', playerScore)

        while playerScore < 21:
            choice = input('Enter H to Hit or S to Stand: ').upper()
            if len(choice) != 1 or (choice not in ['H', 'S']):
                os.system('clear')
                print('Invalid choice!!! Try again...')
                continue

            if choice.upper() == 'S':
                break
            else:
                playerCard, deck = dealCard(deck)
                playerCards.append(playerCard)
                playerScore += playerCard.value
                cardPos = 0

                #if deal an ace, adjust score for each existing ace in hand
                while playerScore > 21 and cardPos < len(playerCards):
                    if playerCards[cardPos].value == 11:
                        playerCards[cardPos].value = 1
                        playerScore -= 10
                        cardPos += 1
                    else:
                        cardPos += 1
                
                if playerScore > 21:
                    break
            
            os.system('clear')
            print('DEALER CARDS: ')
            showCards(dealerCards[:-1], True)
            print('DEALER SCORE = ', dealerScore - dealerCards[-1].value)
            print()
            print('PLAYER CARDS: ')
            showCards(playerCards, False)
            print('PLAYER SCORE = ', playerScore)
        
        os.system('clear')
        print('PLAYER CARDS: ')
        showCards(playerCards, False)
        print('PLAYER SCORE = ', playerScore)
        print()
        print('DEALER IS REVEALING THEIR CARDS...')
        print('DEALER CARDS: ')
        showCards(dealerCards, False)
        print('DEALER SCORE = ', dealerScore)

        if playerScore == 21:
            print('PLAYER HAS A BLACKJACK, PLAYER WINS!!!')
            quit()
        
        if playerScore > 21:
            print('PLAYER BUSTED!! GAME OVER!!')
            quit()
        
        input('Continue...')
        while dealerScore < 17:
            os.system('clear')
            print('DEALER DECIDES TO HIT...')
            dealerCard, deck = dealCard(deck)
            dealerCards.append(dealerCard)
            dealerScore += dealerCard.value

            #if dealt an ace, fix it blah blah
            cardPos = 0
            while dealerScore > 21 and cardPos < len(dealerCards):
                if dealerCards[cardPos].value == 1:
                    dealerCards[cardPos].value = 1
                    dealerScore -= 10
                    cardPos += 1
                else:
                    cardPos += 1
            
            print("PLAYER CARDS: ")
            showCards(playerCards, False)
            print('PLAYER SCORE = ', playerScore)
            print()
            print('DEALER CARDS: ')
            showCards(dealerCards, False)
            print('DEALER SCORE = ', dealerScore)
            if dealerScore > 21:
                break
            input('Continue...')
            

        if dealerScore > 21:
            print('DEALER BUSTED!! YOU WIN!!')
            quit()
        elif dealerScore == 21:
            print('DEALER HAS A BLACKJACK!!! PLAYER LOSES!!!')
            quit()
        elif dealerScore == playerScore:
            print('TIE GAME!!!')
        elif playerScore > dealerScore:
            print('PLAYER WINS!!!')
        else:
            print('DEALER WINS!!!')

def initDeck():
    suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    #UNICODE calues for card symbol images
    suitSymbols = {'Hearts': '\u2661', 'Diamonds': '\u2662',
                   'Spades': '\u2664', 'Clubs': '\u2667'}
    cards = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
             '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10 }
    deck = []
    for suit in suits:
        for card, value in cards.items():
            deck.append(Card(card, value, suitSymbols[suit]))
    return deck

if __name__ == '__main__':
    deck = initDeck()
    playBlackjack(deck)