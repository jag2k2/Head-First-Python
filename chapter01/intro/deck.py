import random

suits = ["Clubs", "Spades", "Hearts", "Ace"]        # python list [] - mutable
faces = ["Jack", "Queen", "King", "Ace"]            # python list [] - mutable
numbered = [2, 3, 4, 5, 6, 7, 8, 9, 10]             # python list [] - mutable

def draw ():
    the_suit = random.choice(suits)
    the_card = random.choice(faces + numbered)
    return the_card, "of", the_suit                 # returns a python tuple () - immutable

if __name__ == "__main__":
    for _ in range (5):         # _ is python's default variable 
        print(draw())