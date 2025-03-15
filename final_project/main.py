import random
import draw_ingredients
import os

import ingredients

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

class Player:
    def __init__(player, name):
        player.name = name
        player.ingredients = [
        "garlic_1", "garlic_1", "garlic_1", "garlic_1",
        "garlic_2", "garlic_2", "garlic_3"]  # List of ingredients (ingredients)
        player.rubies = 0  # Currency used in the game
        player.droplet_position = 0  # Starting position in the pot
        player.victory_points = 0  # Total victory points

    def add_ingredient(player, ingredients):
        player.ingredients.append(ingredients)

    def gain_rubies(player, amount):
        player.rubies += amount

    def move_droplet(player, spaces):
        player.droplet_position += spaces

    def gain_victory_points(player, points):
        player.victory_points += points

    def __str__(player):
        return (f"Player: {player.name}, Rubies: {player.rubies}, "
                f"Droplet Position: {player.droplet_position}, "
                f"Victory Points: {player.victory_points}, "
                f"Ingredients: {player.ingredients}")

player1 = Player("Garrett")


all_ingredients = [
    ingredients.create_ingredient("garlic", 1, 0),
    ingredients.create_ingredient("garlic", 2, 0),
    ingredients.create_ingredient("garlic", 3, 0),
    ingredients.create_ingredient("pumpkin", 1, 3),

    # Toadstool (Red) - Moves extra if orange chips are present
    ingredients.create_ingredient("toadstool", 1, 6, "Move extra if orange chips are present"),
    ingredients.create_ingredient("toadstool", 2, 10, "Move extra if orange chips are present"),
    ingredients.create_ingredient("toadstool", 4, 16, "Move extra if orange chips are present"),

    # Mandrake (Yellow) - Doubles movement of next drawn chip
    ingredients.create_ingredient("mandrake", 1, 9, "Next drawn chip moves twice as far"),
    ingredients.create_ingredient("mandrake", 2, 13, "Next drawn chip moves twice as far"),
    ingredients.create_ingredient("mandrake", 4, 19, "Next drawn chip moves twice as far"),

    # Garden Spider (Green) - Gains rubies if last or second-to-last chip
    ingredients.create_ingredient("garden_spider", 1, 4, "Gains ruby if last or second-to-last chip"),
    ingredients.create_ingredient("garden_spider", 2, 8, "Gains ruby if last or second-to-last chip"),
    ingredients.create_ingredient("garden_spider", 4, 14, "Gains ruby if last or second-to-last chip"),

    # Ghost’s Breath (Purple) - Grants victory points and bonuses based on quantity
    ingredients.create_ingredient("ghosts_breath", 1, 9, "More purple chips grant extra victory points and rubies"),

    # Crow Skull (Blue) - Grants ruby if placed on a ruby space
    ingredients.create_ingredient("crow_skull", 1, 4, "Grants ruby if placed on a ruby space"),
    ingredients.create_ingredient("crow_skull", 2, 8, "Grants ruby if placed on a ruby space"),
    ingredients.create_ingredient("crow_skull", 4, 14, "Grants ruby if placed on a ruby space"),
]

for ingredient in all_ingredients:
    print(ingredient)


draw_ingredients.randomize_ingredients(player1.ingredients)
while True:
    user_input = input("would you like to draw an ingredient?")

    if user_input != 'y':
        break

    if draw_ingredients.draw_ingredient(player1.ingredients) == None:
        print("Bag is empty. EXITING!!!!")
        break

