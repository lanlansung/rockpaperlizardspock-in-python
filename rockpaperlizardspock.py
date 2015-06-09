#import random functions.
import random

"""Assign a number to the entry. Included Caps on first
   letter as it is common user entry mistake."""
def name_to_number(name):
    if name in("Rock","rock"):
        return 0
    elif name in ("Spock","spock"):
        return 1
    elif name in ("Paper" ,"paper"):
        return 2
    elif name in ("Lizard" ,"lizard"):
        return 3
    elif name in("Scissors" , "scissors"):
        return 4
    else: 
        print "Invalid entry, please try again."
    
"""Convert the entry back into a number to be used 
   in the formula."""
def number_to_name(number):
    if number == 0:
        return "rock"
    if number == 1:
        return "Spock"
    if number == 2:
        return "paper"
    if number == 3:
        return "lizard"
    if number == 4:
        return "scissors"
    else:
        print "Invalid entry, please try again."
    
    
#The main function.
def rpsls(player_choice): 
    #Printing out player's input.
    print " "
    print "Player chooses " + str(player_choice)
    
    #Converting the input into number.
    player_number = name_to_number(player_choice)
    
    #Generating a random computer number and printing.
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses " + str(comp_choice)
    
    #Compute difference.
    diff = player_number - comp_number
    #Computer module of diff over 5.
    mod = diff%5
    #Determine winner.
    if mod in (1,2):
        print "Player wins!"
    elif mod in (3,4):
        print "Computer wins!"
    else:
        print "Draw! Please try again."
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")