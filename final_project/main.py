import random
import draw_ingredients


user_input = 'y'
draw_ingredients.draw_first_ingredient()
while user_input == 'y':
    user_input = input("would you like to draw an ingredient?")

    if draw_ingredients.is_bag_empty():
        print("you have no ingredients in your bag!!!")
        break

    draw_ingredients.draw_ingredients()
