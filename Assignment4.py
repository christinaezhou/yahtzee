import turtle
import random
# CSC 131 Assignment 4
# Christina Zhou
# December 6th

# This is the game Yhatzee. This allows the user to roll the dice and freeze dice

# global list of die, list of die lists
global allDice
# global list of buttons, list of button list
global buttons
# random number generator for the number on dice one
global diceNum1
# random number generator for the number on dice two
global diceNum2
# random number generator for the number on dice three
global diceNum3
# random number generator for the number on dice four
global diceNum4
# random number generator for the number on dice five
global diceNum5

# It should draw using the turtle a rectangle with its upper-left-hand corner at (x, y)
# with the width, height, pen color, and fill color specified.
# If the text is not None, then it also use the turtle to write the text on the rectangle.


def drawRectangle(turtle, x,y, width, height, lineColor, fillColor, text):
    turtle.shape("turtle")
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(lineColor,fillColor)
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.right(180)
    turtle.end_fill()
    turtle.penup()

    if (text != ""):
        turtle.goto(x + width /2 , y - (height/5) )
        turtle.write(text,  font = ("arial", 15, "bold"))

# It should draw using the drawRectangle() function above and the drawDots()
# function below to draw a die with its upper-left-hand corner at (x, y) with the width,
# height, pen color, fill color, and dots specified


def drawDie(turtle, x, y, width, lineColor, fillColor, numDots):

    drawRectangle(turtle, x, y, width, width, lineColor, fillColor, "")

    drawDots(turtle, x, y, numDots)


# It should draw the dots of the die, where the die is positioned with its upper-left-hand corner at (x, y).


def drawDots(turtle, x, y, numDots):
    turtle.shape ("turtle")
    turtle.penup()
    #move to the middle
    
    if(numDots == 1):
        turtle.goto(x + 50 ,y - 50)
        turtle.pendown()
        turtle.color("black","black")
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        turtle.penup()
    #corner diagonals
    
    elif(numDots ==2 ):
        turtle.goto(x + 25, y - 75)
        turtle.pendown()
        turtle.color("black", "black")
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        turtle.penup()

        turtle.goto(x +75, y-20 )
        turtle.pendown()
        turtle.color("black", "black")
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        turtle.penup()
    #diagonal dots  the middle one
    
    elif(numDots ==3):

        turtle.goto(x + 50, y - 50)
        turtle.pendown()
        turtle.color("black", "black")
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()

        turtle.penup()
        turtle.goto(x + 75, y - 75)
        turtle.pendown()
        turtle.color("black", "black")
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        turtle.penup()

        turtle.goto(x + 25, y - 25)
        turtle.pendown()
        turtle.color("black", "black")
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        turtle.penup()
        # diagonal dots  the middle one
        
    elif (numDots == 4):
        turtle.goto(x + 75, y - 75)
        turtle.pendown()
        turtle.color("black", "black")
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        turtle.penup()

        turtle.goto(x + 25, y - 25)
        turtle.pendown()
        turtle.color("black", "black")
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        turtle.penup()

        turtle.goto(x + 75, y - 25)
        turtle.pendown()
        turtle.color("black", "black")
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        turtle.penup()

        turtle.goto(x + 25, y - 75)
        turtle.pendown()
        turtle.color("black", "black")
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        turtle.penup()
        
    #corner four and middle one
    elif(numDots == 5):

        turtle.goto(x + 75, y - 75)
        turtle.pendown()
        turtle.color("black", "black")
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        turtle.penup()

        turtle.goto(x + 25, y - 25)
        turtle.pendown()
        turtle.color("black", "black")
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        turtle.penup()

        turtle.goto(x + 75, y - 25)
        turtle.pendown()
        turtle.color("black", "black")
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        turtle.penup()

        turtle.goto(x + 25, y - 75)
        turtle.pendown()
        turtle.color("black", "black")
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        turtle.penup()

        turtle.goto(x + 50, y - 50)
        turtle.pendown()
        turtle.color("black", "black")
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        turtle.penup()

    #corner four plus two more
    else:
        turtle.goto(x + 75, y - 75)
        turtle.pendown()
        turtle.color("black", "black")
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        turtle.penup()

        turtle.goto(x + 25, y - 25)
        turtle.pendown()
        turtle.color("black", "black")
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        turtle.penup()

        turtle.goto(x + 75, y - 25)
        turtle.pendown()
        turtle.color("black", "black")
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        turtle.penup()

        turtle.goto(x + 25, y - 75)
        turtle.pendown()
        turtle.color("black", "black")
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        turtle.penup()

        turtle.goto(x + 25, y - 50)
        turtle.pendown()
        turtle.color("black", "black")
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        turtle.penup()

        turtle.goto(x + 75, y - 50)
        turtle.pendown()
        turtle.color("black", "black")
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        turtle.penup()

# The function should return True if the point (x, y)
# is within the rectangle specified by upperLeftX, upperLeftY, width, and height.
#  It should return False if not


def isWithin(upperLeftX, upperLeftY, width, height, x, y):
    if((x > upperLeftX) and (x <= upperLeftX + width) and (y < upperLeftY) and (y > upperLeftY - height)):
        return True
    else:
        return False

# Iterate through the list of Dice and (using the isWithin() function) determine if a die was clicked.
# If so, then it should call the dieClick() function below passing the die number (index within the list).
# Iterate through the list of Buttons and (using the isWithin() funciton) determine if a button was clicked.
# If so, then it should call the buttonClick() function below passing the button number (index within the list).


def mouseclick(x,y):
    global allDice
    global buttons

    for i in range(len(allDice)):
        if(isWithin(allDice[i][0], allDice[i][1], allDice[i][2], allDice[i][2], x ,y) == True):
            print("clicked at ", i)
            dieClicked(i)

    
    for i in range(len(buttons)):
        if(isWithin(buttons[i][0], buttons[i][1], buttons[i][3], buttons[i][2], x ,y) == True):
            print("clicked at ", i)
            buttonClicked(i)

# The dieClick() should take as parameters the index number of the die within the list of dice.
# The function should toggle the background color of the die.  For example, if it was "white" then make it "green".
# If it was "green" then make it "white".  Next the function should redraw the die using the drawDie() function.


def dieClicked(idx):
 
    if(allDice[idx][4] == "white"):
        allDice[idx][4] = "green"
        drawDie(turtle, allDice[idx][0],allDice[idx][1],allDice[idx][2],allDice[idx][3],allDice[idx][4],allDice[idx][5])

    elif (allDice[idx][4] == "green"):
        allDice[idx][4] = "white"
        drawDie(turtle, allDice[idx][0],allDice[idx][1],allDice[idx][2],allDice[idx][3],allDice[idx][4],allDice[idx][5])



# If the button is the "New Roll" button, then it should:  set the background colors of the Dice to the original
#  background color and assign random numbers between 1 and 6 to the Dice and redraws dice

# If the button is the "Roll" button, then it should:
# If its background color is the original color (e.g. "white"), then: Assign random numbers between 1 and 6 to the Dice
# and redraw


def buttonClicked(idx):
    global allDice
    if (buttons[idx][6] == "NEW ROLL"):
        diceNum1 = random.randint(1, 6)
        diceNum2 = random.randint(1, 6)
        diceNum3 = random.randint(1, 6)
        diceNum4 = random.randint(1, 6)
        diceNum5 = random.randint(1, 6)
        allDice = [[-300, 300, 100, "black", "white", diceNum1], [0, 300, 100, "black", "white", diceNum2],
                   [300, 300, 100, "black", "white", diceNum3], [-300, 150, 100, "black", "white", diceNum4],
                   [0, 150, 100, "black", "white", diceNum5]]

        for i in range(len(allDice)):

            drawDie(turtle,allDice[i][0],allDice[i][1],allDice[i][2],allDice[i][3],allDice[i][4],allDice[i][5])


    elif (buttons[idx][6] == "ROLL"):
        for i in range(len(allDice)):
            if(allDice[i][4] == "white"):
                diceRandNum = random.randint(1, 6)
                drawDie(turtle, allDice[i][0],allDice[i][1], allDice[i][2], allDice[i][3], allDice[i][4], diceRandNum )


# main function creates a turtle
# creates a list of dice parameter
# creates a list of button parameters
# registers the mouseclick function to be the listener for mouse clicks
# draws turtle and dice buttons
# calls turtle.mainloop()


def main():

    global allDice
    global buttons

    turtle.speed(10)
    diceNum1= random.randint(1, 6)
    diceNum2= random.randint(1, 6)
    diceNum3 = random.randint(1, 6)
    diceNum4= random.randint(1, 6)
    diceNum5= random.randint(1, 6)

    buttons = [[-200, -200, 30, 150, "black", "blue", "ROLL"], [200, -200, 30, 150, "black", "blue", "NEW ROLL"]]

    allDice = [[-300, 300, 100, "black", "white", diceNum1], [0, 300, 100, "black", "white", diceNum2],
               [300, 300, 100, "black", "white", diceNum3], [-300, 150, 100, "black", "white", diceNum4],
               [0, 150, 100, "black", "white", diceNum5]]

    for i in range(len(allDice)):

        drawDie(turtle,allDice[i][0],allDice[i][1],allDice[i][2],allDice[i][3],allDice[i][4],allDice[i][5])

    for i in range(len(buttons)):

        drawRectangle(turtle, buttons[i][0], buttons[i][1], buttons[i][2], buttons[i][3], buttons[i][4], buttons[i][5], buttons[i][6])

    click = turtle.Screen()
    click.onclick(mouseclick, 1, True)
    turtle.mainloop()
    
main()