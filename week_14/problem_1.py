def readposint():
    while True:
        try:
            user_input = input("Enter a positive integer: ").strip()
            if not user_input:
                print("Input cannot be empty. Please enter a positive integer.")
                continue
            number = int(user_input)
            if number > 0:
                return number
            else:
                print("Input must be a positive integer. Please try again.")
        except:
            print("Invalid input. Please enter a positive integer.")

pos_int = readposint()
print(f"You entered: {pos_int}")
