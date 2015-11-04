# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
remaining_guess = 7
num_range = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    f.start()
    range100()

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global num_range, remaining_guess
    remaining_guess = 7
    num_range = random.randrange(0, 100)

    print "New game. Range is from 0 to 100"
    print "Number of remaining guesses is", remaining_guess
    print ""

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global num_range, remaining_guess
    remaining_guess = 10
    num_range = random.randrange(0, 1000)

    print "New game. Range is from 0 to 1000"
    print "Number of remaining guesses is", remaining_guess
    print ""

def input_guess(guess):
    # main game logic goes here
    global remaining_guess
    guess = int(guess)
    remaining_guess -= 1

    print "Guess was", guess
    print "Number of remaining guesses is", remaining_guess

    if guess == num_range:
        print "Correct!"
        print ""
        range100()
    elif remaining_guess == 0:
        print "You ran out of guesses. The number was", num_range
        print ""
        range100()
    elif guess < num_range:
        print "Higher!"
        print ""
    else:
        print "Lower!"
        print ""



# create frame
f = simplegui.create_frame("Guess The Number",200,200)

# register event handlers for control elements and start frame
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game
new_game()


# always remember to check your completed program against the grading rubric
