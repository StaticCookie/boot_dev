import random

class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self):
        self.__cards = []
        self.create_deck()

    def create_deck(self):
        for x in range(4):
            for i in range(13):
                self.__cards.append((DeckOfCards.RANKS[i],DeckOfCards.SUITS[x]))

        
    def shuffle_deck(self):
        random.shuffle(self.__cards)
        print(self.__cards)

    def deal_card(self):
        if self.__cards:
            return self.__cards.pop()

    def __str__(self):
        return f"The deck has {len(self.__cards)} cards"
