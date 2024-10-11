# Import necessary modules
import random

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
    p1_card = player1_hand.pop(0)
    p2_card = player2_hand.pop(0)
    result = card_comparison(p1_card, p2_card)
    if result == 1:
        p1_deck.extend([p1_card, p2_card])
    elif result == 2:
        p2_deck.extend([p1_card, p2_card])
    else:
        print('WAR !!!!!')
        if len(player1_hand) >= 4 and len(player2_hand) >= 4:
            war(player1_hand, player2_hand, p1_card, p2_card)
        else:
            return 'Player 1 won' if len(p1_deck) > len(p2_deck) else 'Player 2 won'

    return result


def war(player1_hand, player2_hand, p1_card, p2_card):
    p1_triplet = [p1_card]
    p2_triplet = [p2_card]
    for num in range(4):
        p1_triplet.append(player1_hand.pop(0))
        p2_triplet.append(player2_hand.pop(0))

    result = card_comparison(p1_triplet[-1], p2_triplet[-1])
    if result == 0:
        war(player1_hand,player2_hand, p1_triplet[-1], p2_triplet[-1])
    elif result == 1:
        p1_deck.extend(p1_triplet+p2_triplet)
    elif result == 2:
        p2_deck.extend(p1_triplet+p2_triplet)

    return result


def play_game():
    result = 0
    while p1_deck != [] and p2_deck != []:
        result = play_round(p1_deck, p2_deck)
    print(len(p1_deck), len(p2_deck))
    return 'Player 1 won' if p1_deck != [] else 'Player 2 won'


print(play_game())
