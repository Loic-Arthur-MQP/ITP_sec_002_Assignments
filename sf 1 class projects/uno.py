import random
import time

# ranks and colours in uno
colours = ('red 🔴', 'blue 🔵', 'green 🟢', 'yellow 🟡', 'wild ⚫')
ranks = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+2', 'skip', 'reverse')
wilds_rank = ('+4', 'wild', 'shuffle hands', 'exchange hands', "give you a card", 'can play another turn')

# creating parts of the main deck
# A card is a list with a tuple and a string EX. [('green, '4'), 'green' ].
# first = green / second = 4 / third = green
# The first and second elements are the colour and rank of the card.
# The third element is the colour that can be played un top of that card. I.E when we play a wild card, we must change the colour in the game without changing the card it's self

normal_cards = 2 * [[(colour, rank), colour] for rank in ranks[1:] for colour in colours[:-1]] + [
    [(colour, '0'), colour] for colour in colours[:-1]]
power_cards = 4 * [[(colour, rank), colour] for rank in wilds_rank[:2] for colour in colours[-1:]]
special_cards = [[(colour, rank), colour] for rank in wilds_rank[2:] for colour in colours[-1:]]

deck = normal_cards + power_cards + special_cards  # creating the initial deck
random.shuffle(deck)

# sharing cards
p_deck = [deck.pop(0) for _ in range(7)]
com_deck = [deck.pop(0) for _ in range(7)]


#  creating the central deck-check if the central card is in the normal cards (from 0 to 9)
def choosing_central():
    central_card = deck.pop(0)
    while central_card[0][1] not in ranks[:10]:  # we assume that we can't start with skip or reverse
        deck.append(central_card)
        central_card = deck.pop(0)

    return central_card


f_central_card = choosing_central()
discard_pile = [choosing_central()]
whose_turn = random.choice([False, True])  # we take False(0) = computer , True(1) = player

# start messages
print('UNO'), time.sleep(1)
print('Shuffling cards'), time.sleep(2)
print('Sharing cards'), time.sleep(2)
print('\nSTART'), time.sleep(0.5)
print(f'middle card -----> {discard_pile[-1][0]}')


# Computer plays randomly but satisfies the playing conditions
def computer_play(com_hand: list, central_card: list, _whose_turn):
    played = False  # decides if the computer played or not
    if not played:
        for i, card in enumerate(com_hand):
            if (card[0][1] == central_card[0][1] or card[1] == central_card[1]) and card[0][0] != colours[-1]:  # check if card is valid and is normal
                time.sleep(1), print(f'\ncomputer plays -----> {card[0]}')
                discard_pile.append(com_hand.pop(i))
                played = True

                if card[0][1] == "+2" or card[0][1] == "skip":
                    if com_hand:
                        _whose_turn = coloured_power_card(card, False)
                break

    if not played:
        for i, card in enumerate(com_hand):
            if card in power_cards:
                time.sleep(1), print(f'\ncomputer plays -----> {card[0]}')
                discard_pile.append(com_hand.pop(i))
                played = True
                if com_hand:
                    _whose_turn = wild_power_cards(card, False)
                break

    if not played:
        for i, card in enumerate(com_hand):
            if card in special_cards:
                time.sleep(1), print(f'\ncomputer plays -----> {card[0]}')
                discard_pile.append(com_hand.pop(i))
                played = True
                if com_hand:
                    _whose_turn = wild_special_cards(card, False)
                break

    if not played:
        time.sleep(1), print('\ncomputer draws from deck')
        com_hand.append(deck.pop())

    time.sleep(1.2)
    _whose_turn = not _whose_turn
    return _whose_turn


# Defines how the User will play
def valid_play(p_hand: list, central_card: tuple, _whose_turn: bool):
    time.sleep(0.5)
    print(f'\nHere are your cards'), time.sleep(0.6)
    print('______________________________________________________________________________________________________________________________________________________________')
    print(f'{[f'{i + 1}{(card[0])}' for i, card in enumerate(p_hand)]}')
    print('______________________________________________________________________________________________________________________________________________________________')
    time.sleep(0.5)
    p_choice = int(input('\nChoose the card\'s number to PLAY the card :  Enter 0 to DRAW : ')) - 1
    if p_choice + 1:
        p_card = p_hand.pop(p_choice % len(p_hand))  # makes sure user don't take card more than index

        if p_card in special_cards:
            discard_pile.append(p_card)
            if p_hand:
                _whose_turn = wild_special_cards(p_card, True)  # calling function to implement the action card

        elif p_card in power_cards:
            discard_pile.append(p_card)
            if p_hand:
                _whose_turn = wild_power_cards(p_card, True)  # calling function to implement the action card

        elif p_card[0][1] == central_card[0][1] or p_card[1] == central_card[1]:
            discard_pile.append(p_card)
            if p_card[0][1] == '+2' or p_card[0][1] == 'skip':
                if p_hand:
                    _whose_turn = coloured_power_card(p_card, True)

        else:
            print("You can't play that card! 2 cards penalty")
            time.sleep(0.5)
            p_hand.append(p_card)
            p_hand.append(deck.pop(0))
            p_hand.append(deck.pop(0))

    else:
        print('\nyou draw 1 from deck')
        p_hand.append(deck.pop(0))

    time.sleep(1.2)
    _whose_turn = not _whose_turn
    return _whose_turn


def change_colour(_whose_turn):  # is called when we have a wild card in the game
    com_colours = [com_deck[_][0][0] for _ in range(len(com_deck)) if com_deck[_][0][0] in colours[:-1]]
    time.sleep(0.5)
    colour_choice = input(
        '\nChoose the next colour: blue(b) green(g) red(r) yellow(y) -> ') if _whose_turn else (
        random.choice(com_colours) if com_colours else random.choice(colours[:-1]))

    player_colours = ('r', 'b', 'g', 'y')  # r matches to red in colours in player_colours.index(colour_choice)
    colour_choice = colours[player_colours.index(colour_choice)] if _whose_turn else colour_choice

    if not _whose_turn:
        time.sleep(1), print(f'\ncomputer chose {colour_choice} ')
    return colour_choice


def wild_power_cards(card, _whose_turn):  # implementing Action cards for wild +4 and simple wild
    player = who_is_playing(not _whose_turn)
    colour_choice = change_colour(_whose_turn)
    discard_pile[-1][1] = colour_choice  # Changes the colour for wild cards

    if card[0][1] == '+4':
        time.sleep(2)
        print('computer draw 4 cards') if _whose_turn else print('you draw 4')
        time.sleep(2)
        print('Play again') if _whose_turn else print('Your turn is skipped')
        player.extend([deck.pop(0) for _ in range(4)])
        _whose_turn = not _whose_turn

    return _whose_turn


def wild_special_cards(card, _whose_turn):  # implementing Action cards for special cards
    player = who_is_playing(_whose_turn)
    colour_choice = change_colour(_whose_turn)
    discard_pile[-1][1] = colour_choice  # Changes the colour for wild cards

    if card[0][1] == wilds_rank[-2]:  # give you one of my cards
        if _whose_turn:
            time.sleep(1)
            ans = int(input('\nWhich card do you want to give? ')) - 1
            pur_card = player.pop(ans)
            time.sleep(1.5), print(f'\nYou gave {pur_card}')
        else:
            pur_card = random.choice(com_deck)
            time.sleep(1.5), print(f'\nYou received {pur_card}')
        player = who_is_playing((not _whose_turn))
        player.append(pur_card)

    elif card[0][1] == wilds_rank[-1]:  # I can play another turn
        _whose_turn = not _whose_turn  # try to change this to make whose turn not to change here

    return _whose_turn


def coloured_power_card(card, _whose_turn):
    if card[0][1] == '+2':
        player = who_is_playing(not _whose_turn)
        player.append(deck.pop(0))
        player.append(deck.pop(0))
        time.sleep(1), print('\ncomputer draws 2 cards') if _whose_turn else print('\nYou draw 2')

    time.sleep(0.7), print('\nYou play gain') if _whose_turn else print('\nYour turn is skipped')

    _whose_turn = not _whose_turn
    return _whose_turn


def who_is_playing(_whose_turn):
    return p_deck if _whose_turn else com_deck


# Maintains the game running until one win
def main_game_run(_whose_turn):
    while p_deck and com_deck:
        if len(deck) == 0:
            deck.extend([discard_pile.pop(0) for _ in range(len(discard_pile) - 2)])
            random.shuffle(deck)
        if _whose_turn:
            _whose_turn = valid_play(p_deck, discard_pile[-1], _whose_turn)
            if len(p_deck) == 1:
                time.sleep(1), print("\n>>> YOUR UNO <<<")
            time.sleep(0.7), print(f'middle card -> {discard_pile[-1][0]}')
        else:
            _whose_turn = computer_play(com_deck, discard_pile[-1], _whose_turn)
            if len(com_deck) == 1:
                time.sleep(1), print("\n>>> COMPUTER's UNO <<<")
            time.sleep(0.7), print(f'middle card -> {discard_pile[-1][0]}')

    time.sleep(0.5), print('OUT !!')
    time.sleep(1)
    return f'\nComputer won' if p_deck else f'\nYou won !!'


print(main_game_run(whose_turn))

time.sleep(3)
