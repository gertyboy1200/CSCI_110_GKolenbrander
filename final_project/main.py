"""
Quacks of Quedlinburg Game
Author: Garrett Kolenbrander
CSCI 110
Date: 16/5/25

Professor: John Kull
Final Project

More information about the game can be found here:
- https://cdn.1j1ju.com/medias/ba/73/db-the-quacks-of-quedlinburg-rulebook.pdf
- https://www.ultraboardgames.com/the-quacks-of-quedlinburg/ingredients.php
"""

import draw_ingredients
import os
import sys
import ingredients
import player
import evaluation
import store


def clear_screen():
    # Clears the terminal screen depending on the operating system
    os.system("cls" if os.name == "nt" else "clear")


play_again = "y"

while play_again == "y":
    filename = "board.txt"

    # Load ingredients and store
    all_ingredients = ingredients.get_ingredients()
    the_store = store.Store()

    # Start the game log
    with open("game_log.txt", "w") as log_file:
        log_file.write("Game Log Started\n")
        log_file.write("================\n")

    clear_screen()

    # Set up players
    num_players = int(input("Enter the number of players: "))
    players = []
    for i in range(num_players):
        name = input(f"Enter name for Player {i + 1}: ")
        new_player = player.Player(name)
        ingredients.initialize_bag(new_player)
        players.append(new_player)

    board_data = evaluation.read_board_data(filename)

    # Main game loop: 9 rounds
    for round in range(9):
        # Drawing phase
        for current_player_drawing in players:
            clear_screen()
            print("ROUND: ", round + 1)
            print(f"\n--- {current_player_drawing.name}'s turn ---\n")

            while True:
                user_input = input(
                    "Would you like to draw an ingredient? (y/n): "
                ).lower()

                # Stop if player has exploded
                if current_player_drawing.explosion_count > 7:
                    print(
                        f"Your explosion count was {current_player_drawing.explosion_count}"
                    )
                    break

                if user_input != "y":
                    break

                draw_ingredients.randomize_bag(current_player_drawing)
                drawn_ingredient = draw_ingredients.draw_ingredient(
                    current_player_drawing
                )
                if drawn_ingredient is None:
                    print("Bag is empty. EXITING!!!!")
                    break
                else:
                    # Match drawn ingredient with its class
                    matching_ingredient = next(
                        (
                            ingredient
                            for ingredient in all_ingredients
                            if ingredient.type == drawn_ingredient
                        ),
                        None,
                    )

                    with open("game_log.txt", "a") as log_file:
                        if drawn_ingredient:
                            ingredients.do_ingredient_action(
                                drawn_ingredient, current_player_drawing
                            )
                            log_file.write("Drawn ingredient details:\n")
                            log_file.write(str(drawn_ingredient) + "\n")
                            print()
                            print(current_player_drawing)
                            print()
                        else:
                            print("Ingredient not found in the class")

        # Evaluation Phase
        clear_screen()
        print("Welcome to the evaluation phase!")
        print("There are 6 sections in the evaluation phase:")
        print("A: Roll the bonus die (if your pot didn't explode).")
        print("B: Resolve chip actions (purple, black, etc.).")
        print("C: Gain rubies based on your final space.")
        print("D: Gain victory points (or choose this if you exploded).")
        print("E: Buy up to 2 chips (choose this if you exploded, instead of D).")
        print("F: Spend 2 rubies to move your droplet forward.")
        input("press enter to continue")
        clear_screen()
        print("PHASE A")

        # Section A: Bonus die roll for leading players
        non_exploded_players = [p for p in players if p.explosion_count <= 7]

        if non_exploded_players:
            max_position = max(p.droplet_position for p in non_exploded_players)
            eligible_players = [
                p for p in non_exploded_players if p.droplet_position == max_position
            ]
            for p in eligible_players:
                print(f"{p.name} gets to roll the bonus die!")
                evaluation.bonus_die(p)
        else:
            print("No players are eligible to roll the bonus die.")
        input("press enter to continue")

        # Section B–F for each player
        for current_player_evaluating in players:
            evaluation.garden_spider(current_player_evaluating)
            evaluation.ghosts_breath(current_player_evaluating)

            # Section C: Gain rubies
            clear_screen()
            print("PHASE C")
            print(current_player_evaluating)
            if board_data[current_player_evaluating.droplet_position][2] == 1:
                print("YOU GAINED A RUBY")
                current_player_evaluating.rubies += 1
                print(f"You have {current_player_evaluating.rubies} rubies!")
            else:
                print("YOU DIDN'T GAIN A RUBY")

            input("press enter to continue")

            # Sections D & E depending on explosion
            if current_player_evaluating.explosion_count > 7:
                clear_screen()
                print("You've EXPLODED. You will not be able to complete all phases.")
                section_choice = input("You must choose between section D and E: ")

                if section_choice.lower() == "d":
                    current_player_evaluating.victory_points += board_data[
                        current_player_evaluating.droplet_position
                    ][3]

                elif section_choice.lower() == "e":
                    clear_screen()
                    print("PHASE E")
                    enter_store = input("Would you like to buy a chip? (Y/N): ")
                    if enter_store.lower() == "y":
                        store.the_store_ui(
                            current_player_evaluating, the_store, board_data
                        )
            else:
                # Section D: Gain victory points
                current_player_evaluating.victory_points += board_data[
                    current_player_evaluating.droplet_position
                ][3]

                # Section E: Buy chips
                clear_screen()
                print("PHASE E")
                enter_store = input("Would you like to buy a chip? (Y/N): ")
                if enter_store.lower() == "y":
                    store.the_store_ui(current_player_evaluating, the_store, board_data)

            # Section F: Reset for next round
            current_player_evaluating.reset()

    # Determine the winner(s)
    max_score = max(player.victory_points for player in players)
    winners = [player for player in players if player.victory_points == max_score]

    clear_screen()
    print("\n\U0001f389 Game Over! \U0001f389")
    if len(winners) == 1:
        print(f"The winner is {winners[0].name} with {max_score} victory points!")
    else:
        print("It's a tie!")
        for player in winners:
            print(f"- {player.name} with {player.victory_points} points")
    print()
    play_again = input("Would you like to play again?? Y/N: ").lower()


# Simple test function to verify board data loading
def test(did_pass):
    """Print the result of a test"""
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


test(
    evaluation.read_board_data("board_data_test.txt")
    == [(1, 1, 0, 0), (2, 2, 0, 0), (3, 3, 0, 0), (4, 4, 0, 0)]
)
