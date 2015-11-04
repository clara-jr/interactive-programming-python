# Rock-paper-scissors-lizard-Spock


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def name_to_number(name):

    # convert name to a number using if/elif/else
    # don't forget to return the result!
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        print name + ' is an invalid entry. Valid entries are rock, Spock, paper, lizard, scissors. Please try again.'


def number_to_name(number):

    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        print number + ' is an invalid entry. Valid entry is from 0 to 4. Please try again.'


def rpsls(player_name):

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randint(0,4) # it could also be used random.randrange(0,5)

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_name)

    # convert comp_number to comp_name using the function number_to_name()
    comp_name = number_to_name(comp_number)

    # compute difference of comp_number and player_number modulo five
    difference = (player_number - comp_number)
    difference_modular = (difference % 5) # negative cases

    # print out the message for the player's choice
    print "Player chooses", player_name
    # print out the message for computer's choice
    print "Computer chooses", comp_name

    # use if/elif/else to determine winner, print winner message
    if difference_modular == 1 or difference_modular == 2:
        print 'Player wins!'
    elif difference_modular == 3 or difference_modular == 4:
        print 'Computer wins!'
    elif difference_modular == 0:
        print 'Player and computer tie!'
    else:
        print 'Oops! Something has gone wrong! Please try again.'

    # print a blank line to separate consecutive games
    print "\n"

# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
