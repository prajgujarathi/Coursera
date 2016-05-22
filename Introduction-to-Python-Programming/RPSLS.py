# Rock-paper-scissors-lizard-Spock template
#Created on 14 april 2016

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
#http://www.codeskulptor.org/#user41_dvMQ9DtQ5s_0.py

# helper functions
import random
def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if(name == "rock"):
        return 0
    if(name == "Spock"):
        return 1
    if(name == "paper"):
        return 2
    if(name == "lizard"):
        return 3
    if(name == "scissors"):
        return 4

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if(number == 0):
        return "rock"
    if(number == 1):
        return "Spock"
    if(number == 2):
        return "paper"
    if(number == 3):
        return "lizard"
    if(number == 4):
        return "scissors"
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    
    
    # print a blank line to separate consecutive games
    print("")
    # print out the message for the player's choice
    print("Player's choice is:"+player_choice)
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,4,1)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print("computer's choice is: " + comp_choice)
    # compute difference of comp_number and player_number modulo five
    diff = (comp_number - player_number)%5
    # use if/elif/else to determine winner, print winner message
    if(diff == 0):
        print("Player and Computer ties")
    elif(diff == 1):
        print("Computer won!")
    elif(diff == 2):     
        print("Computer won!")
    elif(diff == 3):     
        print("Player won!")
    elif(diff == 4):     
        print("Player won!")
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


