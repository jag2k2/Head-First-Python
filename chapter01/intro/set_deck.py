import random

suits = ["Clubs", "Spades", "Hearts", "Ace"]
faces = ["Jack", "Queen", "King", "Ace"]
numbered = [2, 3, 4, 5, 6, 7, 8, 9, 10]
deck = set()
for suit in suits:
    for card in (faces + numbered):
        deck.add((card, "of", suit))        # build up deck with tuples

def draw ():
    selected_card = random.choice(list(deck))   # each card is a tuple
    deck.remove(selected_card)                  # remove the card from the deck so that it doesn't get selected again
    return selected_card

if __name__ == "__main__":
    for i in range (len(deck)):         # _ is python's default variable 
        print(i, draw())
