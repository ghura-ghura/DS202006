import random

# Roll the dice
low = 1
high = 20

# User input for the roll
user_input = input("Please press enter to be able to roll the dice.. ")

# Show the results 
if user_input == "":  # Enter pressed with no other characters
        result = random.randint(low, high)
        print(f"You rolled a {result} (range {low}–{high}).")
else:
        print("Invalid input.")
 



