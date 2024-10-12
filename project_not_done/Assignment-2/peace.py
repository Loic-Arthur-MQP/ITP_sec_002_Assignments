# Import necessary modules
import random

# Define the ranks and suits
ranks = ("2", "3", "4")
suits = ("hearts", "diamonds", "clubs", "spades")

# Create a deck of cards
deck = [(suit, rank) for suit in suits for rank in ranks]

# Shuffle the deck
random.shuffle(deck)

# Split the deck into two hands
p1_deck = deck[:len(deck) // 2]
p2_deck = deck[len(deck) // 2:]
state = 1


def card_comparison(p1_card: tuple, p2_card: tuple):
    def specify_index(x: str):
        return ranks.index(x)

    # noinspection PyTypeChecker
    higher_rank = max(p1_card[1], p2_card[1], key=specify_index)
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
        print('WAR !!!!!')
        if len(player1_hand) >= 4 and len(player2_hand) >= 4:
            war(player1_hand, player2_hand, p1_card, p2_card)
        else:
            return 'Player 1 won' if len(p1_deck) > len(p2_deck) else 'Player 2 won'
    print(f'play\'s {len(p1_deck)}, {len(p2_deck)}')
    print(f'player {result} won the round')
    print('done')
    return result


def war(player1_hand, player2_hand, p1_card, p2_card):
    global state
    print('war fare')
    p1_triplet = [p1_card]
    p2_triplet = [p2_card]
    if len(player1_hand) >= 4 and len(player2_hand) >= 4:
        for num in range(4):
            p1_triplet.append(player1_hand.pop(0))
            p2_triplet.append(player2_hand.pop(0))
    else:
        print('changing state')
        print(f'War\'s {len(p1_deck)}, {len(p2_deck)}')
        print('Player 1 won the game' if len(p1_deck) > len(p2_deck) else 'Player 2 won the game')
        state = 0
        return 0

    result = card_comparison(p1_triplet[-1], p2_triplet[-1])
    if result == 0:
        print('WAR !!!!!!!')
        war(player1_hand, player2_hand, p1_triplet[-1], p2_triplet[-1])
    elif result == 1:
        p1_deck.extend(p2_triplet + p1_triplet)
    elif result == 2:
        p2_deck.extend(p1_triplet + p2_triplet)

    return 1


def play_game():
    while p1_deck != [] and p2_deck != [] and state:
        play_round(p1_deck, p2_deck)
    print(f'state {state}')
    print(len(p1_deck), len(p2_deck))
    return 'Player 1 won the game' if p1_deck != [] else 'Player 2 won the game'


print(play_game())
