#!/usr/bin/env python
"""1st line coding automatik akan pilih python interpretor sbg default tp kalo guna unix base os, window tak boleh"""

import random

def main():
    """Start a number guessing game bertween 1-100."""
    print("Guess the number!")

    x=random.randint(1,100)
    guess=None

    while x!=guess:

        guess=int(input("Pick a number between 1 to 100: "))

        if x==guess:
            print("You genius!")
        elif x>guess:
            print("Try a bigger number.")
        elif x<guess:
            print("Try a smaller number.")

main()