import random

def main():
    """Start a alphabet guessing game for USTP."""
    print("Guess the alphabet!")

    y="USTP"
    x=random.choice(y)
    guess=None
    
    while x!=guess:
        print("huruf",x)
        guess=str(input("Pick alphabet USTP: "))
        
        
        if x==guess:
            print("Great.")
        else:
            print("Sorry.")

main()