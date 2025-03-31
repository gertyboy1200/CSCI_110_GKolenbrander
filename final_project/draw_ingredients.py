import random


def randomize_ingredients(ingredients):
    random.shuffle(ingredients)
    return ingredients

    
def draw_ingredient(ingredients):
    if ingredients:
        return ingredients.pop()
    return None
