import ingredients  # Module that contains Ingredient class and ingredient-related functions
import os  # For clearing the terminal screen


class Store:
    def __init__(self):
        # Initialize the store with a full list of available ingredients (chips)
        self.stock = ingredients.get_ingredients()  # List of all available ingredients

    def list_items(self):
        # Display all available chips in the store with their index number
        print("Available Chips in Store:")
        for idx, ingredient in enumerate(self.stock, 1):
            print(f"{idx}. {ingredient}")

    def buy_chip(self, player, ingredient_index):
        # Attempt to sell a chip to the player given the chip's index in stock
        if 0 <= ingredient_index < len(self.stock):
            chip = self.stock[ingredient_index]
            # Check if the player has enough money to buy the chip
            if player.money >= chip.cost:
                player.money -= chip.cost  # Deduct cost from player's money
                player.bag.append(chip)  # Add the purchased chip to player's bag
                print(f"{player.name} bought {chip.type} for ${chip.cost}")
            else:
                # Inform player they lack sufficient funds
                print("Not enough money.")
        else:
            # Inform player the selected chip index is invalid
            print("Invalid chip selection.")


def clear_screen():
    # Clear the console screen (compatible with Windows and Unix-like OS)
    os.system("cls" if os.name == "nt" else "clear")


def the_store_ui(current_player_evaluating, the_store, board_data):
    # Update the player's money based on their current droplet position on the board
    current_player_evaluating.money = board_data[
        current_player_evaluating.droplet_position
    ][1]

    bought_colors = []  # Track colors of chips already bought this turn to enforce no duplicates
    purchases = 0  # Count number of chips purchased this turn

    while purchases < 2:  # Allow the player to buy up to two chips
        clear_screen()  # Clear the screen to keep UI clean
        print(f"Store - Buy Chip {purchases + 1}")
        print(f"Current Money: {current_player_evaluating.money}")
        the_store.list_items()  # Show available chips in the store

        chip_choice = input("Enter the number of the chip to buy or 'N' to skip: ")

        if chip_choice.lower() == "n":
            # Player opts to skip buying more chips
            break

        try:
            # Convert input to zero-based index
            chip_index = int(chip_choice) - 1
            selected_chip = the_store.stock[chip_index]

            # Enforce rule: cannot buy two chips of the same color in one turn
            if selected_chip.color in bought_colors:
                print("You cannot buy two chips of the same color!")
                input("Press enter to continue")
                continue  # Prompt player again without counting this as a purchase

            # Check if player has enough money to buy the selected chip
            if selected_chip.cost > current_player_evaluating.money:
                print("You don't have enough money for that chip.")
                input("Press enter to continue")
                continue  # Prompt player again without counting this as a purchase

            # Purchase successful: process transaction and update state
            the_store.buy_chip(current_player_evaluating, chip_index)
            bought_colors.append(
                selected_chip.color
            )  # Track color to prevent duplicates
            purchases += 1
            input("Press enter to continue")

        except (ValueError, IndexError):
            # Handle invalid input such as non-numeric or out-of-range choices
            print("Invalid input. Try again.")
            input("Press enter to continue")
