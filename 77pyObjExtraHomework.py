# Create a deck of cards class. Internally, the deck of cards should use another class, a card class.
#
# Your requirements are: - The Deck class should have a deal method to deal a single card from the deck - After a
# card is dealt, it is removed from the deck. - There should be a shuffle method which makes sure the deck of cards
# has all 52 cards (throws error otherwise) and then rearranges them randomly. - The Card class should have a suit (
# Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K) - The Card class should display it's type
# when printed : e.g. 2 of Diamonds - The Deck class should display only the number of cards there are still in the
# deck when printed.
import random


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def display(self):
        print("{} of {}".format(self.value, self.suit))

    def __repr__(self):
        return f'Card: {self.value} of {self.suit}'


class Deck:

    def __init__(self):
        self.cards = []

    def build(self):
        self.cards = []
        for s in ["hearts", "diamonds", "clubs", "spades"]:
            for v in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                self.cards.append(Card(s, v))

    def deal(self):
        self.cards.pop()

    def display(self):
        print("The number of cards left is : {}".format(len(self.cards)))

    def shuffle(self):
        if not self.cards:
            raise Exception("The deck of cards is empty")
        else:
            random.shuffle(self.cards)

    def __repr__(self):
        return f'Deck of cards: {self.cards}'


deck_of_cards = Deck()  # create the empty deck
# deck_of_cards.shuffle()  # shuffle the deck will raise an error here

deck_of_cards.build()  # fill the deck with cards
deck_of_cards.__repr__()
print(deck_of_cards.cards)

deck_of_cards.shuffle()  # shuffle again
deck_of_cards.__repr__()
print(deck_of_cards.cards)

deck_of_cards.display()  # display method
print(len(deck_of_cards.cards))

deck_of_cards.deal()  # deal method
deck_of_cards.display()
print(len(deck_of_cards.cards))


deck_of_cards.build()  # rebuild
print(len(deck_of_cards.cards))  # again will have 52 cards that needs to be reshuffled
print(deck_of_cards.cards)
