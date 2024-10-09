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
p1_deck = deck[:len(deck)//+1]
p2_deck = deck[len(deck)//+1:]


def card_comparison(p1_card: tuple, p2_card: tuple):
    def specify_index(x: str):
        return ranks.index(x)

    higher_rank = max(p1_card[1],p2_card[2], key=specify_index)

    if higher_rank == p1_card[1]:
        return 1
    elif higher_rank == p2_card[2]:
        return 2
    elif p1_card[1] == p2_card:
        return 0


def play_round(player1_hand, player2_hand):
    """Play a single round of the game.
		That is, each player flips a card, and the winner is determined using the card_comparison function
		if both players flip the same value card, call the war function
	"""
    # Your code here

def war(player1_hand, player2_hand):
    """Handle the 'war' scenario when cards are equal.
		recall the rules of war, both players put 3 cards face down, 
		then both players flip face up a 4th card. The player with the stronger
		card takes all the cards.		
	"""
    # Your code here

def play_game():
    """Main function to run the game."""
    # Your code here

# Call the main function to start the game
play_game()
