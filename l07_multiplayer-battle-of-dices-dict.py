import random 
import sys
import copy 

# Variables to keep track of the score 
rounds = 0 
gameover = False 
# Number of wins needed to win the game: 
winning_score = 3 

def rollD6():
    return random.randint(1, 6)

# Dictionary Template for storing player information: 
player_info = {
    "name": "",
    "email": "",
    "country": "",
    "wins": 0,
    "rolls": []

}

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

    players.append(player)

# Repeats until the game is over. As many rounds as necessary: 
while gameover is False:

    print(f"Round {rounds+1}:")

    # Dice roll for each player in the current round: 
    current_rolls = []

    # We need to roll the dice for each player 
    for each_player in players:
        roll = rollD6()

        each_player["rolls"].append(roll)
        current_rolls.append(roll)

        print(f"Player {each_player['name']} rolled: {roll}")

    # Obtain the highest roll for this round: 
    max_roll = max(current_rolls)

    # Find winners of the round 
    winners = []

    # Search for all players who got the highest roll: 
    for each_player in players:
        if(each_player["rolls"][-1] == max_roll):
            each_player["wins"] += 1 
            print(f"Player {each_player['name']} won in round {rounds}")

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




