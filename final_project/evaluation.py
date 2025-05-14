import random
import ingredients

def read_board_data(filename):
    board_data = []

    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('#') or not line.strip():
                continue
            
            parts = [part.strip() for part in line.split('|')]
            
            # Convert the parts to integers
            droplet_position = int(parts[0])
            money = int(parts[1])
            ruby = int(parts[2])
            victory_points = int(parts[3])
            
            # Append the tuple to the board_data list
            board_data.append((droplet_position, money, ruby, victory_points))
    return board_data

def bonus_die(player):
    bonuses = [
        "1 victory point",
        "2 victory points",
        "3 victory points",
        "1 ruby",
        "Advance droplet one space",
        "Draw 1 pumpkin chip and add it to your bag"
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
        # Add a pumpkin chip to the bag (assumes you have a create_ingredient function)
        pumpkin_chip = ingredients.create_ingredient("pumpkin_1", "orange", 1, 0)
        player.bag.append(pumpkin_chip)

def garden_spider(player):
    if len(player.pot) <= 1:
        print("Not enough items in your pot")
        return
    
    second_player_pot = player.pot.copy()
    last_chip = second_player_pot.pop()
    second_to_last_chip = second_player_pot.pop()


    if last_chip.color == "green":
        player.rubies += 1

    if second_to_last_chip == "green":
        player.rubies += 1

def ghosts_breath(player):
    print(player.pot)
    purple_count = 0

    # Count purple chips in the pot
    for chip in player.pot:
        print(chip)
        if chip.color == "purple":
            purple_count += 1

    # Award bonuses based on count
    if purple_count >= 3:
        # Let player choose a lower reward if desired
        # For now, auto-apply highest reward:
        player.victory_points += 2
        player.droplet_position += 1  # Move droplet forward
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


