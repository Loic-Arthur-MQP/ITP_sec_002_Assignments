import random
import time

colours = ('red', 'blue', 'green', 'yellow', 'wild')
ranks = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+2', 'skip', 'reverse')
wilds_rank = ('+4', 'wild', 'shuffle hands', 'exchange hands', "Draw 3 if you can't play", 'I can play another turn')

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

whose_turn = random.choice([0, 1]) # we take 0 = computer , 1 = player


def computer_play(com_hand: list, central_card: tuple):
    for card in com_hand:
        if card[0] == central_card[0] or card[1] == central_card[1]:
            discard_pile.append(com_hand.pop(com_hand.index(card)))
            break
        elif card in power_cards:
            if card[1] == 'wild':
                action_power_cards()
            else:
                action_power_cards()
            break
        elif card in special_cards:
            action_special_cards()
        break


def valid_play(p_hand: list, central_card: tuple):
    time.sleep(1)
    print(p_hand)
    play_decision = input('Play (1) or Draw (0) : ') # call uno, call out a player  
    if play_decision:
        time.sleep(0.5)
        p_choice = int(input('Choose which card to play : ')) - 1
        p_card = p_hand.pop(p_choice)
        if p_card in special_cards:
            action_special_cards(p_card)  # calling function to implement the action card

        elif p_card in power_cards:
            valid_colour = action_power_cards(p_card) 
            return valid_colour

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


def change_colour(_whose_turn):
    com_colours = [com_deck[_][0] for _ in range(len(com_deck)) if com_deck[_][0] in colours[:-1]]
    colour_choice = input('Choose the next colour: blue(b) green(g) red(r) yellow(y) -> ') if whose_turn else random.choice[com_colours]

    player_colours = ('r','b','g', 'y')
    colour_choice = colours[player_colours.index(colour_choice)]
    return colour_choice


def action_power_cards(card, _whose_turn):  # implementing Action cards for power_cards
    player = who_is_playing(not whose_turn)
    colour_choice = change_colour(_whose_turn)
    
    if card[1] == '+4':
        player.extend([deck.pop(0) for _ in range(4)])i
        colour_choice = change_colour(_whose_turn)

    else:
        player_colours = ('r','b','g', 'y')
        colour_choice = change_colour(_whose_turn)
        
    return colour_choice


def action_special_cards(card, _whose_turn):  # implementing Action cards for special cards
    player = who_is_playing(_whose_turn)
    colour_choice = change_colour(_whose_turn
    if card[1] == wilds_ranks[4]:
        player.append(card)
    elif card[1] == wilds_rank[5]:
        whose_turn = (whose_turn + 1) % 2 # try to change this to make whose turn not to change here
                                  return colour_choice 


def who_is_playing(_whose_turn):
    return p_deck if _whose_turn else com_deck

def main_game_run():
    while p_deck and com_deck:
        while whose_turn == 1:
            valid_play()
        while whose_turn == 2:
            computer_play()
