import random 
import sys
import copy 

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
        
# Function for mapping the dice roll to the right dice
def pick_die(code):
      # Maybe insert a criteria if input is wrong 
      if code == "d4": return Dice.rollD4
      if code == "d6": return Dice.rollD6
      if code == "d8": return Dice.rollD8
      if code == "d12": return Dice.rollD12
      if code == "d20": return Dice.rollD20
      if code == "d100": return Dice.rollD100
      return None


# Dictionary Template for storing player information: 
player_info = {
    "name": "",
    "email": "",
    "country": "",
    "wins": 0,
    "rolls": [],
    "die_1": None,
    "die_2": None,
}

# Variables to keep track of the score 
rounds = 0 
gameover = False 
# Number of wins needed to win the game: 
winning_score = 3 
# List to store the dicts for each player: 
players = []

# Obtain the number of players: 
raw_input = input("How many players?")

# Check so the user actually ads a number otherwise ends the following code... 
if not raw_input.isdigit():
    print("Please enter a number otherwise the program will end....")
    sys.exit()
number_of_players = int(raw_input)

# For loop to obtain the player names: 
for i in range(number_of_players):

    # Make a deep copy of the template for this player: 
    player = copy.deepcopy(player_info)

    player["name"] = input(f"What is the name of Player {i+1} ? ")
    player["email"] = input(f"What is the e-mail of Player {i+1} ?")
    player["country"] = input(f"What is the country of Player {i+1} ?")

    # Collecting the input for the dices from the user 
    code1 = input(f"Choose FIRST die for Player {i+1} (d4, d6, d8, d12, d20, d100): ").lower()
    code2 = input(f"Choose SECOND die for Player {i+1} (d4, d6, d8, d12, d20, d100): ").lower()
    
    # Match function for the dies
    die_1 = pick_die(code1)
    die_2 = pick_die(code2)

    # Check is the user entered something or not exit if they do an error... 
    if die_1 is None or die_2 is None:
        print("Invalid die code. Use one of: d4, d6, d8, d12, d20, d100.")
        sys.exit()

    player["die_1"] = die_1
    player["die_2"] = die_2

    players.append(player)

# Repeats until the game is over. As many rounds as necessary: 
while gameover is False:

    print(f"Round {rounds+1}:")

    # Dice roll for each player in the current round: 
    current_rolls = []

    # We need to roll the dice for each player and here we collect that info from the dict. 
    for each_player in players:
        r1 = each_player["die_1"]()   
        r2 = each_player["die_2"]()
        total = r1 + r2

        each_player["rolls"].append(total)  
        current_rolls.append(total)

        print(f"Player {each_player['name']} rolled {r1} + {r2} = {total}")


    # Obtain the highest roll for this round: 
    max_roll = max(current_rolls)

    # Find winners of the round 
    winners = []

    # Search for all players who got the highest roll: 
    for each_player in players:
        if(each_player["rolls"][-1] == max_roll):
            each_player["wins"] += 1 
            print(f"Player {each_player['name']} won in round {rounds+1}")

            winners.append(each_player['name'])
    print(f"Winners of this round: {winners}")

    for each_player in players:
        if(each_player["wins"] >= winning_score):
            print(f"\n {each_player['name']} is the newest Battle of Dices Champion")
            gameover = True
    
    if gameover is False: 
        print("This heated Battle of Dices is still ongoing. Who will win in the end? ")
    
    rounds += 1 

# Save results 
filename = input("Enter the filename to save the results: " )
with open(filename, "w") as file: 
    #Player Information
    file.write("Player Information: \n")

    # Savers each player information using python automatically concatenation of adjacent strings: 
    for each_player in players: 
        file.write(
            f"Name: {each_player['name']}\n"
            f"* Email: {each_player['email']}\n"
            f"* Country: {each_player['country']}\n"
            f" Wins: {each_player['wins']} \n"
        )
    file.write("\nGame rounds:\n")

    # Round history 
    for r in range(rounds):
        # Start with empty text for this round 
        rolls_str = ""

        # Go through each player and build the string step by step 
        for i, each_player in enumerate(players):
            rolls_str += f"{each_player['name']} rolled {each_player['rolls'][r]}"

            # Add a comma and space unless it's the last player 
            if i < len(players) - 1: 
                rolls_str += ", "
        # Now write the full round info to the file 
        file.write(f"Round {r+1}:\n {rolls_str}\n")

print("\nGame over! Results saved succesfully. ")




