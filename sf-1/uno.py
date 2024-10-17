import random
import time

colours = ('red', 'blue', 'green', 'yellow', 'wild')
ranks = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+2', 'skip', 'reverse')
wilds_rank = ('+4', 'wild', 'shuffle hands', 'exchange hands', 'customizable1', 'customizable2')

normal_cards = 2 * [(colour, rank) for rank in ranks[1:] for colour in colours[:-1]]
power_cards = 4 * [(colour, rank) for rank in wilds_rank[:2] for colour in colours[-1:]]
zero_cards = [(colour, '0') for colour in colours[:-1]]
special_cards = [(colour, rank) for rank in wilds_rank[2:] for colour in colours[-1:]]

deck = normal_cards + power_cards + zero_cards + special_cards
random.shuffle(deck)

def choosing_central():
    central_card = deck.pop(0)
    if central_card[1] in ranks[:10]:
        return central_card
    else:
        deck.append(central_card)
        choosing_central()

discard_pile = [choosing_central()]
p_deck = [deck.pop(0) for _ in range(7)]
com_deck = [deck.pop(0) for _ in range(7)]


whose_turn = random.choice([1,2])

def computer_play(com_hand ,central_card):
    

def valid_play(p_hand, central_card):
    time.sleep(1)
    print(p_hand)
    play_decision = input('Play (1) or Draw (0) : ')
    if play_decision:
        time.sleep(0.5)
        p_choice = int(input('Choose which card to play : ')) - 1
        p_card = p_hand[p_choice]
        if p_card in special_cards:
            action_cards1(p_card) # calling function to implement the action card

        elif p_card in power_cards:
            action_cards2(p_card)
        elif p_card[0] == central_card[0] or p_card[1] == central_card[1]:
            discard_pile.append(p_card)
        else:
            print("You can't play that card! 2 cards penalty")
            time.sleep(0.5)
            p_hand.append(deck.pop(0))
            p_hand.append(deck.pop(0))
            whose_turn = 2
    else:
        p_hand.append(deck.pop(0))
        whose_turn = 2


def action_cards1(card): # implementing Action cards for special cards
    return

def action_cards2(card):  # implementing Action cards for power_cards
    return

def main_game_play():
    while p_deck != [] and com_deck != []:
        while whose_turn == 1:
            valid_play()
        while whose_turn == 2:
            computer_play()
