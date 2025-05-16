import ingredients
import os


class Store:
    def __init__(self):
        self.stock = ingredients.get_ingredients()  # List of all available ingredients

    def list_items(self):
        print("Available Chips in Store:")
        for idx, ingredient in enumerate(self.stock, 1):
            print(f"{idx}. {ingredient}")

    def buy_chip(self, player, ingredient_index):
        if 0 <= ingredient_index < len(self.stock):
            chip = self.stock[ingredient_index]
            if player.money >= chip.cost:
                player.money -= chip.cost
                player.bag.append(chip)
                print(f"{player.name} bought {chip.type} for ${chip.cost}")
            else:
                print("Not enough money.")
        else:
            print("Invalid chip selection.")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def the_store_ui(current_player_evaluating, the_store, board_data):
    current_player_evaluating.money = board_data[
        current_player_evaluating.droplet_position
    ][1]
    bought_colors = []
    purchases = 0

    while purchases < 2:  # Allow up to 2 chips
        clear_screen()
        print(f"Store - Buy Chip {purchases + 1}")
        print(f"Current Money: {current_player_evaluating.money}")
        the_store.list_items()

        chip_choice = input("Enter the number of the chip to buy or 'N' to skip: ")

        if chip_choice.lower() == "n":
            break

        try:
            chip_index = int(chip_choice) - 1
            selected_chip = the_store.stock[chip_index]

            if selected_chip.color in bought_colors:
                print("You cannot buy two chips of the same color!")
                input("Press enter to continue")
                continue

            if selected_chip.cost > current_player_evaluating.money:
                print("You don't have enough money for that chip.")
                input("Press enter to continue")
                continue

            # Successful purchase
            the_store.buy_chip(current_player_evaluating, chip_index)
            bought_colors.append(selected_chip.color)
            purchases += 1
            input()

        except (ValueError, IndexError):
            print("Invalid input. Try again.")
            input("Press enter to continue")
