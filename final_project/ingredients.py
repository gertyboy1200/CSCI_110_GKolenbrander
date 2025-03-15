class Ingredient:
    def __init__(self, name, value, cost, bonus = ""):
        self.name = name  
        self.value = value
        self.cost = cost
        self.bonus = bonus 

    def __str__(self):
        return (f"Name: {self.name}, Value: {self.value}, Cost: {self.cost}, Bonus: {self.bonus}")

def create_ingredient(name, value, cost, bonus = ""):
    return Ingredient(name, value, cost, bonus)


def garlic_1():
    return 1
def garlic_2():
    return 2
def garlic_3():
    return 3



def pumpkin_1(): #cost 3
    return 3



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