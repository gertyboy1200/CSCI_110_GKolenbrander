import random
import draw_ingredients
import os

import ingredients
import player
import evaluation
import store

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

filename = 'board.txt'

all_ingredients = ingredients.get_ingredients()
the_store = store.Store()

with open("game_log.txt", "w") as log_file:
    log_file.write("Game Log Started\n")
    log_file.write("================\n")

clear_screen()
    
num_players = int(input("Enter the number of players: "))
players = []
for i in range(num_players):
    name = input(f"Enter name for Player {i + 1}: ")
    new_player = player.Player(name)
    ingredients.initialize_bag(new_player)
    players.append(new_player)


for round in range(2):

    #drawing phase
    for current_player_drawing in players:
        clear_screen()
        print("ROUND: ", round + 1)
        print(f"\n--- {current_player_drawing.name}'s turn ---\n")
        
        while True:
            user_input = input("Would you like to draw an ingredient? (y/n): ").lower()

            if current_player_drawing.explosion_count > 7:
                print(f"Your explosion count was {current_player_drawing.explosion_count}")
                break

            if user_input != 'y':
                break
            draw_ingredients.randomize_bag(current_player_drawing)
            drawn_ingredient = draw_ingredients.draw_ingredient(current_player_drawing)
            if drawn_ingredient is None:
                print("Bag is empty. EXITING!!!!")
                break
            else:
                matching_ingredient = next((ingredient for ingredient in all_ingredients if ingredient.type == drawn_ingredient), None)

                with open("game_log.txt", "a") as log_file:
                    if drawn_ingredient:
                        ingredients.do_ingredient_action(drawn_ingredient, current_player_drawing)
                        log_file.write("Drawn ingredient details:\n")
                        log_file.write(str(drawn_ingredient) + "\n")
                        print()
                        print(current_player_drawing)
                        print()
                    else:
                        print("Ingredient not found in the class")
            
            

    for current_player_evaluating in players:
        clear_screen()
        print(f"Welcome to the evaluation phase, {current_player_evaluating.name}!")
        print("There are 6 sections in the evaluation phase:")
        print("A: Roll the bonus die (if your pot didn't explode).")
        print("B: Resolve chip actions (purple, black, etc.).")
        print("C: Gain rubies based on your final space.")
        print("D: Gain victory points (or choose this if you exploded).")
        print("E: Buy up to 2 chips (choose this if you exploded, instead of D).")
        print("F: Spend 2 rubies to move your droplet forward.")
        input("press enter to continue")



        # section A
        #if current players droplet position is greater than all others roll die
        clear_screen()
        print("PHASE A")

        if all(current_player_evaluating.droplet_position > other.droplet_position for other in players if other != current_player_evaluating):
            print(f"{current_player_evaluating.name} has the farthest droplet!")
            evaluation.bonus_die(current_player_evaluating)
            print(current_player_evaluating)


        input("press enter to continue")
        # section B
        #chip actions
        clear_screen()
        print("PHASE B")





        input("press enter to continue")

        # section C
        #gain rubies if landed on ruby space
        clear_screen()
        print("PHASE C")

             
        board_data = evaluation.read_board_data(filename)
        print(current_player_evaluating)
        if board_data[current_player_evaluating.droplet_position][2] == 1:
            print("YOU GAINED A RUBY")
            current_player_evaluating.rubies += 1
            print(f"You have {current_player_evaluating.rubies} rubies!")
        else:
            print("YOU DIDN'T GAIN A RUBY")

        input("press enter to continue")


        # section D

        #
        if current_player_evaluating.explosion_count > 7:
            clear_screen()
            print("You've EXPLODED. You will not be able to complete all phases of the evaluation phase")
            section_choice = input("You must choose between section D and E: ")

            if section_choice.lower() == "d":
                # Section D
                clear_screen()
                print("PHASE D")
                current_player_evaluating.victory_points += board_data[current_player_evaluating.droplet_position][3]
                input("Press enter to continue")

            elif section_choice.lower() == "e":
                # Section E
                clear_screen()
                print("PHASE E")
                enter_store = input("Would you like to buy a chip? (Y/N): ")

                if enter_store.lower() == "y":
                    store.the_store_ui(current_player_evaluating, the_store, board_data)




        else:
            #section D
            clear_screen()
            print("PHASE D")
            current_player_evaluating.victory_points += board_data[current_player_evaluating.droplet_position][3]
            input("press enter to continue")
            #section E
            
            clear_screen()
            print("PHASE E")

            enter_store = input("Would you like to buy a chip? (Y/N): ")

            if enter_store.lower() == "y":
                store.the_store_ui(current_player_evaluating, the_store, board_data)







        player.reset(current_player_evaluating)
        #player.show_bag(current_player_evaluating)


        input()




    #evaluation phase


        #for position, money, ruby, victory_points in board_data:
        #   print(f"Space {position}: Money = {money}, Ruby = {ruby}, Victory Points = {victory_points}")





