# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
#created on 25 april 2016
#http://www.codeskulptor.org/#user41_4C30ZpdiSOQfG2c_0.py
import simplegui
import random
number = 0
count = 7
range1 = ""
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global number ,count 
    number = 0
    count = 7
    
    if(range1 != ""):
        if(range1 == "range100"):
            range100()
        elif(range1 == "range1000"):
            range1000()  
    else:
        range100()
        



# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global number, count , range1
    range1 = "range100"
    count = 7
    number = random.randrange(0,100,1)
    print "Guess number in Range 100"
    return number

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global number, count , range1 
    range1 = "range1000"
    count = 10
    number = random.randrange(0,1000,1)
    print "Guess number in Range 1000"
    return number
    
def input_guess(guess):
    # main game logic goes here	
    global count
    print "Number of guess remaining are "+ str(count)
    if(count >= 0):
        count -= 1
        print "Guess was: " + guess
        global number
        if(int(guess) > number):
            print "Lower"
            return
        if(int(guess) < number):
            print "Higher"
            return
        if(int(guess) == number):
            print "Correct"
            new_game()
    else:
        print "You are out of Guess. Start new Game"
        new_game()
    

    
# create frame
frame = simplegui.create_frame('Input_guess', 200, 200)
inp = frame.add_input('Guess', input_guess, 50)
button1 = frame.add_button('range100', range100 ,100)
button2 = frame.add_button('range1000', range1000, 100)
frame.add_button('Restart',new_game,100)
frame.start()
# register event handlers for control elements and start frame


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
