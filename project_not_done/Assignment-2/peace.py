# Import necessary modules
import random

modifiers = ['One more', 'Another', 'Again!!!', 'Infinite', 'Brutal', 'Non stop', 'An extra', 'A further', 'World',
             'Not Peaceful', 'Continuous', 'Unbreakable', '1000']

# Define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

# Create a deck of cards
deck = [(suit, rank) for suit in suits for rank in ranks]

# Shuffle the deck
random.shuffle(deck)

# Split the deck into two hands
p1_deck = deck[:len(deck) // 2]
p2_deck = deck[len(deck) // 2:]
p1_quintuplets = []
p2_quintuplets = []
war_chain = [1]


def card_comparison(p1_card: tuple, p2_card: tuple):
    # noinspection PyTypeChecker
    higher_rank = max(p1_card[1], p2_card[1], key=ranks.index)
    if p1_card[1] == p2_card[1]:
        return 0
    elif higher_rank == p1_card[1]:
        return 1
    elif higher_rank == p2_card[1]:
        return 2


def play_round(player1_hand: list, player2_hand: list):
    print('start')
    p1_card = player1_hand.pop(0)
    p2_card = player2_hand.pop(0)
    result = card_comparison(p1_card, p2_card)
    if result == 1:
        p1_deck.extend([p2_card, p1_card])
    elif result == 2:
        p2_deck.extend([p1_card, p2_card])
    else:
        print('WAR !!!!')
        result = war(player1_hand, player2_hand, p1_card, p2_card, p1_quintuplets, p2_quintuplets)
    return result


def war(player1_hand, player2_hand, p1_card, p2_card, war_deck1, war_deck2):
    if war_chain:
        war_deck1.append(p1_card)
        war_deck2.append(p2_card)
    else:
        war_chain.append(1)

    print(f'tri 1 = {len(war_deck1)}, tri 2 = {len(war_deck2)}, {war_deck1==p1_quintuplets}{war_deck2==p2_quintuplets}')
    if len(player1_hand) >= 4 and len(player2_hand) >= 4:
        for num in range(4):
            war_deck1.append(player1_hand.pop(0))
            war_deck1.append(player2_hand.pop(0))
    else:
        print(f'War\'s {len(p1_deck)}, {len(p2_deck)}')
        rest1 = [p1_deck.pop(0) for x in range(len(p1_deck))]
        rest2 = [p2_deck.pop(0) for x in range(len(p2_deck))]

        if len(rest1) == len(rest2):
            return 0
        return 1 if len(rest1) > len(rest2) else 2

    result = card_comparison(war_deck1[-1], war_deck2[-1])
    if result == 0:
        war_chain.remove(1)
        print(f'{random.choice(modifiers)} WAR !!!!')
        war(player1_hand, player2_hand, war_deck1[-1], war_deck2[-1], p1_quintuplets, p2_quintuplets)
    elif result == 1:
        p1_deck.extend(war_deck2 + war_deck1)
        war_deck1.clear()
        war_deck2.clear()
    elif result == 2:
        p2_deck.extend(war_deck1 + war_deck2)
        war_deck1.clear()
        war_deck2.clear()

    return result


def play_game():
    result = 0
    while p1_deck != [] and p2_deck != []:
        result = play_round(p1_deck, p2_deck)
    print(len(p1_deck), len(p2_deck))
    if not result:
        return 'WHAT A DRAW !'
    else:
        return f'Player {result} won the game'


print(play_game())
