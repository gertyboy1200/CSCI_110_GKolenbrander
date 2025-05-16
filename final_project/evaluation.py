import random
import ingredients


# Reads board configuration from a file and returns a list of tuples.
# Each tuple contains (droplet_position, money, ruby, victory_points)
def read_board_data(filename):
    board_data = []

    with open(filename, "r") as file:
        for line in file:
            # Skip comment lines and empty lines
            if line.startswith("#") or not line.strip():
                continue

            parts = [part.strip() for part in line.split("|")]

            # Convert string parts to integers
            droplet_position = int(parts[0])
            money = int(parts[1])
            ruby = int(parts[2])
            victory_points = int(parts[3])

            board_data.append((droplet_position, money, ruby, victory_points))

    return board_data


# Simulates rolling the bonus die and gives the appropriate reward to the player
def bonus_die(player):
    bonuses = [
        "1 victory point",
        "2 victory points",
        "3 victory points",
        "1 ruby",
        "Advance droplet one space",
        "Draw 1 pumpkin chip and add it to your bag",
    ]

    roll = random.randint(0, 5)
    print(f"You rolled: {bonuses[roll]}")

    if roll == 0:
        player.victory_points += 1
    elif roll == 1:
        player.victory_points += 2
    elif roll == 2:
        player.victory_points += 3
    elif roll == 3:
        player.rubies += 1
    elif roll == 4:
        player.droplet_position += 1
    elif roll == 5:
        # Create and add a pumpkin chip (orange, value 1, no special action)
        pumpkin_chip = ingredients.create_ingredient("pumpkin_1", "orange", 1, 0)
        player.bag.append(pumpkin_chip)


# Checks the last two chips in the pot. For each green chip among them, awards 1 ruby.
def garden_spider(player):
    # Need at least two chips in pot for this to apply
    if len(player.pot) <= 1:
        print("Not enough items in your pot")
        return

    second_player_pot = player.pot.copy()  # Avoid mutating the actual pot
    last_chip = second_player_pot[-1]
    second_to_last_chip = second_player_pot[-2]

    if last_chip.color == "green":
        player.rubies += 1

    if second_to_last_chip.color == "green":
        player.rubies += 1


# Awards bonus based on the number of purple chips in the player's pot
def ghosts_breath(player):
    purple_count = 0

    # Count purple chips
    for chip in player.pot:
        if chip.color == "purple":
            purple_count += 1

    # Apply rewards based on count
    if purple_count >= 3:
        # Auto-apply highest reward (can be changed later for player choice)
        player.victory_points += 2
        player.droplet_position += 1
        print("3+ purple chips: +2 VP, droplet moves forward 1 space")

    elif purple_count == 2:
        player.victory_points += 1
        player.rubies += 1
        print("2 purple chips: +1 VP, +1 ruby")

    elif purple_count == 1:
        player.victory_points += 1
        print("1 purple chip: +1 VP")

    else:
        print("No purple chips: no bonus")
        print(purple_count)
