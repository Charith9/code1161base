"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""
from __future__ import division
from __future__ import print_function
from exercise1 import not_number_rejector
from exercise1 import super_asker
import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    marge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("Hi, let's begin")
    print("Please enter a lowerbound:")
    lowerbound = not_number_rejector("Your lowerbound is:")
    upperbound = not_number_rejector("What is you upperbound?:")
    while upperbound <= lowerbound:
        print("Re-enter upperbound")
        pass
    upperbound = int(upperbound)
    lowerbound = int(lowerbound)

    actualNumber = random.randint(lowerbound, upperbound)
    guess = False
    while not guess:
        try:
            input_number = int(raw_input("Guess number:"))
            print("{} is accepted".format(input_number))
            if input_number == actualNumber:
                print("{} is correct".format(input_number))
                guess = True
            elif input_number < actualNumber:
                print("Too small, Re-try")
            elif input_number > upperbound:
                print("Out of bounds")
            elif input_number < lowerbound:
                print("Out of bounds")
            else:
                print("Too large, Re-try")
        except Exception as e:
                print("Try again, number required ({})".format(e))
        return "Thats it"
    pass

    actualNumber = random.randint(upperbound, lowerbound)
    guess = False

    while not guess:
        try:
            input_number = int(raw_input("Guess number:"))
            print("{} is accepted".format(input_number))
            if input_number == actualNumber:
                print("{} is correct".format(input_number))
            guess = True
            elif input_number < actualNumber:
                print("Too small, Re-try")
            elif input_number > lowerbound:
                print("Out of bounds")
            elif input_number < upperbound:
                print("Out of bounds")
        else:
            print("Too large, Re-try")
    except Exception as e:
            print("Try again, number required ({})".format(e))
    return "Voila"
    pass


if __name__ == "__main__":
    advancedGuessingGame()
