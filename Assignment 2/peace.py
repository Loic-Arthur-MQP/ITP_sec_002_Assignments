"""
WAR is played with two players using a standard 52-card deck. The deck is divided equally, with each player receiving 26

Gameplay:
Both players simultaneously reveal the top card of their pile.
The player with the higher card takes both cards and places them at the bottom of their stack.
If the cards are of equal value, WAR is declared. Each player places three face-down cards followed by one face-up card.
The player with the higher face-up card wins all the cards in the battle.

Winning:
The game continues until one player has collected all the cards.
The game can also end after a predetermined number of battles, and the player with the most cards wins
(Instructor note : "Ensure that the game continues until one player wins all the cards" (Course website).)
"""

# Import necessary modules
import random
import time

# start message
print('''PEACE
Shuffling the cards ...
    ''')
time.sleep(3)
print('Sharing the cards...')
time.sleep(2)

# Setting up useful English expressions
modifiers = ['One more', 'Another', 'Again!!!', 'Infinite', 'Brutal', 'Non stop', 'An extra', 'A further', 'World',
             'Not Peaceful', 'Continuous', 'Unbreakable', '1000']
modifiers2 = ['Real fighting time', 'Prepare your best fighters', 'The Outstanding Duel !', 'Lightening time',
              'Come on!', 'BROUHAHA', 'DOWN CARDS', 'Cardrupting Period', 'Cardilicious', 'Bubble Up']
response = ['YES', 'Yes', 'yes', 'yeah', 'Yeah', 'YEAH', 'y', 'Y', 'oui']

# Create and splitting deck of card
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

deck = [(suit, rank) for suit in suits for rank in ranks[:-2]]
random.shuffle(deck)

p1_deck = deck[:len(deck) // 2]
p2_deck = deck[len(deck) // 2:]
p1_quintuplets = []  # deck that holds the wars' card
p2_quintuplets = []
war_chain = [1]  # determines if cards are to be pop from players hand during war, []-> war chain, [1]-> no chain


# Creating the game's functions and mechanism
def card_comparison(p1_card: tuple, p2_card: tuple):
    higher_rank = max(p1_card[1], p2_card[1], key=ranks.index)
    if p1_card[1] == p2_card[1]:
        return 0
    elif higher_rank == p1_card[1]:
        return 1
    elif higher_rank == p2_card[1]:
        return 2


def play_round(player1_hand: list, player2_hand: list):
    print('\nRound start')
    time.sleep(0.5)
    p1_card = player1_hand.pop(0)
    p2_card = player2_hand.pop(0)
    print(f'{p1_card} ⚡🆚⚡ {p2_card}')
    result = card_comparison(p1_card, p2_card)
    if result == 1:
        p1_deck.extend([p2_card, p1_card])
    elif result == 2:
        p2_deck.extend([p1_card, p2_card])
    else:  # when result = 0
        time.sleep(0.5)
        print('\nWAR !!!!')
        time.sleep(0.5)
        result = war(player1_hand, player2_hand, p1_card, p2_card, p1_quintuplets, p2_quintuplets)
    if result:
        time.sleep(0.5)
        print(f'Player {result} won the round\n ')
    return result


def war(player1_hand, player2_hand, p1_card, p2_card, war_deck1, war_deck2):
    time.sleep(0.5)
    print(f'{random.choice(modifiers2)}')
    time.sleep(3.5)
    if war_chain:
        war_deck1.append(p1_card)
        war_deck2.append(p2_card)
    else:
        war_chain.append(1)  # so that when it's already on war, players directly put faced down cards
        # we don't want to append p1 and p2 to war deck when it's already there.

    if len(player1_hand) >= 4 and len(player2_hand) >= 4:
        for num in range(4):
            war_deck1.append(player1_hand.pop(0))
            war_deck2.append(player2_hand.pop(0))
    else:
        rest1 = [p1_deck.pop(0) for x in range(len(p1_deck))]
        rest2 = [p2_deck.pop(0) for x in range(len(p2_deck))]

        if len(rest1) == len(rest2):
            return 0
        return 1 if len(rest1) > len(rest2) else 2

    print(f'{war_deck1[-1]} ⚡🆚⚡ {war_deck2[-1]}')  # the 4 card of war deck (face up card) fight together.
    result = card_comparison(war_deck1[-1], war_deck2[-1])

    if result == 0:
        war_chain.remove(1)
        time.sleep(2)
        print(f'\n{random.choice(modifiers)} WAR !!!!')
        war(player1_hand, player2_hand, war_deck1[-1], war_deck2[-1], war_deck1, war_deck2)
    elif result == 1:
        p1_deck.extend(war_deck2 + war_deck1)
        p1_quintuplets.clear(), p2_quintuplets.clear() # clear war deck for future fights
    elif result == 2:
        p2_deck.extend(war_deck1 + war_deck2)
        p1_quintuplets.clear(), p2_quintuplets.clear()

    return result


def play_game():
    game_count = 0
    count = 0
    result = 0

    while p1_deck != [] and p2_deck != []:
        result = play_round(p1_deck, p2_deck)
        print(result)
        time.sleep(2)
        count += 1
        game_count += 1
        if count >= 52:
            ask_shuffle = input(
                "The game's not ending!, It might be annoying.Do you want to shuffle both of your cards?\n ")
            if ask_shuffle in response:
                random.shuffle(p1_deck)
                random.shuffle(p2_deck)
                time.sleep(0.5)
            count = 0
        if game_count >= 100:
            ask_end = input('You have been playing for some time now. Do you want to end ?\n ')
            if ask_end in response:
                print('Nice game')
                break
            else:
                print('Go Crazy')
                game_count = 0
                time.sleep(0.5)

    if not result:
        return '\n WHAT A DRAW !'
    else:
        return f'Player {result} won the game'


print(play_game())
