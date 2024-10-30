
# Import necessary modules
import random
import time

# Define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

# Create a deck of cards
deck = [(rank,suit) for rank in ranks for suit in suits]

# Shuffle the deck 
random.shuffle(deck)

# Split the deck into two hands
p1_deck = deck[0:26]
p2_deck = deck[26:52]

# This variable holds all the cards from a war, gets given to winner later
war_card_pile = []

def card_comparison(p1_card, p2_card):
    """This is the logic that compares two cards to find the stronger card
		Return 1 if player 1's card is strong, 2 for player 2
		if the cards are equal, return 0.

		Hint, using the index function will make this very simple (one liner)"""
    # Your code here
    if ranks.index(p1_card[0]) > ranks.index(p2_card[0]):
        return 1
    elif ranks.index(p1_card[0]) < ranks.index(p2_card[0]):
        return 2
    else:
        return 0


def play_round(p1_deck, p2_deck):
    """Play a single round of the game.
		That is, each player flips a card, and the winner is determined using the card_comparison function
		if both players flip the same value card, call the war function
	"""
    # Your code here

    wait(mode)

    p1_card = p1_deck.pop(0)
    p2_card = p2_deck.pop(0)

    if card_comparison(p1_card,p2_card) == 1:
        p1_deck.extend([p1_card,p2_card])
        print("P1 wins with a " + p1_card[0] + " of " + p1_card[1] + " versus a " + p2_card[0] + " of " + p2_card[1])
    elif card_comparison(p1_card,p2_card) == 2:
        p2_deck.extend([p2_card,p1_card])
        print("P2 wins with a " + p2_card[0] + " of " + p2_card[1] + " versus a " + p1_card[0] +" of " + p1_card[1])  
    else:
        print("BOTH P1 AND P2 PLAY A " + p1_card[0] + ", ITS TIME FOR WAR!!!!!")
        wait(mode)
        war_card_pile.extend([p1_card,p2_card])
        return war(p1_deck,p2_deck)

def war(p1_deck,p2_deck):
    """Handle the 'war' scenario when cards are equal.
		recall the rules of war, both players put 3 cards face down, 
		then both players flip face up a 4th card. The player with the stronger
		card takes all the cards.		
	"""
    # Your code here
    # The way I'm handling war is that each player puts up to three cards into the "war_pile", but, if they have less than 3 cards to play, they will put as many as they can so that they still have one left to play. IF, the card that was played to start the war was the last card in that player's deck, then they have no more cards and only then do they lose
    p1_war_cards = []

    for x in p1_deck:
        if len(p1_deck) == 1:
            break
        elif p1_deck.index(x) < 3:
            p1_war_cards.append(p1_deck.pop(0))
        else:
            break

    p2_war_cards = []

    for x in p2_deck:
        if len(p2_deck) == 1:
            break
        elif p2_deck.index(x) < 3:
            p2_war_cards.append(p2_deck.pop(0))
        else:
            break

    war_card_pile.extend(p1_war_cards)
    war_card_pile.extend(p2_war_cards)
    
    print("P1's " + str(len(p1_war_cards)) + " cards for the war are ")
    for x in p1_war_cards:
        if p1_war_cards.index(x) < 3:
            time.sleep(0.05)
            print("The " + p1_war_cards[p1_war_cards.index(x)][0] + " of " + p1_war_cards[p1_war_cards.index(x)][1])   
        else:
            break

    wait(mode)
    print("P2's " + str(len(p2_war_cards)) + " cards for the war are ")
    for x in p2_war_cards:
        if p2_war_cards.index(x) < 3:
            time.sleep(0.05)
            print("The " +  p2_war_cards[p2_war_cards.index(x)][0]  + " of " +  p2_war_cards[p2_war_cards.index(x)][1])   
        else:
            break

    wait(mode)
    print("The winner of the war is... ")
    time.sleep(0.05)
    print("...")
    time.sleep(0.05)
    print("...") 
    wait(mode)

    if len(p1_deck) == 0:
        print("P2 because P1 has run out of cards!")
    elif len(p2_deck) == 0:
        print("P1 because P2 has run out of cards!")
    else:

        p1_card = p1_deck.pop(0)
        p2_card = p2_deck.pop(0)

        war_card_pile.extend([p1_card,p2_card])

        if card_comparison(p1_card,p2_card) == 1:
            p1_deck.extend(war_card_pile)
            war_card_pile.clear()
            print("P1! with a " + p1_card[0] + " of " + p1_card[1] + " versus a " + p2_card[0] + " of " + p2_card[1] + "!")
        elif card_comparison(p1_card,p2_card) == 2:
            p2_deck.extend(war_card_pile)
            war_card_pile.clear()
            print("P2! with a " + p2_card[0] + " of " + p2_card[1] + " versus a " + p1_card[0] +" of " + p1_card[1] + "!")  
        else:
            print("BOTH P1 AND P2 PLAY A " + p1_card[0] + ", ITS TIME FOR WAR AGAIN!!!!!")
            wait(mode)
            return war(p1_deck,p2_deck)

def play_game():
    """Main function to run the game."""
    # Your code here 
    
    while True:
        if len(p1_deck) == 0:
            print("P2 wins!")
            break
        elif len(p2_deck) == 0:
            print("P1 wins!")
            break
        else:
            play_round(p1_deck,p2_deck)

# Setting the game speed

# Function that waits in FAST or SLOW mode, or prompts input in MANUAL mode

def wait(mode):
    if mode == "FAST" or mode == "fast":
        time.sleep(0.01)
    elif mode == "SLOW" or mode == "slow":
        time.sleep(1)
    else: 
        word = input()
        if word == "cards" or word == "CARDS":
            print("P1's cards: " + str(len(p1_deck)) + " P2's cards: " + str(len(p2_deck)))
            print()

while True:

    mode = input("Type 'FAST' for fast mode, 'SLOW' for slow mode, or 'MANUAL' for manual mode ")

    if mode == "FAST" or mode =="fast":
        break
    elif mode == "SLOW" or mode == "slow":
        break
    elif mode == "MANUAL" or mode == "manual":
        print()
        print("Press enter to go to the next line, or type 'CARDS' to also see both player's decks")
        break
    else:
        print("Invalid choice, try again")

# Call the main function to start the game
play_game()
