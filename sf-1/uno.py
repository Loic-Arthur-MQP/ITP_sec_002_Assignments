def start_game():
    colours = ('red' , 'blue', 'green', 'yellow','white')
    ranks = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '+2', 'skip_turn', 'rotation')
    unranks = ('whites', 'constraints')
    
    deck = [2*(colour, rank) for rank in ranks[1:] for colour in colours[:-1]]
    
