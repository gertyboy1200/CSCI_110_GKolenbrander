class Ingredient:
    def __init__(self, type, color, value, cost, bonus = ""):
        self.type = type  
        self.color = color
        self.value = value
        self.cost = cost
        self.bonus = bonus 

    def __str__(self):
        return (f"Type: {self.type}, Color: {self.color}, Value: {self.value}, Cost: {self.cost}, Bonus: {self.bonus}")





def create_ingredient(type, color, value, cost, bonus = ""):
    return Ingredient(type, color, value, cost, bonus)

def get_ingredients():

    all_ingredients = [
        # Garlic (White) - Basic ingredient
        create_ingredient("garlic_1", "white", 1, 0),
        create_ingredient("garlic_2", "white", 2, 0),
        create_ingredient("garlic_3", "white", 3, 0),

        # Pumpkin (Orange) - No special bonus
        create_ingredient("pumpkin_1", "orange", 1, 3),

        # Toadstool (Red) - Moves extra if orange chips are present
        create_ingredient("toadstool_1", "red", 1, 6, "Move extra if orange chips are present"),
        create_ingredient("toadstool_2", "red", 2, 10, "Move extra if orange chips are present"),
        create_ingredient("toadstool_4", "red", 4, 16, "Move extra if orange chips are present"),

        # Mandrake (Yellow) - Doubles movement of next drawn chip
        create_ingredient("mandrake_1", "yellow", 1, 9, "Next drawn chip moves twice as far"),
        create_ingredient("mandrake_2", "yellow", 2, 13, "Next drawn chip moves twice as far"),
        create_ingredient("mandrake_4", "yellow", 4, 19, "Next drawn chip moves twice as far"),

        # Garden Spider (Green) - Gains rubies if last or second-to-last chip
        create_ingredient("garden_spider_1", "green", 1, 4, "Gains ruby if last or second-to-last chip"),
        create_ingredient("garden_spider_2", "green", 2, 8, "Gains ruby if last or second-to-last chip"),
        create_ingredient("garden_spider_4", "green", 4, 14, "Gains ruby if last or second-to-last chip"),

        # Ghost’s Breath (Purple) - Grants victory points and bonuses based on quantity
        create_ingredient("ghosts_breath_1", "purple", 1, 9, "More purple chips grant extra victory points and rubies"),

        # Crow Skull (Blue) - Grants ruby if placed on a ruby space
        create_ingredient("crow_skull_1", "blue", 1, 4, "Grants ruby if placed on a ruby space"),
        create_ingredient("crow_skull_2", "blue", 2, 8, "Grants ruby if placed on a ruby space"),
        create_ingredient("crow_skull_4", "blue", 4, 14, "Grants ruby if placed on a ruby space"),
    ]


    return all_ingredients

def do_ingredient_action(matching_ingredient, player):
    print("ingredient", matching_ingredient)

    

    if matching_ingredient.color == "white":
        garlic(matching_ingredient, player)

    elif matching_ingredient.color == "orange":
        pumpkin(matching_ingredient, player)


    elif matching_ingredient.color == "purple":
        print("Ghost’s Breath effect: More purple chips grant extra victory points and rubies")
    elif matching_ingredient.type == "crow_skull":
        print("Crow Skull effect: Grants ruby if placed on a ruby space")
    else:
        print("No special effect for this ingredient")


def garlic(matching_ingredient, player):
    player.explosion_count += matching_ingredient.value
    player.droplet_position += matching_ingredient.value
    return player


def pumpkin(matching_ingredient, player):
    player.droplet_position += matching_ingredient.value
    return player


#If you draw a red chip from your bag and there are no orange chips in your pot, 
# move the red chip forward only according to the value depicted on it. 
# If there are already 1 or 2 orange chips in your pot, 
# move the red chip an additional 1 space forward irrespective of its value.
def toadstool_1(): #cost 6
    return 1
def toadstool_2(): #cost 10
    return 2
def toadstool_4(): #cost 16
    return 4



#Bonus: If you draw a yellow chip from the bag, move the next chip that you draw twice as far. 
# For instance, a 2-chip that is drawn after a yellow chip is moved 4 spaces forward. 
# The values of the yellow chips are of no significance.
def mandrake_1():  #cost 9
    return 1
def mandrake_2(): #cost 13
    return 2
def mandrake_4():  #cost 19
    return 4

def mandrake(matching_ingredinet, player):
    player.droplet_position += matching_ingredinet.value
    player.mandrake_marker = 1
    return(player)


#Bonus: In Evaluation Phase B, you receive 1 ruby for every green chip 
# (irrespective of its value) that was either the last chip placed in your pot or next to last. 
# You do not receive any rubies for any green chips that are not on your last or next to last space.
def garden_spider_1(): #cost 4
    return 1
def garden_spider_2(): #cost 8
    return 2
def garden_spider_4(): #cost 14
    return 4



#Bonus: In Evaluation Phase B, count up the purple chips in your pot. 
# If there is 1 purple chip, you receive 1 victory point.
#If there are 2 purple chips, you receive 1 victory point and 1 ruby.
# If there are 3 or more purple chips, you receive 2 victory points and you may move your droplet 1 space forward. 
# There is no added bonus for 4 or more chips. However, it is always possible to use a lower action. 
# For example, you can take the bonus for 2 purple chips even though you have 3 chips.
def ghosts_breath_1(): #cost 9
    return 1




#Bonus: If you place a blue chip on a ruby space, you immediately receive 1 ruby. 
# The values of the blue chips are of no significance.
def crow_skull_1(): #cost 4
    return 1
def crow_skull_2(): #cost 8
    return 2
def crow_skull_4(): #cost 14
    return 4