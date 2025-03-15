import random


def randomize_ingredients(ingredients):
    random.shuffle(ingredients)
    return ingredients

def draw_ingredient(ingredients):
    if ingredients:
        print(ingredients[len(ingredients) - 1])
        return ingredients.pop()
    return None
