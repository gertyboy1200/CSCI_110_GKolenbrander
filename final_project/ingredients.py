# Ingredient class and related functions for "The Quacks of Quedlinburg" implementation


class Ingredient:
    def __init__(self, type, color, value, cost, bonus=""):
        self.type = type
        self.color = color
        self.value = value
        self.cost = cost
        self.bonus = bonus

    def __str__(self):
        return (
            f"Type: {self.type}, Color: {self.color}, "
            f"Value: {self.value}, Cost: {self.cost}, Bonus: {self.bonus}"
        )


# Factory function to create Ingredient instances
def create_ingredient(type, color, value, cost, bonus=""):
    return Ingredient(type, color, value, cost, bonus)


# Returns a list of all possible ingredient types in the game
def get_ingredients():
    all_ingredients = [
        # Garlic (White) - Basic ingredient
        create_ingredient("garlic_1", "white", 1, 0),
        create_ingredient("garlic_2", "white", 2, 0),
        create_ingredient("garlic_3", "white", 3, 0),
        # Pumpkin (Orange) - No special bonus
        create_ingredient("pumpkin_1", "orange", 1, 3),
        # Toadstool (Red) - Bonus movement if orange chips are in pot
        create_ingredient(
            "toadstool_1", "red", 1, 6, "Move extra if orange chips are present"
        ),
        create_ingredient(
            "toadstool_2", "red", 2, 10, "Move extra if orange chips are present"
        ),
        create_ingredient(
            "toadstool_4", "red", 4, 16, "Move extra if orange chips are present"
        ),
        # Mandrake (Yellow) - Next drawn chip moves twice as far
        create_ingredient(
            "mandrake_1", "yellow", 1, 9, "Next drawn chip moves twice as far"
        ),
        create_ingredient(
            "mandrake_2", "yellow", 2, 13, "Next drawn chip moves twice as far"
        ),
        create_ingredient(
            "mandrake_4", "yellow", 4, 19, "Next drawn chip moves twice as far"
        ),
        # Garden Spider (Green) - Gains rubies if in last or second-to-last position
        create_ingredient(
            "garden_spider_1",
            "green",
            1,
            4,
            "Gains ruby if last or second-to-last chip",
        ),
        create_ingredient(
            "garden_spider_2",
            "green",
            2,
            8,
            "Gains ruby if last or second-to-last chip",
        ),
        create_ingredient(
            "garden_spider_4",
            "green",
            4,
            14,
            "Gains ruby if last or second-to-last chip",
        ),
        # Ghost’s Breath (Purple) - Bonus VPs/rubies based on quantity
        create_ingredient(
            "ghosts_breath_1",
            "purple",
            1,
            9,
            "More purple chips grant extra victory points and rubies",
        ),
        # Crow Skull (Blue) - Bonus ruby if placed on ruby space
        create_ingredient(
            "crow_skull_1", "blue", 1, 4, "Grants ruby if placed on a ruby space"
        ),
        create_ingredient(
            "crow_skull_2", "blue", 2, 8, "Grants ruby if placed on a ruby space"
        ),
        create_ingredient(
            "crow_skull_4", "blue", 4, 14, "Grants ruby if placed on a ruby space"
        ),
    ]
    return all_ingredients


# Adds starting ingredients to a player's bag
def initialize_bag(player):
    all_ingredients = get_ingredients()

    # Add starting ingredients (hardcoded default setup)
    player.bag.append(all_ingredients[0])
    player.bag.append(all_ingredients[0])
    player.bag.append(all_ingredients[0])
    player.bag.append(all_ingredients[0])
    player.bag.append(all_ingredients[1])
    player.bag.append(all_ingredients[1])
    player.bag.append(all_ingredients[2])
    player.bag.append(all_ingredients[3])
    player.bag.append(all_ingredients[10])  # garden_spider_1


# Dispatches the appropriate action based on the ingredient's color
def do_ingredient_action(matching_ingredient, player):
    print("ingredient", matching_ingredient)

    if matching_ingredient.color == "white":
        garlic(matching_ingredient, player)
    elif matching_ingredient.color == "orange":
        pumpkin(matching_ingredient, player)
    elif matching_ingredient.color == "yellow":
        mandrake(matching_ingredient, player)
    elif matching_ingredient.color == "green":
        garden_spider(matching_ingredient, player)
    elif matching_ingredient.color == "red":
        toadstool(matching_ingredient, player)
    elif matching_ingredient.color == "purple":
        ghosts_breath(matching_ingredient, player)
    elif matching_ingredient.color == "blue":
        crow_skull(matching_ingredient, player)
    else:
        print("ERRORRRRR")


# Garlic: Simple movement and explosion risk
def garlic(matching_ingredient, player):
    player.explosion_count += matching_ingredient.value
    if player.mandrake_marker == 1:
        player.droplet_position += matching_ingredient.value * 2
        player.mandrake_marker = 0
    elif player.mandrake_marker == 0:
        player.droplet_position += matching_ingredient.value
    else:
        print("ERROR")
    return player


# Pumpkin: Basic chip with no effect other than movement
def pumpkin(matching_ingredient, player):
    if player.mandrake_marker == 1:
        player.droplet_position += matching_ingredient.value * 2
        player.mandrake_marker = 0
    elif player.mandrake_marker == 0:
        player.droplet_position += matching_ingredient.value
    else:
        print("ERROR")
    return player


# Toadstool: Gains bonus movement depending on number of orange chips in pot
def toadstool(matching_ingredient, player):
    if player.mandrake_marker == 1:
        player.droplet_position += matching_ingredient.value * 2
        player.mandrake_marker = 0
    elif player.mandrake_marker == 0:
        player.droplet_position += matching_ingredient.value
    else:
        print("ERROR")

    # Count orange chips already in the pot
    total_orange_in_pot = sum(1 for chip in player.pot if chip.color == "orange")

    if total_orange_in_pot == 1 or total_orange_in_pot == 2:
        player.droplet_position += 1
    elif total_orange_in_pot >= 3:
        player.droplet_position += 2
    else:
        print("you had no orange chips, no bonus")
    return player


# Mandrake: Sets marker to double the next chip's movement
def mandrake(matching_ingredient, player):
    if player.mandrake_marker == 1:
        player.droplet_position += matching_ingredient.value * 2
        player.mandrake_marker = 0
    elif player.mandrake_marker == 0:
        player.droplet_position += matching_ingredient.value
    else:
        print("ERROR")

    player.mandrake_marker = 1
    return player


# Garden Spider: Only its position matters in the pot (evaluated elsewhere)
def garden_spider(matching_ingredient, player):
    if player.mandrake_marker == 1:
        player.droplet_position += matching_ingredient.value * 2
        player.mandrake_marker = 0
    elif player.mandrake_marker == 0:
        player.droplet_position += matching_ingredient.value
    else:
        print("ERROR")
    return player


# Ghost’s Breath: Bonus effects based on quantity, applied in evaluation phase
def ghosts_breath(matching_ingredient, player):
    if player.mandrake_marker == 1:
        player.droplet_position += matching_ingredient.value * 2
        player.mandrake_marker = 0
    elif player.mandrake_marker == 0:
        player.droplet_position += matching_ingredient.value
    else:
        print("ERROR")
    return player


# Crow Skull: Bonus awarded only if placed on a ruby space (checked elsewhere)
def crow_skull(matching_ingredient, player):
    if player.mandrake_marker == 1:
        player.droplet_position += matching_ingredient.value * 2
        player.mandrake_marker = 0
    elif player.mandrake_marker == 0:
        player.droplet_position += matching_ingredient.value
    else:
        print("ERROR")
    return player
