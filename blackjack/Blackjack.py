# Name: Niall Joseph
# Program: Blackjack. A class with blackjack enabling functions and a main function
#           where you play blackjack
# Date: 3/3/20
# Description: Plays a game of blackjack using various methods of a player class. Some changes.
#               Ace is always 11. Getting 2 aces is double blackjack and you win 3 times your bet.
#               You automatically stand after hitting 3 times.

#Imports the card deck.
from Blackjack_CardDeck import *
from graphics import *
from random import *


class Player:
    #Intializes the player with money, a value(The combined value of their current hand)
    #And the deck they are using.
    def __init__(self, money, value, deck):
        #Initializes various neccessary variable.
        self.money = money
        self.value = value
        self.deck = deck
        self.over = True
        self.bet = 0
    #Getter that returns hand value
    def getValue(self):
        return self.value
    #Getter that returns money
    def getMoney(self):
        return self.money
    #Getter that returns current deck
    def getDeck(self):
        return self.deck
    #Getter that returns the value of boolean variable self.over
    def gameState(self):
        return self.over

    #Draws buttons for hitting and standing, as well as the exiting text at the end.
    #Variables for _____1 are for button 1, and _______2 is for button 2.
    def buttons(self, win, center1, width1, height1, center2, width2, height2):
        #Creates the corners of the buttons
        cornerTL1 = Point(center1.getX() - (width1/2), center1.getY() + (height1/2))
        cornerBR1 = Point(center1.getX() + (width1/2), center1.getY() - (height1/2))
        cornerTL2 = Point(center2.getX() - (width2/2), center2.getY() + (height2/2))
        cornerBR2 = Point(center2.getX() + (width2/2), center2.getY() - (height2/2))
        #Creates and draws the buttons.
        hitButton = Rectangle(cornerTL1, cornerBR1)
        standButton = Rectangle(cornerTL2, cornerBR2)
        hitButton.setFill(color_rgb(91, 133, 92))
        standButton.setFill(color_rgb(91, 133, 92))
        hitButton.draw(win)
        standButton.draw(win)
        #If the game is over. (When game is over, Over = False)
        if not(self.over):
            #Makes the buttons label yes and no
            contText = Text(center1, "Yes")
            exitText = Text(center2, "No")
            exitText.setSize(36)
            contText.setSize(36)
            contText.draw(win)
            exitText.draw(win)
        else:
            #Labels the buttons hit and stand
            hitText = Text(center1, "Hit")
            standText = Text(center2, "Stand")
            hitText.setSize(36)
            standText.setSize(36)
            hitText.draw(win)
            standText.draw(win)
        while True:
            #Depending on where you click (Which button) returns True or False.
            click = win.getMouse()
            pointX = click.getX()
            pointY = click.getY()
            if pointY <= cornerTL1.getY() and pointY >= cornerBR2.getY():
                if pointX >= cornerTL1.getX() and pointX <= cornerBR1.getX():
                    return True
                elif pointX >= cornerTL2.getX() and pointX <= cornerBR2.getX():
                    return False
    #Draws a card flipped over.
    def drawFlipped(self,win,center,width,height):
        #Creates the 4 corners of the card
        cornerTL = Point(center.getX() - (width/2), center.getY() + (height/2))
        cornerBR = Point(center.getX() + (width/2), center.getY() - (height/2))
        cornerTR = Point(center.getX() + (width/2), center.getY() + (height/2))
        cornerBL = Point(center.getX() - (width/2), center.getY() - (height/2))
        #Draws the inner background and the border
        cardInner = Rectangle(Point(cornerTL.getX() + (width/12), cornerTL.getY() - (height/12)), Point(cornerBR.getX() - (width/12), cornerBR.getY() + (height/12)))
        cardInner.setFill(color_rgb(72,92,235))
        cardBorder = Rectangle(cornerTL, cornerBR)
        cardBorder.setFill("White")
        cardBorder.draw(win)
        cardInner.draw(win)
        #Draws each suit in each corner of the card for decoration.
        card_Suit1 = Text(Point(cornerBR.getX() - (width/4), cornerBR.getY() + (height/4)), "♥")
        card_Suit2 = Text(Point(cornerTL.getX() + (width/4), cornerTL.getY() - (height/4)), "♦")
        card_Suit3 = Text(Point(cornerBL.getX() + (width/4), cornerBL.getY() + (height/4)), "♠")
        card_Suit4 = Text(Point(cornerTR.getX() - (width/4), cornerTR.getY() - (height/4)), "♣")
        card_Suit1.setTextColor("Red")
        card_Suit2.setTextColor("Red")
        card_Suit3.setTextColor("Black")
        card_Suit4.setTextColor("Black")
        #Scales text size based on card size
        size = round(width * height / 110)
        if size > 36:
            size = 36
        card_Suit1.setSize(round((2 / 3) * size))
        card_Suit2.setSize(round((2 / 3) * size))
        card_Suit3.setSize(round((2 / 3) * size))
        card_Suit4.setSize(round((2 / 3) * size))
        #Draws the suits
        card_Suit1.draw(win)
        card_Suit2.draw(win)
        card_Suit3.draw(win)
        card_Suit4.draw(win)

    #Returns the blackjack value depending on what the value of the card is
    def evaluate(self,val):
        if val == "A":
            return 11
        elif val == "J" or val == "K" or val == "Q":
            return 10
        else:
            return int(val)

    #Makes buttons to bet.
    #______X is for buttonx
    def makeBet(self, win, center1, width1, height1, center2, width2, height2, center3, width3, height3):
        #Sets the corners of each of the buttons depending on the centers, heights, and width
        cornerTL1 = Point(center1.getX() - (width1/2), center1.getY() + (height1/2))
        cornerBR1 = Point(center1.getX() + (width1/2), center1.getY() - (height1/2))
        cornerTL2 = Point(center2.getX() - (width2/2), center2.getY() + (height2/2))
        cornerBR2 = Point(center2.getX() + (width2/2), center2.getY() - (height2/2))
        cornerTL3 = Point(center3.getX() - (width3/2), center3.getY() + (height3/2))
        cornerBR3 = Point(center3.getX() + (width3/2), center3.getY() - (height3/2))
        #Draws the buttons with their labels
        plusButton = Rectangle(cornerTL1, cornerBR1)
        minusButton = Rectangle(cornerTL2, cornerBR2)
        betButton = Rectangle(cornerTL3, cornerBR3)
        plusButton.setFill(color_rgb(91, 133, 92))
        minusButton.setFill(color_rgb(91, 133, 92))
        betButton.setFill(color_rgb(91, 133, 92))
        plusButton.draw(win)
        minusButton.draw(win)
        betButton.draw(win)
        plusText = Text(center1, "+50")
        minusText = Text(center2, "-50")
        betText = Text(center3, "Bet")
        #States how much money you have left
        totalText = Text(Point(center3.getX(), center3.getY() - (height3)), "Money Left: $" + str(self.money))
        #If your current bet is more than your money sets it to your money.
        #(If you made a big bet previously then lost)
        if self.bet > self.getMoney():
            self.bet = self.getMoney()
        #Draws the current bet amount
        betAmt = Text(Point(center3.getX(), center3.getY() + (height3)), "$" + str(self.bet))
        betAmt.setSize(36)
        betAmt.draw(win)
        #Makes the text sizes bigger than draws them.
        plusText.setSize(36)
        minusText.setSize(36)
        betText.setSize(36)
        totalText.setSize(36)
        plusText.draw(win)
        minusText.draw(win)
        betText.draw(win)
        totalText.draw(win)
        #While loop until betting is done
        while True:
            #Depending on where you click (Which button) does different things.
            click = win.getMouse()
            pointX = click.getX()
            pointY = click.getY()
            if pointY <= cornerTL1.getY() and pointY >= cornerBR3.getY():
                #Does not add more if you do not have the money to bet that much
                if pointX >= cornerTL1.getX() and pointX <= cornerBR1.getX() and self.money - self.bet > 0:
                    self.bet += 50
                    betAmt.undraw()
                    betAmt = Text(Point(center3.getX(), center3.getY() + (height3)), "$" + str(self.bet))
                    betAmt.setSize(36)
                    betAmt.draw(win)
                #Does not let you bet negative
                elif pointX >= cornerTL2.getX() and pointX <= cornerBR2.getX() and self.bet > 0:
                    self.bet -= 50
                    betAmt.undraw()
                    betAmt = Text(Point(center3.getX(), center3.getY() + (height3)), "$" + str(self.bet))
                    betAmt.setSize(36)
                    betAmt.draw(win)
                #You can not bet if your bet is 0
                elif pointX >= cornerTL3.getX() and pointX <= cornerBR3.getX() and self.bet != 0:
                    break
    #Runs through a full turn of the game (1 hand)
    def turn(self):
        #Creates the Bet GUI then makes the bet.
        betGUI = GraphWin("Bet", 720, 400)
        betGUI.setCoords(-600, -800, 600, 800)
        betGUI.setBackground(color_rgb(71, 113, 72))
        self.makeBet(betGUI, Point(-300, 0), 300, 500, Point(300, -0), 300, 500, Point(0, 0), 300, 500)
        betGUI.close()
        #Sets the game to not over
        self.over = True
        if True:
            #Gets the top 4 cards. Draws the first dealer card, and both of the player cards face up. the 2nd dealer card is face down.
            dealer1GUI = GraphWin("Dealer Card 1", 200, 280)
            dealer1 = self.deck.getTopCard()
            dealer1.draw(dealer1GUI, Point(100,140), 200, 280)
            dealer2GUI = GraphWin("Dealer Card 2", 200, 280)
            dealer2 = self.deck.getTopCard()
            self.drawFlipped(dealer2GUI, Point(100,140), 200, 280)
            player1GUI = GraphWin("Player Card 1", 200, 280)
            player1 = self.deck.getTopCard()
            player1.draw(player1GUI, Point(100,140), 200, 280)
            player2GUI = GraphWin("Player Card 2", 200, 280)
            player2 = self.deck.getTopCard()
            player2.draw(player2GUI, Point(100,140), 200, 280)
            #Makes a GUI to let you hit and stand (Control the game)
            controlGUI = GraphWin("Control Panel", 720, 400)
            controlGUI.setCoords(-600, -800, 600, 800)
            controlGUI.setBackground(color_rgb(71, 113, 72))
            #Sets your total value to the value of your cards.
            self.value = self.evaluate(player1.getValue()) + self.evaluate(player2.getValue())
            #Sets the value of the dealer to the value of their cards.
            dealerVal = self.evaluate(dealer1.getValue()) + self.evaluate(dealer2.getValue())
            #Makes a boolean for whether you are standing or not
            stand = False
            #Counter variables for amount of times that they have hit
            hit = 0
            dealerHit = 0
            #If their value is not at 21, you can hit or stand
            if self.value < 21:
                #hit. If the button is the hit button:
                if self.buttons(controlGUI, Point(-300, 0), 500, 500, Point(300, -0), 500, 500):
                    #Increases the hit counter
                    hit = 1
                    #Makes a 3rd card
                    player3GUI = GraphWin("Player Card 3", 200, 280)
                    player3 = self.deck.getTopCard()
                    player3.draw(player3GUI, Point(100,140), 200, 280)
                    #Adds the value of the card to the total value
                    self.value += self.evaluate(player3.getValue())
                    if not(self.value > 21):
                        if self.buttons(controlGUI, Point(-300, 0), 500, 500, Point(300, -0), 500, 500):
                            #Increases the hit counter
                            hit = 2
                            #Makes a 4th card
                            player4GUI = GraphWin("Player Card 4", 200, 280)
                            player4 = self.deck.getTopCard()
                            player4.draw(player4GUI, Point(100,140), 200, 280)
                            #Adds the value of the card to the total value
                            self.value += self.evaluate(player4.getValue())
                            if not(self.value > 21):
                                if self.buttons(controlGUI, Point(-300, 0), 500, 500, Point(300, -0), 500, 500):
                                    #Increases the hit counter
                                    hit = 3
                                    #Makes a 5th card
                                    player5GUI = GraphWin("Player Card 5", 200, 280)
                                    player5 = self.deck.getTopCard()
                                    player5.draw(player5GUI, Point(100,140), 200, 280)
                                    #Adds the value of the card to the total value
                                    self.value += self.evaluate(player5.getValue())
                #stand. If the button is the stand button
                if not(self.value > 21):
                    #Reveals the dealers card face up.
                    dealer2.draw(dealer2GUI, Point(100,140), 200, 280)
                    #In Blackjack, the dealer will continue to hit until they reach 17+.
                    while dealerVal < 17:
                        #Adds one to dealer hit everytime the while loop starts.
                        dealerHit += 1
                        #If the dealer has hit 0 times creates a new dealer card and adds its value to the total dealer value
                        if dealerHit == 1:
                            dealer3GUI = GraphWin("Dealer Card 3", 200, 280)
                            dealer3 = self.deck.getTopCard()
                            dealer3.draw(dealer3GUI, Point(100,140), 200, 280)
                            dealerVal += self.evaluate(dealer3.getValue())
                        #If the dealer has hit 1 time creates a new dealer card and adds its value to the total dealer value
                        if dealerHit == 2:
                            dealer4GUI = GraphWin("Dealer Card 4", 200, 280)
                            dealer4 = self.deck.getTopCard()
                            dealer4.draw(dealer4GUI, Point(100,140), 200, 280)
                            dealerVal += self.evaluate(dealer4.getValue())
                        #If the dealer has hit 2 times creates a new dealer card and adds its value to the total dealer value
                        if dealerHit == 3:
                            dealer5GUI = GraphWin("Dealer Card 5", 200, 280)
                            dealer5 = self.deck.getTopCard()
                            dealer5.draw(dealer5GUI, Point(100,140), 200, 280)
                            dealerVal += self.evaluate(dealer5.getValue())
                    #winCondition function is set to the end result of the game.
                    #Money is changed depending on the
                    #If the dealer gets over 21(Bust) the player wins. Doubles your bet
                    if dealerVal > 21:
                        winCondition = "Dealer Bust, Player Win"
                        self.money += self.bet
                        profit = "+" + "$" +  str(self.bet)
                    #If the dealer has a higher value than the palyer, the dealer wins. Lose your bet
                    elif dealerVal > self.value:
                        winCondition = "Dealer Win"
                        self.money -= self.bet
                        profit = "-" + "$" +  str(self.bet)
                    #If the player has a higher value than the dealer, the player wins. Doubles your bet
                    if dealerVal < self.value:
                        winCondition = "Player Win"
                        self.money += self.bet
                        profit = "+" + "$" +  str(self.bet)
                    #If the player has an equal value as the dealer, the dealer pushes. Get your bet back
                    if dealerVal == self.value:
                        winCondition = "Push"
                        profit = "$0"
                else:
                    #If the player gets over 21(Bust) the player loses. Lose your bet.
                    if self.value >= 21:
                        dealer2.draw(dealer2GUI, Point(100,140), 200, 280)
                        winCondition = "Bust, Dealer Win"
                        self.money -= self.bet
                        profit = "-" + "$" +  str(self.bet)
            #If the player gets blackjack, Triples your bet    
            elif self.value == 21:
                dealer2.draw(dealer2GUI, Point(100,140), 200, 280)
                winCondition = "Blackjack, Player Win"
                self.money += 2 * self.bet
                profit = "+" + "$" +  str(self.bet * 2)
            #IF the player gets double blackjack, quadruples your bet
            else:
                dealer2.draw(dealer2GUI, Point(100,140), 200, 280)
                winCondition = "Double Blackjack, Player Win"
                self.money += 4 * self.bet
                profit = "+" + "$" + str(self.bet * 4)
            #Sets over to false.
            self.over = False
            #Stating the end result of the game
            winText = Text(Point(0, 700), winCondition)
            winText.setSize(32)
            winText.draw(controlGUI)
            #Asking whether you would like to continue the game
            exitText = Text(Point(0, 575), "Would you like to continue?")
            exitText.setSize(32)
            exitText.draw(controlGUI)
            #Stating how much you won and how much you have left.
            profitText = Text(Point(0, 450), str(profit) + " You have: $" + str(self.getMoney()))
            profitText.setSize(32)
            profitText.draw(controlGUI)
            #Sets the game state equal to the answer to the player's choice ("Whether you would like to continue or not")
            self.over = not(self.buttons(controlGUI, Point(-300, 0), 500, 500, Point(300, -0), 500, 500))
            #Closes all the windows.
            winText.undraw()
            exitText.undraw()
            dealer1GUI.close()
            dealer2GUI.close()
            player1GUI.close()
            player2GUI.close()
            if hit >= 1:
                player3GUI.close()
            if hit >= 2:
                player4GUI.close()
            if hit == 3:
                player5GUI.close()
            if dealerHit >= 1:
                dealer3GUI.close()
            if dealerHit >= 2:
                dealer4GUI.close()
            if dealerHit == 3:
                dealer5GUI.close()
            controlGUI.close()
            #Refills the deck and shuffles it for the next game.
            self.deck = Deck()
            self.deck.shuffle()
            
    

            
        
def main():
    #Writes instructions
    instructionsGUI = GraphWin("Instructions", 500, 400)
    instructionsGUI.setCoords(-100, -250, 100, 800)
    instructionsGUI.setBackground(color_rgb(111, 153, 112))
    instructions1 = Text(Point(0, 700), "Welcome to Blackjack (Modified)!")
    instructions2 = Text(Point(0, 550), "The goal of the game is to get blackjack while beating the dealer")
    instructions3 = Text(Point(0, 500), "You start by getting 2 cards face up")
    instructions4 = Text(Point(0, 450), "The dealer gets 1 card face up, 1 card face down")
    instructions5 = Text(Point(0, 400), "You have 2 actions, hit or stand")
    instructions6 = Text(Point(0, 350), "Hit means you want another card")
    instructions7 = Text(Point(0, 300), "Stand means you want to check your cards against the dealers")
    instructions8 = Text(Point(0, 250), "Face cards are worth 10, and aces are worth 11. Every other card is worth its number")
    instructions9 = Text(Point(0, 200), "If your first 2 cards total to 21, you get Blackjack, and receive 3 times your bet")
    instructions10 = Text(Point(0, 150), "If your first 2 cards are both aces, you get a Double Blackjack, and receive 4 times your bet")
    instructions11 = Text(Point(0, 100), "If you get above 21 otherwise, you bust, meaning you loose your bet")
    instructions12 = Text(Point(0, 50), "If you get 5 cards without busting, you automatically stand")
    instructions13 = Text(Point(0, 0), "If you beat the dealer, or the dealer busts you receive double your bet")
    instructions14 = Text(Point(0, -50), "If both of your hands are of the same value, you don't win or lose any money")
    instructions15 = Text(Point(0, -100), "If you get a black or double blackjack, you win, even if the dealer has the same or greater")
    instructions16 = Text(Point(0, -150), "You start with $1000")
    instructions17 = Text(Point(0, -200), "Click this window to continue")
    instructions1.draw(instructionsGUI)
    instructions2.draw(instructionsGUI)
    instructions3.draw(instructionsGUI)
    instructions4.draw(instructionsGUI)
    instructions5.draw(instructionsGUI)
    instructions6.draw(instructionsGUI)
    instructions7.draw(instructionsGUI)
    instructions8.draw(instructionsGUI)
    instructions9.draw(instructionsGUI)
    instructions10.draw(instructionsGUI)
    instructions11.draw(instructionsGUI)
    instructions12.draw(instructionsGUI)
    instructions13.draw(instructionsGUI)
    instructions14.draw(instructionsGUI)
    instructions15.draw(instructionsGUI)
    instructions16.draw(instructionsGUI)
    instructions17.draw(instructionsGUI)
    instructionsGUI.getMouse()
    instructionsGUI.close()
    #Creates a new deck and shuffles it.
    deck1 = Deck()
    deck1.shuffle()
    #Creates a new player object with $1000.
    player1 = Player(1000, 0, deck1)
    #While player has more than 0 money, take turns
    while player1.getMoney() > 0:
        player1.turn()
        #If game is over, stop.
        if player1.gameState():
            break
        else:
            #If they have 0 money but want to exit. restart
            if player1.getMoney() == 0:
                main()
    #States the ending money of the player
    completedGUI = GraphWin("Game Complete", 200, 200)
    completedGUI.setCoords(-100, -100, 100, 100)
    completedGUI.setBackground(color_rgb(111, 153, 112))
    complete = Text(Point(0,50),"Game Complete.")
    endMoney = Text(Point(0,0),"You ended on: ")
    moneyEnd = Text(Point(0,-50),"$" + str(player1.getMoney()))
    complete.setSize(24)
    endMoney.setSize(24)
    moneyEnd.setSize(24)
    complete.draw(completedGUI)
    endMoney.draw(completedGUI)
    moneyEnd.draw(completedGUI)
    completedGUI.getMouse()
    completedGUI.close()

    
    

main()


