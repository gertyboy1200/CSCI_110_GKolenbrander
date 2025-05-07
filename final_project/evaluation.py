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

