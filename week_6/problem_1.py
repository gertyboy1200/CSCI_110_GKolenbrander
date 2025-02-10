import random


def get_random_day(n):
    week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    print("Your random week day is:", week_days[n])

get_random_day(random.randint(0,6))