import random
import draw_ingredients
import os

import ingredients
import player

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


player1 = player.Player("Garrett")

all_ingredients = ingredients.get_ingredients()

round = 1

explosion_number = 0

with open("game_log.txt", "w") as log_file:
    log_file.write("Game Log Started\n")
    log_file.write("================\n")


draw_ingredients.randomize_ingredients(player1.ingredients)
while True:
    user_input = input("would you like to draw an ingredient?")

    if user_input != 'y':
        break

    if player1.explosion_count > 7:
        print("your explosion count was", player1.explosion_count)
        break

    drawn_ingredient = draw_ingredients.draw_ingredient(player1.ingredients)
    if drawn_ingredient is None:
        print("Bag is empty. EXITING!!!!")
        break
    else:
        matching_ingredient = next((ingredient for ingredient in all_ingredients if ingredient.type == drawn_ingredient), None)
        with open("game_log.txt", "a") as log_file:
            if matching_ingredient:
                ingredients.do_ingredient_action(matching_ingredient, player1)
                log_file.write("Drawn ingredient details:\n")
                log_file.write(str(matching_ingredient) + "\n")
                print()
                print(player1)
                print()
            else:
                print("Ingredient not found in the class")

    


