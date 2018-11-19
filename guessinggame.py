# guessinggame.py
# Austin Napier
# This program will, within a range of 1 and 1000, generate a random
# number and ask the user to guess a number within those parameters. It
# will then say if the user was too high to too low until they get it
# right, and display how many guesses they made.

from random import randrange

# Constants
LOWLIM=1
UPLIM=1000

# This function decides if the guess is right and, if not, whether it's
# too high or too low, and returns the result to the main function.
def guessfunc(guess, Num):
    if guess < Num:
        result="Too low"
    elif guess > Num:
        result="Too high"
    else:
        result="Correct!"
    return result

def main():
    # Handshake
    print("This program is a guessing game that generates a random")
    print("number between 1 and 1000. It tells you if your guess is too")
    print("low or too high until you get it right, then tells you how")
    print("many guesses it took to get it.")
    print()
    # Generates the random number.
    Num=randrange(LOWLIM, UPLIM)
    # Sets initial value for number of attempts and sets dummy for
    # the initial guess to allow the loop to initiate.
    tries=0
    guess=-1
    # Starts a loop that takes a guess, counts it as a try, runs the
    # guess through the guess function, then provides feedback and
    # either resolves the loop or runs it again.
    while guess != Num:
            guess=int(input("Enter a number between 1 and 1000: "))
            tries=tries+1
            guessfunc(guess, Num)
            if guess==Num:
                print(guessfunc(guess, Num))
                print("You took", tries, "tries.")
            else:
                print(guessfunc(guess, Num))
                

main()
