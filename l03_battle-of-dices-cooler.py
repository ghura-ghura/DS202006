import random
# from dice import Dice

print("🎲 Welcome to Battle of Dices! 🎲")

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
# user_input = input("Type the dice that you want to roll (d4, d6, d8, d12, d20, d100) ")
user_input_1 = input("Type the first dice that you want to roll (d4, d6, d8, d12, d20, d100) ")


if user_input_1 == "d4":
        roll_1 = Dice.rollD4
        # return Dice.rollD4()
        # print(f"You have rolled a {result} ,range 1-4")
elif user_input_1 == "d6":
        roll_1 = Dice.rollD6
        # print(f"You have rolled a {result} ,range 1-6")
elif user_input_1 == "d8":
        roll_1 = Dice.rollD8
        # print(f"You have rolled a {result} ,range 1-8")
elif user_input_1 == "d12":
        roll_1 = Dice.rollD12
        # print(f"You have rolled a {result} ,range 1-12")
elif user_input_1 == "d20":
        roll_1 = Dice.rollD20
        # print(f"You have rolled a {result} ,range 1-20")
elif user_input_1 == "d100":
        roll_1 = Dice.rollD100
        # print(f"You have rolled a {result} ,range 1-100")
else:
        print("Invalid input")

user_input_2 = input("Type the second dice that you want to roll (d4, d6, d8, d12, d20, d100) ")


if user_input_2 == "d4":
        roll_2 = Dice.rollD4
        # return Dice.rollD4()
        # print(f"You have rolled a {result} ,range 1-4")
elif user_input_2 == "d6":
        roll_2 = Dice.rollD6
        # print(f"You have rolled a {result} ,range 1-6")
elif user_input_2 == "d8":
        roll_2 = Dice.rollD8
        # print(f"You have rolled a {result} ,range 1-8")
elif user_input_2 == "d12":
        roll_2 = Dice.rollD12
        # print(f"You have rolled a {result} ,range 1-12")
elif user_input_2 == "d20":
        roll_2 = Dice.rollD20
        # print(f"You have rolled a {result} ,range 1-20")
elif user_input_2 == "d100":
        roll_2 = Dice.rollD100
        # print(f"You have rolled a {result} ,range 1-100")
else:
        print("Invalid input")

def play_game():
    player1_wins = 0
    player2_wins = 0
    played_rounds = 0

    #While loop 
    while player1_wins < 3 and player2_wins < 3:

    # Round
        player1_roll = roll_1() + roll_2()
        #player1_roll = random.randint(1, 6)
        print("Player 1 rolled the total of: ", player1_roll)

        player2_roll = roll_1() + roll_2()
        # player2_roll = random.randint(1, 6)
        print("Player 2 rolled the total of: ", player2_roll)

        input("\nPress ENTER to continue...")

    # So far so good right? But how to check who got the highest roll?

        if player1_roll > player2_roll:
            player1_wins += 1
            print("Player 1 wins this round!")
            print("Because ", player1_roll," is greater than ", player2_roll)
        elif player2_roll > player1_roll:
            player2_wins += 1
            print("Player 2 wins this round!")   
            print("Because ", player2_roll," is greater than ", player1_roll)
        else: # player1_roll == player2_roll:
            print("Amaaazzinng! This round has a tie!")
        print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")    
        
        # Updated played rounds
        played_rounds += 1

    if player1_wins == 3:
        print(f"Player 1 is our new Champion and it took {played_rounds} rounds to win")
    elif player2_wins == 3:
        print(f"Player 2 is our new Champion and it took {played_rounds} rounds to win")
    else:
        pass
#start a new game  
play_game()    

# We can print the game score:


# Since none of them would have won after 1 round, we could copy this code several times
# until we have enough times to make sure someone wins.





