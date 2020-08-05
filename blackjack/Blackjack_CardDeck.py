# Name: Niall Joseph
# Program: A deck of cards class..
# Date: 3/3/20
# Description:  Each Card is an object with a value and a suit, and can be
#           drawn on a graphics windows. Each deck starts with 52 cards and can have cards taken
#           from the top, cut, and shuffled
from graphics import *
from random import *


class Card:
    #Initializes the class
    def __init__(self,value,suit):
        #Sets self.value and self.suit equal to the input values.
        self.value = value
        self.suit = suit
    #getter to return value
    def getValue(self):
        return self.value
    #getter to return suit
    def getSuit(self):
        return self.suit
    #Uses graphics to draw the card
    def draw(self,win,center,width,height):
        #Sets the corners using the center and width and height.
        cornerTL = Point(center.getX() - (width/2), center.getY() + (height/2))
        cornerBR = Point(center.getX() + (width/2), center.getY() - (height/2))
        #Makes the background of the card
        cardBase = Rectangle(cornerTL, cornerBR)
        cardBase.setFill("White")
        cardBase.draw(win)
        #sets cardval and cardsuit equal to self.value and self.suit
        cardVal = self.value
        cardSuit = self.suit
        #Makes text for the value and suit
        card_Val = Text(center, cardVal)
        card_Suit1 = Text(Point(cornerBR.getX() - (width/6), cornerBR.getY() + (height/6)), cardSuit)
        card_Suit2 = Text(Point(cornerTL.getX() + (width/6), cornerTL.getY() - (height/6)), cardSuit)
        #Changes the text size depending on card size
        size = round(width * height / 110)
        if size > 36:
            size = 36
        card_Val.setSize(size)
        card_Suit1.setSize(round((2 / 3) * size))
        card_Suit2.setSize(round((2 / 3) * size))
        #Sets hearts and diamonds red and spades and clubs black.
        if cardSuit == "♥" or cardSuit == "♦":
            card_Val.setTextColor("Red")
            card_Suit1.setTextColor("Red")
            card_Suit2.setTextColor("Red")
        if cardSuit == "♠" or cardSuit == "♣":
            card_Val.setTextColor("Black")
            card_Suit1.setTextColor("Black")
            card_Suit2.setTextColor("Black")
        #Draws the value and suit.
        card_Val.draw(win)
        card_Suit1.draw(win)
        card_Suit2.draw(win)
    #When the card object is printed, states what the suit and value is.
    #Converts symbols to words
    def __str__(self):
        if self.suit == "♥":
            suit = "Hearts"
        elif self.suit == "♦":
            suit = "Diamonds"
        elif self.suit == "♠":
            suit = "Spades"
        elif self.suit == "♣":
            suit = "Clubs"
        if self.value == "A":
            val = "Ace"
        elif self.value == "J":
            val = "Jack"
        elif self.value == "K":
            val = "King"
        elif self.value == "Q":
            val = "Queen"
        else:
            val = self.value
        #Returns in the format of "Value of Suit"
        return val + " of " + suit

#Deck class.
class Deck:
    #Initializes the deck with a list of cards with each number and suit combo.
    def __init__(self):
        self.deck = []
        for val1 in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]:
            for suit1 in ["♥","♦","♠","♣"]:
                self.deck.append(Card(val1, suit1))
    #Returns the first element of the deck list and removes it.
    def getTopCard(self):
        card = self.deck.pop(0)
        return card
    #Returns the length of the deck.
    def getCardsLeft(self):
        return len(self.deck)
    #Cuts the deck
    def cutDeck(self,n):
        #Makes placeholder lists.
        numList = []
        placeholderDeck = []
        #Makes a list of length n
        for i in range(n):
            numList.append(i)
        #Reverses the list.
        numList.reverse()
        #Goes through the reverse number list and takes that element of the list and removes it
        #from the main deck and adds it to the back of the placeholder deck.
        for i in numList:
            placeholderDeck.append(self.deck.pop(i))
        #reverses the placeholder deck.
        placeholderDeck.reverse()
        #Adds the placeholderdeck to the end of the deck.
        for i in placeholderDeck:
            self.deck.append(i)
    #Takes a random card in the deck and adds it to the end of the deck.
    #Repeats 100,000 times in order to be more random
    def shuffle(self):
        for i in range(100000):
            self.deck.append(self.deck.pop(randint(0, 51)))
    #Returns nothing when printing the deck.
    def __str__(self):
        return ""



