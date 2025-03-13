import random

def draw_first_ingredient():
    with open('ingredient_bag.txt', 'r') as file:
        lines = [line.strip() for line in file]

    random_int = random.randint(1, len(lines))

    print("your first ingredient was a", lines[random_int - 1])

    with open('drawn_ingredients.txt', 'w') as file:
        file.write(lines[random_int - 1] + "\n")

    lines.remove(lines[random_int - 1])

    with open('remaining_ingredients.txt', 'w') as f:
        for line in lines:
            f.write(line  + "\n")

def draw_ingredients():

    with open('remaining_ingredients.txt', 'r') as file:
        lines = [line.strip() for line in file]

    random_int = random.randint(1, len(lines))

    print("you drew a", lines[random_int - 1])

    with open('drawn_ingredients.txt', 'a') as file:
        file.write(lines[random_int - 1] + "\n")

    lines.remove(lines[random_int - 1])

    with open('remaining_ingredients.txt', 'w') as f:
        for line in lines:
            f.write(line  + "\n")

def is_bag_empty():
    
    with open('remaining_ingredients.txt', 'r') as file:
        lines = file.readlines()

    if lines == []:
        return True 