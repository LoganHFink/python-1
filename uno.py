# Logan Fink, Joey Scozzari, William Poirier 
# Addition: Dont let the player play if they dont have a valid card
# When they can't play something or type out an invalid option, it tells them to try again, and let's them choose again to either draw or play 

import random

colours = ("R","Y","B","G")

ranks = list(range(1,11)) 

deck = [(rank,colour) for rank in ranks for colour in colours]

special_cards = ["+2"]

deck += [(action, colour) for action in special_cards for colour in colours]

random.shuffle(deck)

def main_loop(p1_hand,p2_hand,face_up,deck):
 
    # When current_turn = 0, p1. When current_turn = 1, p2.
    current_turn = 0

    while len(p1_hand) > 0 and len(p2_hand) > 0 and len(deck) > 1:
        
        if current_turn == 0: # P1's turn        

            print(f"It is player 1's turn")
            print(f"The face up card is {face_up}")
            print(f"Player 1's hand is {p1_hand}")
        
            current_turn = 1

            while True:
                print("Enter P to play a card, or D to draw a card ")
                choice = input()

                if choice == "P" or choice == "p": # Player wants to play
                    print("Choose a card to play by it's index (starting at 0) ")
                    index = int(input())
                    is_valid = valid_play(face_up,p1_hand[index])
                    if is_valid and p1_hand[index] == "+2":
                        face_up = p1_hand.pop(index)
                        p2_deck.extend([deck.pop[0],deck.pop[0]])
                        break
                    elif is_valid:
                        face_up = p1_hand.pop(index)
                        break
                    else:
                        print("Invalid card, try again")

                elif choice == "D" or choice == "d": # Player wants to draw
                    p1_hand.append(deck.pop(0))
                    break

                else:
                    print("Invalid input, try again")
        else: # AI's turn

            current_turn = 0

            print("It is the AI's turn ")

            card_played = ()
                        
            for card in p2_hand:
                if valid_play(face_up,card) and card[0] == "+2":
                    p1_hand.extend([deck.pop(0),deck.pop(0)])

                    card_played = (p2_hand.pop(p2_hand.index(card)))
                    face_up = card_played

                    break
                elif valid_play(face_up,card):

                    card_played = (p2_hand.pop(p2_hand.index(card)))
                    face_up = card_played

                    break
            if len(card_played) > 0:
                print(f"The AI has played {face_up}")

                card_played = ()

            else:
                p2_hand.append(deck.pop(0))
                print("The AI has drawn a card")

    if len(p1_hand) <= 0:
        print("P1 has won since they have no more cards!")
    elif len(p2_hand) <=0:
        print("The AI has won since it has no more cards!")
    else:
        print("The deck is empty, the game is over ")

def valid_play(face_up,card_chosen):
    return face_up[0] == card_chosen[0] or face_up[1] == card_chosen[1]

def start_game(deck):

    p1_hand = [deck.pop(0) for _ in range(7)]
    p2_hand = [deck.pop(0) for _ in range(7)]
    face_up = deck.pop(0)

    main_loop(p1_hand,p2_hand,face_up,deck)

start_game(deck)
