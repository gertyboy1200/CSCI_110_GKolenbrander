import random


def randomize_bag(player):
    random.shuffle(player.bag)
    return player

    
def draw_ingredient(player):
    if not player.bag: 
        return
    drawn = player.bag.pop()
    player.pot.append(drawn)
    return drawn

def reset_round(player):
    player.bag.extend(player.pot)    # Put everything back in the bag
    player.pot.clear()             # Clear the pot

