# Name: Niall Joseph & Theodore Chen
# Program: Battleship. Player vs Computer. 3 Difficulties. Replayability.
# Date: 2/9/20
# Description: This program is the game of Battleship. You start by choosing a difficulty, then you
# place down 5 ships with different length, the aircraft carrier (5 spaces), battleship (4),
# submarine (3), destroyer (3), and patrol boat (2). The computer will also place down these same ships randomly.
# Then you may select one of the enemies spaces, and fire. The first to reach 17 wins.
# After completing a game, you may restart or exit.
# 
# Inputs: Player's ship location, Player firing sequence, difficulty, restart.
# Outputs: Computer's ship locations, whether the player hit or missed, who won the game, visual of player's ship location
# Other: Instructions to play the game, score counter
from math import *
from graphics import *
from random import *

#2 sets of 8 lists with 8 values each. The lists contain the states of each position on the board
#There are 4 states, empty, ship, hit, and miss. The game starts with a completely empty board.
columnA = list(["Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"])
columnB = list(["Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"])
columnC = list(["Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"])
columnD = list(["Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"])
columnE = list(["Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"])
columnF = list(["Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"])
columnG = list(["Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"])
columnH = list(["Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"])

columnCompA = list(["Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"])
columnCompB = list(["Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"])
columnCompC = list(["Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"])
columnCompD = list(["Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"])
columnCompE = list(["Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"])
columnCompF = list(["Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"])
columnCompG = list(["Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"])
columnCompH = list(["Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"])

####################################################################
#Defines the main function
def main():
    #Sets a boolean variable game which controls a while loop that contains all the code
    game = True
    while game == True:

####################################################################
        #Creates a new gui called control panel that will control the difficulty
        controlGUI = GraphWin("Control Panel",400,700)
        #Sets the background color to a light blue
        controlBackground = Rectangle(Point(0,0),Point(400,700))
        controlBackground.setFill(color_rgb(0,170,250))
        controlBackground.draw(controlGUI)
        #Creates text that explains what the gui does, and buttons that show the boundries
        #of where the user can click to set the difficulty
        difficultyText = Text(Point(200,65),"Choose a Difficulty: ")
        difficultyText.setSize(18)
        difficultyText.draw(controlGUI)
        easyButton = Rectangle(Point(100,100),Point(300,175))
        easyButton.setFill(color_rgb(0,140,220))
        easyText = Text(Point(200,137.5),"Easy")
        easyText.setSize(20)
        easyButton.draw(controlGUI)
        easyText.draw(controlGUI)
        normalButton = Rectangle(Point(100,200),Point(300,275))
        normalButton.setFill(color_rgb(0,140,220))
        normalText = Text(Point(200,237.5), "Normal")
        normalText.setSize(20)
        normalButton.draw(controlGUI)
        normalText.draw(controlGUI)
        hardButton = Rectangle(Point(100,300),Point(300,375))
        hardButton.setFill(color_rgb(0,140,220))
        hardText = Text(Point(200,337.5), "Hard")
        hardText.setSize(20)
        hardButton.draw(controlGUI)
        hardText.draw(controlGUI)
        #Sets the initial difficulty to None
        difficulty = "None"
        #Loops through until the difficulty variable is changed
        while difficulty == "None":
            #Gets the x and y value of where the user has clicked
            point = controlGUI.getMouse()
            pointX = point.getX()
            pointY = point.getY()
            #Depending on where the X and Y values for the click are, it does certain things
            if pointX >= 100 and pointX <= 300:
                #If located around the easy button and the difficulty is still None...
                if pointY >= 100 and pointY <= 175 and difficulty == "None":
                    #Sets the difficulty to Easy and closes the GUI.
                    difficulty = "Easy"
                    controlGUI.close()
                    break
                #If located around the normal button and the difficulty is still None...
                if pointY >= 200 and pointY <= 275 and difficulty == "None":
                    #Sets the difficulty to Normal and closes the GUI.
                    difficulty = "Normal"
                    controlGUI.close()
                    break
                #If located around the hard button and the difficulty is still None...
                if pointY >= 300 and pointY <= 375 and difficulty == "None":
                    #Sets the difficulty to Hard and closes the GUI.
                    difficulty = "Hard"
                    controlGUI.close()
                    break

    
        
        

####################################################################
        #Creates a gui that gives general instructions.   
        instructionsGUI = GraphWin("Instructions",1000,200)
        instructionsLine1 = Text(Point(500,80),"Battleship is a game where each player has ships. Place your ships with the arrow keys and use r to rotate")
        instructionsLine1.setSize(16)
        instructionsLine1.draw(instructionsGUI)
        instructionsLine2 = Text(Point(500,100),"Use the arrow keys to control where you are firing and press enter to fire a shot.")
        instructionsLine2.setSize(16)
        instructionsLine2.draw(instructionsGUI)
        instructionsLine3 = Text(Point(500,120),"If you hit your oponent, the space will become red, if you miss, the space will become white.")
        instructionsLine3.setSize(16)
        instructionsLine3.draw(instructionsGUI)
        instructionsLine3 = Text(Point(500,140),"If you hit all of your oponents ships, you win, however if your oponent hits all of your ships first, you will lose")
        instructionsLine3.setSize(16)
        instructionsLine3.draw(instructionsGUI)

####################################################################
        #Creates a GUI for the player.
        playerGUI  = GraphWin("Battleship Player", 500, 500)
        #Creates the gray border of the gui
        border = Rectangle(Point(0,0),Point(500,500))
        border.setFill(color_rgb(220,210,200))
        border.draw(playerGUI)
        #Creates the blue ocean that is the main space of the game
        ocean = Rectangle(Point(50,50),Point(450,450))
        ocean.setFill(color_rgb(1,161,249))
        ocean.draw(playerGUI)
        #The list of the letters that correspond to the x coordinates
        letters = list(["A","B","C","D","E","F","G","H"])
        for i in range(1,9):
            #creates the variable xy which corresponds to the current
            #position of where the labels and lineswill be placed
            xy = ((i) * 50) + 50
            #creates the grid lines
            vertLine =  Line(Point(xy,50),Point(xy,450))
            horizLine = Line(Point(50,xy),Point(450,xy))
            vertLine.draw(playerGUI)
            horizLine.draw(playerGUI)
            #Labels both axes
            vertLabel = Text(Point(25,(xy-25)),(i))
            vertLabel.setSize(20)
            vertLabel.draw(playerGUI)
            horizLabel = Text(Point((xy-25),25),letters[i-1])
            horizLabel.setSize(20)
            horizLabel.draw(playerGUI)
        #Creates a label for the players score
        playerScoreText = Text(Point(350,475),"Player Score: ")
        playerScoreText.setSize(22)
        playerScoreText.draw(playerGUI)
        #Initializes the list variable occupiedComp
        occupiedComp = []

####################################################################

        #   This is the primary for loop for placing ships. First time through the ship is 5 long, so length = 5
        #   and since there's two ships with length 3, when i is 2 or 3 the length is 3
        for i in range(5):
            if i == 0:
                length = 5
            if i == 1:
                length = 4
            if i == 2 or i == 3:
                length = 3
            if i == 4:
                length = 2
    ####################################################################
    #   These are the variables used in the while loops to control when a player either 
    #   places a ship on top of another or the player simply rotates the ship
    #
    #   placing = 1 Is when the player is still placing a ship, and the program only
    #   broke from the while loop because the player rotated the ship
    #
    #   vertical = 1 Is whether or not the player has the ship vertical. When the ship is
    #   vertical/not, it changes how it's position is read and written/displayed
    #
    #   restart = 1 Is whether or not the program needs to placement needs to restart
    #   because the player placed a ship on top of another ship
    #
    #   repeat = 0 Is the variable that is set to the number of times a ship's grids overlap
    #   with another ship. This allows the program to set restart to 1, and ask for a new
    #   ship position
    #
    #   x and y are just the starting positions of all the ship placements
    ####################################################################
            placing = 1
            vertical = 1
            restart = 1
            repeat = 0
            x = 50
            y = 50
            while restart == 1:
                restart = 0
                while placing == 1:
                    while vertical == 1:
                        #   The limits are defined by how long the ship is. If the ship is 5 long,
                        #   the user can only move the ship within a 4x8 grid (depending on
                        #   if vertical or not)
                        limitY = 50*((8 - length) + 1)
                        limitX = 50*((8 - length) + 1)
                        secondX = x + 50
                        secondY = y + 50*length
                        ship = Oval(Point(x,y),Point(secondX,secondY))
                        ship.setFill("gray")
                        ship.draw(playerGUI)
                        move = playerGUI.getKey()
                        #   These are all the different inputs a user can select.
                        #   Enter (Return) places the ship
                        #   r = rotate the ship
                        #   arrow keys move the ship around
                        if move == "Return":
                            placing = 0
                            ship.setFill("black")
                            ship.undraw()
                            ship.draw(playerGUI)
                            break
                        if move == "r":
                            vertical = 0
                            ship.undraw()
                            if x > limitX:
                                x = limitX
                            if x < 50:
                                x = x + 50
                            if y > 400:
                                y = y - 50
                            if y < 50:
                                y = y + 50
                            break
                        if move == "Up":
                            y = y - 50
                        if move == "Down":
                            y = y + 50
                        if move == "Left":
                            x = x - 50
                        if move == "Right":
                            x = x + 50
                        if y > limitY:
                            y = y - 50
                        if x < 50:
                            x = x + 50
                        if x > 400:
                            x = x - 50
                        if y < 50:
                            y = y + 50
                        ship.undraw()
                    #   If the user pressed enter, breaks
                    if placing == 0:
                        break
                    #   All the same as before, except using limitY instead
                    while vertical == 0:
                        limitX = 50*((8 - length) + 1)
                        limitY = 50*((8 - length) + 1)
                        secondX = x + 50*length
                        secondY = y + 50
                        ship = Oval(Point(x,y),Point(secondX,secondY))
                        ship.setFill("gray")
                        ship.draw(playerGUI)
                        move = playerGUI.getKey()
                        if move == "Return":
                            placing = 0
                            ship.setFill("black")
                            ship.undraw()
                            ship.draw(playerGUI)
                            break
                        if move == "r":
                            vertical = 1
                            ship.undraw()
                            if y > limitY:
                                y = limitY
                            if x < 50:
                                x = x + 50
                            if x > 400:
                                x = x - 50
                            if y < 50:
                                y = y + 50
                            break
                        if move == "Up":
                            y = y - 50
                        if move == "Down":
                            y = y + 50
                        if move == "Left":
                            x = x - 50
                        if move == "Right":
                            x = x + 50
                        if x > limitX:
                            x = x - 50
                        if x < 50:
                            x = x + 50
                        if y > 400:
                            y = y - 50
                        if y < 50:
                            y = y + 50
                        ship.undraw()
                #   This reads the positions that the ships occupied based on coords,
                #   and turns it into the string value A1, B1, etc.
                for i in range(length):
                    if vertical == 0:
                        initialX = x + (50*(i))
                        initialY = y
                    if vertical == 1:
                        initialY = y + (50*(i))
                        initialX = x
                    if initialX == 50:
                        column = "A"
                    elif initialX == 100:
                        column = "B"
                    elif initialX == 150:
                        column = "C"
                    elif initialX == 200:
                        column = "D"
                    elif initialX == 250:
                        column = "E"
                    elif initialX == 300:
                        column = "F"
                    elif initialX == 350:
                        column = "G"
                    elif initialX == 400:
                        column = "H"
                    if initialY == 50:
                        row = 1
                    elif initialY == 100:
                        row = 2
                    elif initialY == 150:
                        row = 3
                    elif initialY == 200:
                        row = 4
                    elif initialY == 250:
                        row = 5
                    elif initialY == 300:
                        row = 6
                    elif initialY == 350:
                        row = 7
                    elif initialY == 400:
                        row = 8
                    #   Creates the string value
                    slot = column+str(row)
                    #   Looks for repeats from previous ships
                    repeat = repeat + occupiedComp.count(slot)
                    #   Adds the string value
                    occupiedComp.append(slot)
                #   If the program finds that ships overlap, runs this which removes all
                #   the coordinates that were entered for the misplaced ship, and asks the
                #   user to choose again
                if repeat >= 1:
                    restart = 1
                    ship.undraw()
                    ship.setFill("red")
                    ship.draw(playerGUI)
                    ship.undraw()
                    for i in range(length):
                        del occupiedComp[(len(occupiedComp)-1)]
                    repeat = 0
                    placing = 1
        placeShips(occupiedComp)




####################################################################
        #Creates the computer GUI
        computerGUI  = GraphWin("Battleship Computer", 500, 500)
        #Creates the computerGUI's gray border
        border = Rectangle(Point(0,0),Point(500,500))
        border.setFill(color_rgb(220,210,200))
        border.draw(computerGUI)
        #Creates the ocean that is the main playing field
        ocean = Rectangle(Point(50,50),Point(450,450))
        ocean.setFill(color_rgb(1,161,249))
        ocean.draw(computerGUI)
        #The list of the letters that correspond to the x coordinates
        letters = list(["A","B","C","D","E","F","G","H"])
        for i in range(1,9):
            #creates the variable xy which corresponds to the current
            #position of where the labels and lineswill be placed
            xy = ((i) * 50) + 50
            #Creates the grid lines for the GUI
            vertLine =  Line(Point(xy,50),Point(xy,450))
            horizLine = Line(Point(50,xy),Point(450,xy))
            vertLine.draw(computerGUI)
            horizLine.draw(computerGUI)
            #Labels each row and column
            vertLabel = Text(Point(25,(xy-25)),(i))
            vertLabel.setSize(20)
            vertLabel.draw(computerGUI)
            horizLabel = Text(Point((xy-25),25),letters[i-1])
            horizLabel.setSize(20)
            horizLabel.draw(computerGUI)
        #Creates a label for the computer's score
        computerScoreText = Text(Point(325,475),"Computer Score: ")
        computerScoreText.setSize(22)
        computerScoreText.draw(computerGUI)
            
####################################################################

        #   Computer finds where to put their ships
        #   Format is essentially the same as the player ship placement
        restart = 1
        while restart == 1:
            #   initializes the occupied list (where ships will be placed)
            occupied = []
            restart = 0
            #   exact same loop as player placement, loops 5 times for the 4 different lengths of ship
            for i in range(5):
                if i == 0:
                    length = 5
                if i == 1:
                    length = 4
                if i == 2 or i == 3:
                    length = 3
                if i == 4:
                    length = 2
                #   Instead of the player choosing whether the ships are vertical, randomly selects
                vertical = randint(0,1)
                #   if the ship is vertical
                if vertical == 1:
                    #   defines the limit of where the first square the ship is placed in can be
                    limitY = (8 - length)
                    #   selects a random column (A-H)
                    column = randint(0,7)
                    columnList = ["A","B","C","D","E","F","G","H"]
                    column = columnList[column]
                    row = randint(1,limitY)
                    #   For however long the ship is
                    for i in range(length):
                        #   starts from the inital square that was just chosen, and places a ship occupying space
                        #   for the length of the ship
                        row = row + 1
                        slot = column+str(row)
                        repeat = occupied.count(slot)
                        occupied.append(slot)
                        #   if a spot is chosen to be placed where another ship already is, sets restar to 1 so the
                        #   program knows to start again to choose new ship locations
                        if repeat >= 1:
                            restart = 1
                #   if the ship isn't vertical
                #   same as above
                if vertical == 0:
                    limitX = (8 - length)
                    columnNum = randint(0,limitX)
                    row = randint(1,8)
                    for i in range(length):
                        columnList = ["A","B","C","D","E","F","G","H"]
                        column = columnList[columnNum+i]
                        slot = column+str(row)
                        repeat = occupied.count(slot)
                        occupied.append(slot)
                        if repeat >= 1:
                            restart = 1
        #   once the program stops restarting (in case there are repeats), places all the ships
        placeCompShips(occupied)

####################################################################
        
        #Sets the scores of the player and the computer to 0
        playerScore = 0
        computerScore = 0
        #Creates a text object that states what the current score is.
        playerScoreNum = Text(Point(430,475), playerScore)
        playerScoreNum.setSize(22)
        playerScoreNum.draw(playerGUI)
        computerScoreNum = Text(Point(430,475), computerScore)
        computerScoreNum.setSize(22)
        computerScoreNum.draw(computerGUI)

####################################################################
        
        #   Initiliazes x and y at 75 (where the player's selection circle starts off)
        x = 75
        y = 75
        #   whie the score of player or computer are below 17, the game continues
        while playerScore < 17 and computerScore < 17:
            #   Exact same formatting as the player placement program, with 2 variables 
            #   placing = indicate when the player is done selecting a coordinate to fire at
            #   restart = whether the player chose an invalid coordinate or not so the program asks for the
            #   player to choose again
            restart = 1
            placing = 1
            while restart == 1:
                restart = 0
                while placing == 1:
                    #   Draws the circle that the player moves around to choose a firing spot
                    selection = Circle(Point(x,y),15)
                    selection.setFill("black")
                    selection.draw(computerGUI)
                    move = computerGUI.getKey()
                    #   Once the key is retrieved ^
                    #   either moves the circle in a certain direcion or confirms the player's selection
                    if move == "Return":
                        placing = 0
                        selection.undraw()
                        break
                    if move == "Up":
                        y = y - 50
                    if move == "Down":
                        y = y + 50
                    if move == "Left":
                        x = x - 50
                    if move == "Right":
                        x = x + 50
                    if y > 425:
                        y = y - 50
                    if y < 50:
                        y = y + 50
                    if x > 425:
                        x = x - 50
                    if x < 50:
                        x = x + 50
                    #   undraws the previous circle (the gray circle used for selecting)
                    selection.undraw()
                #   takes the coordinates of the circle and converts it into the two letter/number string of
                #   the coordinate
                if x == 75:
                    column = "A"
                elif x == 125:
                    column = "B"
                elif x == 175:
                    column = "C"
                elif x == 225:
                    column = "D"
                elif x == 275:
                    column = "E"
                elif x == 325:
                    column = "F"
                elif x == 375:
                    column = "G"
                elif x == 425:
                    column = "H"
                if y == 75:
                    row = 1
                elif y == 125:
                    row = 2
                elif y == 175:
                    row = 3
                elif y == 225:
                    row = 4
                elif y == 275:
                    row = 5
                elif y == 325:
                    row = 6
                elif y == 375:
                    row = 7
                elif y == 425:
                    row = 8
                #   initializes validcheck and resets it each time this module runs
                validCheck = ""
                #   Writes the coordinate that was just converted into it's corresponding spot
                validCheck = compWriteCoordinates(column,row)
                #   if the coordinate was already taken up by a miss/hit, returns invalid
                if validCheck == "Invalid":
                    #   indicates that the program needs to run again since the player chose an invalid spot
                    restart = 1
                    placing = 1
            #   Reads the coordinates of what was just chosen and stores it in compCoords
            compCoords = compReadCoordinates(column,row)
            #   If the player hit the ship, creates a custom circle
            if compCoords == "Hit":
                playerScoreNum.undraw()
                playerScore += 1
                playerScoreNum = Text(Point(430,475), playerScore)
                playerScoreNum.setSize(22)
                playerScoreNum.draw(playerGUI)
                selection = Circle(Point(x,y),20)
                selection.setFill("red")
            #   If the player missed the ship, creates another custom circle
            if compCoords == "Miss":
                selection = Circle(Point(x,y),20)
                selection.setFill("white")
            #   draws that circle
            selection.draw(computerGUI)

            #If both scores are under 17...
            if playerScore < 17 and computerScore < 17:
                #Depending on the difficulty gives different chances for a guaranteed hit on a ship. 17/100 for easy, 17/50 for normal, and 17/20 for hard
                if (randint(1,100) <= 17 and difficulty == "Easy") or (randint(1,50) <= 17 and difficulty == "Normal") or (randint(1,20) <= 17 and difficulty == "Hard") :
                    #While loop that will continue going until it hits a new ship.
                    while True:
                        #Uses the list of ships to find a random space with a ship on it
                        shipCoord = occupiedComp[randint(0,16)]
                        #Splits the coordinate into a letter and a number
                        letter = shipCoord[0]
                        number = shipCoord[1]
                        #Checks whether the space has already been fired on.
                        validCheck = ""
                        validCheck = writeCoordinates(letter,number)
                        #If the space has not been fired on...
                        if validCheck != "Invalid":
                            #Sets the coords variable equal to the state of that space
                            coords = readCoordinates(letter,number)
                            #If that space has been hit...
                            if coords == "Hit":
                                #Sets the variables x2 and y2 to the x and y values of that space.
                                x2, y2 = coordConvert(letter, number)
                                #Creates a red circle at that point
                                computerShot = Circle(Point(x2,y2),20)
                                computerShot.setFill("red")
                                computerShot.draw(playerGUI)
                                #Adds 1 to the computer's score and redraws it.
                                computerScoreNum.undraw()
                                computerScore += 1
                                computerScoreNum = Text(Point(430,475), computerScore)
                                computerScoreNum.setSize(22)
                                computerScoreNum.draw(computerGUI)
                                #Breaks out of the loop.
                                break
                else:
                    #While loop that will continue going until it hits a new space.
                    while True:
                        #randomly chooses a coordinate using a letter and number
                        letter, number = [letters[randint(0,7)],randint(1,8)]
                        #If that space is either a ship or empty...
                        if readCoordinates(letter, number) == "Ship" or readCoordinates(letter, number) == "Empty":
                            #Checks the validity of the space
                            validCheck = ""
                            validCheck = writeCoordinates(letter,number)
                            if validCheck != "Invalid":
                                #Sets the coords cariable equal to the state of that space
                                coords = readCoordinates(letter,number)
                                #If the computer hits a ship...
                                if coords == "Hit":
                                    #Sets the variables x2 and y2 to the x and y values of that space.
                                    x2, y2 = coordConvert(letter, number)
                                     #Creates a red circle at that point
                                    computerShot = Circle(Point(x2,y2),20)
                                    computerShot.setFill("red")
                                    #Adds 1 to the computer's score and redraws it.
                                    computerScoreNum.undraw()
                                    computerScore += 1
                                    computerScoreNum = Text(Point(430,475), computerScore)
                                    computerScoreNum.setSize(22)
                                    computerScoreNum.draw(computerGUI)
                                #If the computer misses a ship...
                                if coords == "Miss":
                                    #Sets the variables x2 and y2 to the x and y values of that space.
                                    x2, y2 = coordConvert(letter, number)
                                    #Creates a white circle at that point to signify a miss
                                    computerShot = Circle(Point(x2,y2),20)
                                    computerShot.setFill("white")
                                #Draws the shot that the computer fired then exits the loop
                                computerShot.draw(playerGUI) 
                                break
            
            


####################################################################
        #Creates a new control panel GUI in order to restart or quit the game                    
        controlGUI = GraphWin("Control Panel",400,700)
        controlBackground = Rectangle(Point(0,0),Point(400,700))
        controlBackground.setFill(color_rgb(0,170,250))
        controlBackground.draw(controlGUI)
        #Text object stating whether the player won or lost
        winnerText1 = Text(Point(200,65),"You")
        winnerText1.setSize(36)
        if playerScore == 17:
            winnerText2 = Text(Point(200,100),"Win!")
            winnerText2.setSize(36)
        else:
            winnerText2 = Text(Point(200,100),"Lose")
            winnerText2.setSize(36)
        winnerText1.draw(controlGUI)
        winnerText2.draw(controlGUI)
        #Text object asking whether the palyer wants to restart
        restartText = Text(Point(200,365),"Would you like to restart?: ")
        restartText.setSize(18)
        restartText.draw(controlGUI)
        #A yes button if the player wants to restart
        yesButton = Rectangle(Point(100,400),Point(300,475))
        yesButton.setFill(color_rgb(0,140,220))
        yesText = Text(Point(200,437.5),"Yes")
        yesText.setSize(20)
        yesButton.draw(controlGUI)
        yesText.draw(controlGUI)
        #A no button if the player does not want to restart
        noButton = Rectangle(Point(100,500),Point(300,575))
        noButton.setFill(color_rgb(0,140,220))
        noText = Text(Point(200,537.5), "No")
        noText.setSize(20)
        noButton.draw(controlGUI)
        noText.draw(controlGUI)
        #Sets the variable restarting to blank
        restarting = ""
        #While restarting is not equal to anything...
        while restarting == "":
            #Gets the x and y coordinates of the player mouse click
            point = controlGUI.getMouse()
            pointX = point.getX()
            pointY = point.getY()
            if pointX >= 100 and pointX <= 300:
                #If that click is on the yes button...
                if pointY >= 400 and pointY <= 475 and restarting == "":
                    #Set restarting equal to yes
                    restarting = "Yes"
                #If that click is on the no button...
                if pointY >= 500 and pointY <= 575 and restarting == "":
                    #Set restarting equals to no
                    restarting = "No"
        #If they are restarting...
        if restarting == "Yes":
            #Resets the board so that all the spaces are Empty
            for i in range(8):
                columnA[i] = "Empty"
                columnB[i] = "Empty"
                columnC[i] = "Empty"
                columnD[i] = "Empty"
                columnE[i] = "Empty"
                columnF[i] = "Empty"
                columnG[i] = "Empty"
                columnH[i] = "Empty"
                columnCompA[i] = "Empty"
                columnCompB[i] = "Empty"
                columnCompC[i] = "Empty"
                columnCompD[i] = "Empty"
                columnCompE[i] = "Empty"
                columnCompF[i] = "Empty"
                columnCompG[i] = "Empty"
                columnCompH[i] = "Empty"
            #Closes all the GUIs and goes back to the start of the main while loop
            playerGUI.close()
            computerGUI.close()
            instructionsGUI.close()
            controlGUI.close()
            
        if restarting == "No":
            #Closes the GUIs
            playerGUI.close()
            computerGUI.close()
            instructionsGUI.close()
            controlGUI.close()
            #Sets the value of game to False
            game = False
            #Breaks out of the while loop
            break
        

        

####################################################################

#A function to convert a letter and number into the corresponding coordinate of the center of that space
def coordConvert(letter, number):
    number = int(number)
    if letter == "A":
        x = 75
    elif letter == "B":
        x = 125
    elif letter == "C":
        x = 175
    elif letter == "D":
        x = 225
    elif letter == "E":
        x = 275
    elif letter == "F":
        x = 325
    elif letter == "G":
        x = 375
    elif letter == "H":
        x = 425
    if number == 1:
        y = 75
    elif number == 2:
        y = 125
    elif number == 3:
        y = 175
    elif number == 4:
        y = 225
    elif number == 5:
        y = 275
    elif number == 6:
        y = 325
    elif number == 7:
        y = 375
    elif number == 8:
        y = 425
    #Returns the x and y values of that coordinate
    return x, y

###################################################################
#Returns the state of that space
def readCoordinates(letter, number):
    #Formats number so it can be used to index the lists
    number = int(number)
    number = number - 1
    if letter == "A":
        if columnA[number] == "Empty":
           return "Empty"
        if columnA[number] == "Ship":
           return "Ship"
        if columnA[number] == "Hit":
           return "Hit"
        if columnA[number] == "Miss":
           return "Miss"
    if letter == "B":
        if columnB[number] == "Empty":
           return "Empty"
        if columnB[number] == "Ship":
           return "Ship"
        if columnB[number] == "Hit":
           return "Hit"
        if columnB[number] == "Miss":
           return "Miss"
    if letter == "C":
        if columnC[number] == "Empty":
           return "Empty"
        if columnC[number] == "Ship":
           return "Ship"
        if columnC[number] == "Hit":
           return "Hit"
        if columnC[number] == "Miss":
           return "Miss"
    if letter == "D":
        if columnD[number] == "Empty":
           return "Empty"
        if columnD[number] == "Ship":
           return "Ship"
        if columnD[number] == "Hit":
           return "Hit"
        if columnD[number] == "Miss":
           return "Miss"
    if letter == "E":
        if columnE[number] == "Empty":
           return "Empty"
        if columnE[number] == "Ship":
           return "Ship"
        if columnE[number] == "Hit":
           return "Hit"
        if columnE[number] == "Miss":
           return "Miss"
    if letter == "F":
        if columnF[number] == "Empty":
           return "Empty"
        if columnF[number] == "Ship":
           return "Ship"
        if columnF[number] == "Hit":
           return "Hit"
        if columnF[number] == "Miss":
           return "Miss"
    if letter == "F":
        if columnF[number] == "Empty":
           return "Empty"
        if columnF[number] == "Ship":
           return "Ship"
        if columnF[number] == "Hit":
           return "Hit"
        if columnF[number] == "Miss":
           return "Miss"
    if letter == "G":
        if columnG[number] == "Empty":
           return "Empty"
        if columnG[number] == "Ship":
           return "Ship"
        if columnG[number] == "Hit":
           return "Hit"
        if columnG[number] == "Miss":
           return "Miss"
    if letter == "H":
        if columnH[number] == "Empty":
           return "Empty"
        if columnH[number] == "Ship":
           return "Ship"
        if columnH[number] == "Hit":
           return "Hit"
        if columnH[number] == "Miss":
           return "Miss"
    else:
        return "Invalid"

#Same as read coordinates but for the computers lists
def compReadCoordinates(letter, number):
    number = int(number)
    number = number - 1
    if letter == "A":
        if columnCompA[number] == "Empty":
           return "Empty"
        if columnCompA[number] == "Ship":
           return "Ship"
        if columnCompA[number] == "Hit":
           return "Hit"
        if columnCompA[number] == "Miss":
           return "Miss"
    if letter == "B":
        if columnCompB[number] == "Empty":
           return "Empty"
        if columnCompB[number] == "Ship":
           return "Ship"
        if columnCompB[number] == "Hit":
           return "Hit"
        if columnCompB[number] == "Miss":
           return "Miss"
    if letter == "C":
        if columnCompC[number] == "Empty":
           return "Empty"
        if columnCompC[number] == "Ship":
           return "Ship"
        if columnCompC[number] == "Hit":
           return "Hit"
        if columnCompC[number] == "Miss":
           return "Miss"
    if letter == "D":
        if columnCompD[number] == "Empty":
           return "Empty"
        if columnCompD[number] == "Ship":
           return "Ship"
        if columnCompD[number] == "Hit":
           return "Hit"
        if columnCompD[number] == "Miss":
           return "Miss"
    if letter == "E":
        if columnCompE[number] == "Empty":
           return "Empty"
        if columnCompE[number] == "Ship":
           return "Ship"
        if columnCompE[number] == "Hit":
           return "Hit"
        if columnCompE[number] == "Miss":
           return "Miss"
    if letter == "F":
        if columnCompF[number] == "Empty":
           return "Empty"
        if columnCompF[number] == "Ship":
           return "Ship"
        if columnCompF[number] == "Hit":
           return "Hit"
        if columnCompF[number] == "Miss":
           return "Miss"
    if letter == "F":
        if columnCompF[number] == "Empty":
           return "Empty"
        if columnCompF[number] == "Ship":
           return "Ship"
        if columnCompF[number] == "Hit":
           return "Hit"
        if columnCompF[number] == "Miss":
           return "Miss"
    if letter == "G":
        if columnCompG[number] == "Empty":
           return "Empty"
        if columnCompG[number] == "Ship":
           return "Ship"
        if columnCompG[number] == "Hit":
           return "Hit"
        if columnCompG[number] == "Miss":
           return "Miss"
    if letter == "H":
        if columnCompH[number] == "Empty":
           return "Empty"
        if columnCompH[number] == "Ship":
           return "Ship"
        if columnCompH[number] == "Hit":
           return "Hit"
        if columnCompH[number] == "Miss":
           return "Miss"
    else:
        return "Invalid"


#Used for firing. Takes input for letter and number.
#If that space is empty it changes it to a miss, if the space has a ship, changes it to a hit.
#If it has already been fired upon, returns invalid.
def writeCoordinates(letter, number):
    #Formats number so it can be used for list indexing
    number = int(number)
    number = number - 1
    if letter == "A":
        if columnA[number] == "Hit" or columnA[number] == "Miss":
            return "Invalid"
        if columnA[number] == "Empty":
           columnA[number] = "Miss"
        if columnA[number] == "Ship":
           columnA[number] = "Hit"
    if letter == "B":
        if columnB[number] == "Hit" or columnB[number] == "Miss":
            return "Invalid"
        if columnB[number] == "Empty":
           columnB[number] = "Miss"
        if columnB[number] == "Ship":
           columnB[number] = "Hit"
    if letter == "C":
        if columnC[number] == "Hit" or columnC[number] == "Miss":
            return "Invalid"
        if columnC[number] == "Empty":
           columnC[number] = "Miss"
        if columnC[number] == "Ship":
           columnC[number] = "Hit"
    if letter == "D":
        if columnD[number] == "Hit" or columnD[number] == "Miss":
            return "Invalid"
        if columnD[number] == "Empty":
           columnD[number] = "Miss"
        if columnD[number] == "Ship":
           columnD[number] = "Hit"
    if letter == "E":
        if columnE[number] == "Hit" or columnE[number] == "Miss":
            return "Invalid"
        if columnE[number] == "Empty":
           columnE[number] = "Miss"
        if columnE[number] == "Ship":
           columnE[number] = "Hit"
    if letter == "F":
        if columnF[number] == "Hit" or columnF[number] == "Miss":
            return "Invalid"
        if columnF[number] == "Empty":
           columnF[number] = "Miss"
        if columnF[number] == "Ship":
           columnF[number] = "Hit"
    if letter == "G":
        if columnG[number] == "Hit" or columnG[number] == "Miss":
            return "Invalid"
        if columnG[number] == "Empty":
           columnG[number] = "Miss"
        if columnG[number] == "Ship":
           columnG[number] = "Hit"
    if letter == "H":
        if columnH[number] == "Hit" or columnH[number] == "Miss":
            return "Invalid"
        if columnH[number] == "Empty":
           columnH[number] = "Miss"
        if columnH[number] == "Ship":
           columnH[number] = "Hit"
        
#The same as writeCoordinates but for the computer
def compWriteCoordinates(letter, number):
    number = int(number)
    number = number - 1
    if letter == "A":
        if columnCompA[number] == "Hit" or columnCompA[number] == "Miss":
            return "Invalid"
        if columnCompA[number] == "Empty":
           columnCompA[number] = "Miss"
        if columnCompA[number] == "Ship":
           columnCompA[number] = "Hit"
    if letter == "B":
        if columnCompB[number] == "Hit" or columnCompB[number] == "Miss":
            return "Invalid"
        if columnCompB[number] == "Empty":
           columnCompB[number] = "Miss"
        if columnCompB[number] == "Ship":
           columnCompB[number] = "Hit"
    if letter == "C":
        if columnCompC[number] == "Hit" or columnCompC[number] == "Miss":
            return "Invalid"
        if columnCompC[number] == "Empty":
           columnCompC[number] = "Miss"
        if columnCompC[number] == "Ship":
           columnCompC[number] = "Hit"
    if letter == "D":
        if columnCompD[number] == "Hit" or columnCompD[number] == "Miss":
            return "Invalid"
        if columnCompD[number] == "Empty":
           columnCompD[number] = "Miss"
        if columnCompD[number] == "Ship":
           columnCompD[number] = "Hit"
    if letter == "E":
        if columnCompE[number] == "Hit" or columnCompE[number] == "Miss":
            return "Invalid"
        if columnCompE[number] == "Empty":
           columnCompE[number] = "Miss"
        if columnCompE[number] == "Ship":
           columnCompE[number] = "Hit"
    if letter == "F":
        if columnCompF[number] == "Hit" or columnCompF[number] == "Miss":
            return "Invalid"
        if columnCompF[number] == "Empty":
           columnCompF[number] = "Miss"
        if columnCompF[number] == "Ship":
           columnCompF[number] = "Hit"
    if letter == "G":
        if columnCompG[number] == "Hit" or columnCompG[number] == "Miss":
            return "Invalid"
        if columnCompG[number] == "Empty":
           columnCompG[number] = "Miss"
        if columnCompG[number] == "Ship":
           columnCompG[number] = "Hit"
    if letter == "H":
        if columnCompH[number] == "Hit" or columnCompH[number] == "Miss":
            return "Invalid"
        if columnCompH[number] == "Empty":
           columnCompH[number] = "Miss"
        if columnCompH[number] == "Ship":
           columnCompH[number] = "Hit"

#   Used to place ships based on placeList
def placeShips(placeList):
    #   For how long the list is
    for i in range(len(placeList)):
        #   reads the coordinate (i.e. H3) and sets it to two variables
        coordinate = placeList[i]
        letter = coordinate[0]
        number = int(coordinate[1])
        number = number-1
        #   Sets the current selected coordinate to a spot containing a ship
        if letter == "A":
            columnA[number] = "Ship"
        if letter == "B":
            columnB[number] = "Ship"
        if letter == "C":
            columnC[number] = "Ship"
        if letter == "D":
            columnD[number] = "Ship"
        if letter == "E":
            columnE[number] = "Ship"
        if letter == "F":
            columnF[number] = "Ship"
        if letter == "G":
            columnG[number] = "Ship"
        if letter == "H":
            columnH[number] = "Ship"

#   Same as the function before, just for the computer's list
def placeCompShips(placeList):
    for i in range(len(placeList)):
        coordinate = placeList[i]
        letter = coordinate[0]
        number = int(coordinate[1])
        number = number-1
        if letter == "A":
            columnCompA[number] = "Ship"
        if letter == "B":
            columnCompB[number] = "Ship"
        if letter == "C":
            columnCompC[number] = "Ship"
        if letter == "D":
            columnCompD[number] = "Ship"
        if letter == "E":
            columnCompE[number] = "Ship"
        if letter == "F":
            columnCompF[number] = "Ship"
        if letter == "G":
            columnCompG[number] = "Ship"
        if letter == "H":
            columnCompH[number] = "Ship"

main()
    
    
    





