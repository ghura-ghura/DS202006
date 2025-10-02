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
user_input = input("Type the dice that you want to roll (d4, d6, d8, d12, d20, d100) ")

if user_input == "d4":
        roll = Dice.rollD4
        # return Dice.rollD4()
        # print(f"You have rolled a {result} ,range 1-4")
elif user_input == "d6":
        roll = Dice.rollD6
        # print(f"You have rolled a {result} ,range 1-6")
elif user_input == "d8":
        roll = Dice.rollD8
        # print(f"You have rolled a {result} ,range 1-8")
elif user_input == "d12":
        roll = Dice.rollD12
        # print(f"You have rolled a {result} ,range 1-12")
elif user_input == "d20":
        roll = Dice.rollD20
        # print(f"You have rolled a {result} ,range 1-20")
elif user_input == "d100":
        roll = Dice.rollD100
        # print(f"You have rolled a {result} ,range 1-100")
else:
        print("Invalid input")

All_rounds = []
Player_1_rolls = []
Player_2_rolls = []

def play_game():
    player1_wins = 0
    player2_wins = 0
    played_rounds = 0
    # All_rounds = []
    # Player_1_rolls = []
    # Player_2_rolls = []

    #While loop 
    while player1_wins < 3 and player2_wins < 3:

    # Round start
        player1_roll = roll()
        #player1_roll = random.randint(1, 6)
        print("Player 1 rolled: ", player1_roll)
        Player_1_rolls.append(player1_roll) 


        player2_roll = roll()
        # player2_roll = random.randint(1, 6)
        print("Player 2 rolled: ", player2_roll)
        Player_2_rolls.append(player2_roll) 

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
        All_rounds.append(played_rounds)

    if player1_wins == 3:
        print(f"Player 1 is our new Champion and it took {played_rounds} rounds to win")
        
    elif player2_wins == 3:
        print(f"Player 2 is our new Champion and it took {played_rounds} rounds to win")
    else:
        pass
#start a new game  
play_game()    

 # We can print the game score:
print(f"Rounds played  {All_rounds}" )
print(f"Player 1 rolls {Player_1_rolls}")
print(f"Player 2 rolls {Player_2_rolls}")

filename = input("Enter the filename to save the results: ")

with open(filename,"w") as file: #Write mode for the file here 
       for i in range(len(Player_1_rolls)):
              file.write(f"Round {i+1}: Player 1 rolled {Player_1_rolls[i]}, Player 2 rolled {Player_2_rolls[i]}\n")




