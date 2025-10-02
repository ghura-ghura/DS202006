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

player_names = []
player_wins = []
rounds = 0
gameover = False


# Obtain the number of players: 
number_of_players = int(input("How many players shall participate in this game??  "))
winning_scores = int(input("How many rounds must you win to be the champion?  "))


# For loop to obtain the player names: 
for i in range(number_of_players):
    name = input(f"What is the name of Player {i+1}  ")
    player_names.append(name)

# Initialize scores and rolls 
for i in range(number_of_players):
        player_wins.append(0)

# Initialize player rolls as aempty lists for each player 
player_rolls_history = [] # This will be a nested list 

for i in range (number_of_players):
      #Add an empty list for each player: 
      player_rolls_history.append([])

# Repeats until the game is over 
while gameover is False: 
    print(f"Round {rounds+1}")
    current_rolls = []

    # We need to roll the dice for each player: 
    for i in range(number_of_players):
        roll = Dice.rollD6()                                          
        current_rolls.append(roll)
        player_rolls_history[i].append(roll)
        print(f"Player {player_names[i]} rolled: {roll}")
    input("\n Press ENTER to continue...")

    # ... still in the while gameover is False: 

    # Obtain the highest roll this round: 
    max_roll =max(current_rolls)

    # Winners will store information about who won this round: 
    winners = []

    # Search for the highest roll 
    for j in range(len(current_rolls)):
        if current_rolls[j] == max_roll: 
                winners.append(player_names[j])
                player_wins[j] += 1 

    print(f"The winner of this round is/are: {winners} ")

    # Check if someone reached winning score. Even if unlikley there might be more than one winner.. 
    for z in range(number_of_players):
        if player_wins[z] >= winning_scores: 
            print(f"\n {player_names[z]} is the newest Batte of Dices Champion")
            gameover = True

    # DIsp for ongoing game       
    if gameover is False: 
        print(f"This heated Battle of Dices is still going on! Who will win in the end? ")
    rounds += 1

# Save the results 
filename = input("Enter the filname to save the results: ")

with open(filename, "w") as file: 
      for round_number in range(rounds):
            file.write(f"Round {round_number+1}: ")
            rolls_str = "" # Start with embty string 
            for i in range (number_of_players):
                  rolls_str += (f"  {player_names[i]} rolled {player_rolls_history[i][round_number]} ")
                  if i < number_of_players - 1: # Add a comma after each, except for the last one 
                        rolls_str += ", "
            print(f" Round {round_number+1} {rolls_str}")

            file.write(rolls_str + "\n")
