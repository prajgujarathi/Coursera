# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
#created on 25 april 2016
#http://www.codeskulptor.org/#user41_4C30ZpdiSOQfG2c_0.py
import simplegui
import random
number = 0
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    number = 0
    frame.start()


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global number
    number = random.randrange(0,100,1)
    print number
    return number

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global number
    number = random.randrange(0,1000,1)
    return number
    
def input_guess(guess):
    # main game logic goes here	
    global number
    if(guess > number):
        print "Lower"
        return
    if(guess < number):
        print "Higher"
        return
    if(guess == number):
        print "Correct"
        return
    

    
# create frame
frame = simplegui.create_frame('Input_guess', 500, 500)
inp = frame.add_input('Guess', input_guess, 50)
button1 = frame.add_button('range100', range100 ,100)
button2 = frame.add_button('range1000', range1000, 100)

# register event handlers for control elements and start frame


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
