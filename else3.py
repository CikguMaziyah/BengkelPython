#!/usr/bin/env python
"""1st line coding automatik akan pilih python interpretor sbg default tp kalo guna unix base os, window tak boleh"""

import random

def main():
    """Start a number guessing game bertween 1-50."""
    print("Guess the number!")

    x=random.randint(1,50)
    guess=None

    while x!=guess:

        guess=int(input("Pick a number between 1 to 50: "))
        
        if x==guess:
            print("You're genius.")
        else:
            print("Sorry wrong answer.")

main()