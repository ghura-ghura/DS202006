import random

class Dice: 
        # D4 dice
        @staticmethod
        def rollD4():
                """Roll a 4 sided dice"""
                return random.randint(1,4)
        @staticmethod
        def rollD6():
                """Roll a 6 sided dice"""
                return random.randint(1,6)
        @staticmethod
        def rollD8():
                """Roll a 8 sided dice"""
                return random.randint(1,8)
        @staticmethod
        def rollD12():
                """Roll a 12 sided dice"""
                return random.randint(1,12)
        @staticmethod
        def rollD20():
                """Roll a 20 sided dice"""
                return random.randint(1,20)
        @staticmethod
        def rollD100():
                """Roll a 100 sided dice"""
                return random.randint(1,100)

# Dice rolling program 
user_input = input("Type the dice that you want to roll (d4, d6, d8, d12, d20, d100) ")

if user_input == "d4":
        result = int(Dice.rollD4())
        # return Dice.rollD4()
        print(f"You have rolled a {result} ,range 1-4")
elif user_input == "d6":
        result = int(Dice.rollD6())
        print(f"You have rolled a {result} ,range 1-6")
elif user_input == "d8":
        result = int(Dice.rollD8())
        print(f"You have rolled a {result} ,range 1-8")
elif user_input == "d12":
        result = int(Dice.rollD12())
        print(f"You have rolled a {result} ,range 1-12")
elif user_input == "d20":
        result = int(Dice.rollD20())
        print(f"You have rolled a {result} ,range 1-20")
elif user_input == "d100":
        result = int(Dice.rollD100())
        print(f"You have rolled a {result} ,range 1-100")
else:
        print("Invalid input")
