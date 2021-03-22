import itertools, copy, re, random, unittest

quitPattern = re.compile('[Y]^', re.I)

class Card:
    def __init__(self):
        cardName = deck.pop(0)
        self.name = 'A {} of {}'.format(cardName[0], cardName[1])
        self.house = cardName[0]
        self.suit = cardName[1]
        if(self.house == 'Ace'):
            self.value = 13
        elif(self.house == 'King'):
            self.value = 12
        elif(self.house == 'Queen'):
            self.value = 11
        elif(self.house == 'Jack'):
            self.value = 10
        elif(self.house == '10'):
            self.value = 9
        elif(self.house == '9'):
            self.value = 8
        elif(self.house == '8'):
            self.value = 7
        elif(self.house == '7'):
            self.value = 6
        elif(self.house == '6'):
            self.value = 5
        elif(self.house == '5'):
            self.value = 4
        elif(self.house == '4'):
            self.value = 3
        elif(self.house == '3'):
            self.value = 2
        elif(self.house == '2'):
            self.value = 1

    def __str__(self):
        return str(self.name)

    def __lt__(self, other):
        return self.value < other.value
    def __gt__(self, other):
        return self.value > other.value
    def __add__(self, other):
        return self.vaue + other.value

class Hand:
    def __init__(self, skill='Player'):
        self.name = random.choice(name)
        self.skill = skill
        self.hand = []
        self.value = 0
        self.draw(5)

    def __str__(self):
        hand = []
        for card in self.hand:
            hand.append(str(card))
        return str(hand)

    def draw(self, amount):
        x = 0
        while x < amount:
            self.hand.append(Card())
            x += 1
        self.hand.sort(reverse=True)
        self.count()

    def discard(self, res=''):
        if(res != ''):
            res = res.split(', ')
            for card in res:
                self.hand.pop(int(card))
            self.draw(len(res))

    def count(self):
        house = []
        suit = []
        result = 0
        discardReccomendations = ''
        for card in self.hand:
            house.append(card.house)
            suit.append(card.suit)
            self.value = self.value + card.value
        house.sort()
        suit.sort()
        #Going to add more logic to take into account flushes and such.
        if(self.value == 64):
            result = 100
            discardReccomendations: 'keep'
        elif(self.value <= 39):
            result = 'ERROR'
            discardReccomendations: 'discard your lowest cards'
        elif(self.value == 11):
            result = 0
            discardReccomendations: 'discard your cards. All of them'
        response = [result, discardReccomendations]
        return response

    def __lt__(self, other):
        return self.value < other.value
    def __gt__(self, other):
        return self.value > other.value
    def __add__(self, other):
        return self.vaue + other.value

def main():
    setup()
    print("This is a game of draw poker.")
    print("You have bet 100$ on this game.")
    print("Don't worry though, you have me.")
    print("A super advanced AI that will make sure you have the highest probability of winning.")

    for game in itertools.count(1):
        #This is where the actual game starts being built.
        hand = Hand()
        enemyOne = Hand(random.choices(skill, weights=(100, 100, 100, 1)))
        enemyTwo = Hand(random.choices(skill, weights=(100, 100, 100, 1)))
        enemyThree = Hand(random.choices(skill, weights=(100, 100, 100, 1)))

        print("You have {}.".format(hand))
        result, discardReccomendations = hand.count()
        print("With a {}% chance of winning with your hand, you should {}.".format(result, discardReccomendations))
        response = input("Please specify which cards you wish to get rid of by numerical ID. ")

        hand.discard(response)
        enemyOne.discard()
        enemyTwo.discard()
        enemyThree.discard()
        hands = [hand, enemyOne, enemyTwo, enemyThree]
        hands.sort()
        if(hands[0] != hand):
            result = 'lost'
        else:
            result = 'won'

        winner = hands[0]

        print("You {} game number {} with your hand of {}. {} beat you with a {}.".format(result, game, hand, winner.name, winner))


        quit = input("Play again? Yes or No. ")

        if(quitPattern.match(quit)):
            break
        else:
            setup()

def setup():
    global deck, skill, name
    suit = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
    house = ['King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2', 'Ace']
    skill = ['Novice', 'Adept', 'Expert', 'Cheater']
    name = ['Bill', 'Steve', 'Jennefer', 'Sean', 'ERROR', 'The Shadow Monster']
    deck = list(itertools.product(house, suit))
    random.shuffle(deck)

main()
