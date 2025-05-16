class Player:
    def __init__(self, name):
        self.name = name
        self.bag = []  # List of bag (bag)
        self.pot = []
        self.rubies = 0  # Currency used in the game
        self.droplet_position = 0  # Starting position in the pot
        self.victory_points = 0  # Total victory points
        self.explosion_count = 0
        self.mandrake_marker = 0
        self.money = 0

    def add_ingredient(self, bag):
        self.bag.append(bag)

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
                f"explosion count: {self.explosion_count}, "
                f"mandrake marker: {self.mandrake_marker}, "
                f"money: {self.money}")


    def show_bag(self):
        print(f"{self.name}'s Bag:")
        for chip in self.bag:
            print(f"- {chip.type}")


    def reset(self):
        self.droplet_position = 0
        self.mandrake_marker = 0
        self.explosion_count = 0
        self.money = 0
        self.bag.extend(self.pot)
        self.pot.clear() 

