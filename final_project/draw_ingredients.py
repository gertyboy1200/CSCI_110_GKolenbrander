import random


def randomize_bag(player):
    # Shuffle the player's bag randomly to mix ingredients
    random.shuffle(player.bag)
    return player


def draw_ingredient(player):
    # Draw one ingredient from the player's bag and add it to their pot
    if not player.bag:  # If bag is empty, do nothing
        return
    drawn = player.bag.pop()  # Remove and get the last ingredient in the bag
    player.pot.append(drawn)  # Add the drawn ingredient to the pot
    return drawn  # Return the drawn ingredient


def reset_round(player):
    # Move all ingredients from pot back into the bag and empty the pot for next round
    player.bag.extend(player.pot)  # Add pot ingredients back to bag
    player.pot.clear()  # Clear the pot list
