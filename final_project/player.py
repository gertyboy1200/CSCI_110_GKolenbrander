class Player:
    def __init__(self, name):
        self.name = name
        self.ingredients = [
        "garlic_1", "garlic_1", "garlic_1", "garlic_1",
        "garlic_2", "garlic_2", "garlic_3"]  # List of ingredients (ingredients)
        self.rubies = 0  # Currency used in the game
        self.droplet_position = 0  # Starting position in the pot
        self.victory_points = 0  # Total victory points
        self.explosion_count = 0

    def add_ingredient(self, ingredients):
        self.ingredients.append(ingredients)

    def gain_rubies(self, amount):
        self.rubies += amount

    def move_droplet(self, spaces):
        self.droplet_position += spaces

    def gain_victory_points(self, points):
        self.victory_points += points

    def __str__(self):
        return (f"self: {self.name}, Rubies: {self.rubies}, "
                f"Droplet Position: {self.droplet_position}, "
                f"Victory Points: {self.victory_points}, "
                f"Ingredients: {self.ingredients}, "
                f"explosion count: {self.explosion_count}")
