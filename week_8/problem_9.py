user_input = input("enter the number for the triangle nuber you want to solve for: ")


def print_triangle_numbers(n):
    triangle_number = 0
    for i in range(int(n)):
        triangle_number += (i + 1)
        print((i+1), " ", triangle_number)

print_triangle_numbers(user_input)

def print_triangle_numbers_explicit(n):
    n = int(n)
    print(int((n * (n + 1)) / 2))

print_triangle_numbers_explicit(user_input)