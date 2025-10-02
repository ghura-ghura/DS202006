# Battle of Dices is going to be an amazing 2 player game, 
# where two players face each other using only their sheer luck! 
# 
# The rules are:
# 
# Each player throws one D6.
# The player with the highest roll wins the round.  
# The first player to win 3 times is the winner.
#
# Our main task today is to implement the code necessary to bring this
# amazing game alive!

import random
import sys

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0

# Round 1
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(1,100)
print("Player 1 rolled: ", player1_roll)

player2_roll = random.randint(1,100)
print("Player 2 rolled: ", player2_roll)

Player_1_roll_1 = player1_roll
Player_2_roll_1 = player2_roll

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins = player1_wins + 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player2_roll > player1_roll:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)

else: # player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
    

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the showing some skill and is our new Master of Dices! ")
    sys.exit()
elif player2_wins == 3:
    print("Player 2 is the showing some skill and is our new Master of Dices!")
    sys.exit()
elif player1_wins == player2_wins:
    print("Sooo Extiting with a tie..... Who will win in the end? ")
else:
    print("The match is still on who will win?")
    



# Since none of them would have won after 1 round, we could copy this code several times
# until we have enough times to make sure someone wins.


# Round 2
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(1,100)
print("Player 1 rolled: ", player1_roll)

player2_roll = random.randint(1,100)
print("Player 2 rolled: ", player2_roll)

Player_1_roll_2 = player1_roll
Player_2_roll_2 = player2_roll

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins = player1_wins + 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player2_roll > player1_roll:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)

else: # player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
    

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the showing some skill and is our new Master of Dices! ")
    sys.exit()
elif player2_wins == 3:
    print("Player 2 is the showing some skill and is our new Master of Dices!")
    sys.exit()
elif player1_wins == player2_wins:
    print("Sooo Extiting with a tie..... Who will win in the end? ")

else:
    print("The match is still on who will win?")

# Round 3 
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(1,100)
print("Player 1 rolled: ", player1_roll)

player2_roll = random.randint(1,100)
print("Player 2 rolled: ", player2_roll)

Player_1_roll_3 = player1_roll
Player_2_roll_3 = player2_roll

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins = player1_wins + 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player2_roll > player1_roll:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)

else: # player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
    

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the showing some skill and is our new Master of Dices! ")
    print(f"Rounds played:  1 , 2 , 3 ")
    print(f"Player 1 has rolled", Player_1_roll_1, Player_1_roll_2, Player_1_roll_3 )
    print(f"Player 2 has rolled", Player_2_roll_1, Player_2_roll_2, Player_2_roll_3 )
    sys.exit()
elif player2_wins == 3:
    print("Player 2 is the showing some skill and is our new Master of Dices!")
    print(f"Rounds played:  1 , 2 , 3 ")
    print(f"Player 1 has rolled", Player_1_roll_1, Player_1_roll_2, Player_1_roll_3 )
    print(f"Player 2 has rolled", Player_2_roll_1, Player_2_roll_2, Player_2_roll_3 )
    sys.exit()
elif player1_wins == player2_wins:
    print("Sooo Extiting with a tie..... Who will win in the end? ")
    
else:
    print("The match is still on who will win?")

# Round 4
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(1,100)
print("Player 1 rolled: ", player1_roll)

player2_roll = random.randint(1,100)
print("Player 2 rolled: ", player2_roll)

Player_1_roll_4 = player1_roll
Player_2_roll_4 = player2_roll

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins = player1_wins + 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player2_roll > player1_roll:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)

else: # player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
    

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the showing some skill and is our new Master of Dices! ")
    print(f"Rounds played:  1 , 2 , 3 , 4")
    print(f"Player 1 has rolled", Player_1_roll_1, Player_1_roll_2, Player_1_roll_3, Player_1_roll_4 )
    print(f"Player 2 has rolled", Player_2_roll_1, Player_2_roll_2, Player_2_roll_3, Player_2_roll_4 )
    sys.exit()
elif player2_wins == 3:
    print("Player 2 is the showing some skill and is our new Master of Dices!")
    print(f"Rounds played:  1 , 2 , 3 , 4")
    print(f"Player 1 has rolled", Player_1_roll_1, Player_1_roll_2, Player_1_roll_3, Player_1_roll_4 )
    print(f"Player 2 has rolled", Player_2_roll_1, Player_2_roll_2, Player_2_roll_3, Player_2_roll_4 )
    sys.exit()
elif player1_wins == player2_wins:
    print("Sooo Extiting with a tie..... Who will win in the end? ")
    
else:
    print("The match is still on who will win?")

# Round 5
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(1,100)
print("Player 1 rolled: ", player1_roll)

player2_roll = random.randint(1,100)
print("Player 2 rolled: ", player2_roll)

Player_1_roll_5 = player1_roll
Player_2_roll_5 = player2_roll

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins = player1_wins + 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player2_roll > player1_roll:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)

else: # player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
    

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the showing some skill and is our new Master of Dices! ")
    print(f"Rounds played:  1 , 2 , 3 , 4 , 5")
    print(f"Player 1 has rolled", Player_1_roll_1, Player_1_roll_2, Player_1_roll_3, Player_1_roll_4, Player_1_roll_5 )
    print(f"Player 2 has rolled", Player_2_roll_1, Player_2_roll_2, Player_2_roll_3, Player_2_roll_4, Player_2_roll_5 )
    sys.exit()
elif player2_wins == 3:
    print("Player 2 is the showing some skill and is our new Master of Dices!")
    print(f"Rounds played:  1 , 2 , 3 , 4 , 5")
    print(f"Player 1 has rolled", Player_1_roll_1, Player_1_roll_2, Player_1_roll_3, Player_1_roll_4, Player_1_roll_5 )
    print(f"Player 2 has rolled", Player_2_roll_1, Player_2_roll_2, Player_2_roll_3, Player_2_roll_4, Player_2_roll_5 )
    sys.exit()
elif player1_wins == player2_wins:
    print("Sooo Extiting with a tie..... Who will win in the end? ")
    
else:
    print("The match is still on who will win?")

# Round 6
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(1,100)
print("Player 1 rolled: ", player1_roll)

player2_roll = random.randint(1,100)
print("Player 2 rolled: ", player2_roll)

Player_1_roll_6 = player1_roll
Player_2_roll_6 = player2_roll

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins = player1_wins + 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player2_roll > player1_roll:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)

else: # player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
    

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the showing some skill and is our new Master of Dices! ")
    print(f"Rounds played:  1 , 2 , 3 , 4 , 5 , 6 ")
    print(f"Player 1 has rolled", Player_1_roll_1, Player_1_roll_2, Player_1_roll_3, Player_1_roll_4, Player_1_roll_5, Player_1_roll_6 )
    print(f"Player 2 has rolled", Player_2_roll_1, Player_2_roll_2, Player_2_roll_3, Player_2_roll_4, Player_2_roll_5, Player_2_roll_6 )
    sys.exit()
elif player2_wins == 3:
    print("Player 2 is the showing some skill and is our new Master of Dices!")
    print(f"Rounds played:  1 , 2 , 3 , 4 , 5 , 6 ")
    print(f"Player 1 has rolled", Player_1_roll_1, Player_1_roll_2, Player_1_roll_3, Player_1_roll_4, Player_1_roll_5, Player_1_roll_6 )
    print(f"Player 2 has rolled", Player_2_roll_1, Player_2_roll_2, Player_2_roll_3, Player_2_roll_4, Player_2_roll_5, Player_2_roll_6 )
    sys.exit()
elif player1_wins == player2_wins:
    print("Sooo Extiting with a tie..... Who will win in the end? ")
    
else:
    print("The match is still on who will win?")


# Round 7
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(1,100)
print("Player 1 rolled: ", player1_roll)

player2_roll = random.randint(1,100)
print("Player 2 rolled: ", player2_roll)

Player_1_roll_7 = player1_roll
Player_2_roll_7 = player2_roll

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins = player1_wins + 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player2_roll > player1_roll:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)

else: # player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
    

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the showing some skill and is our new Master of Dices! ")
    print(f"Rounds played:  1 , 2 , 3 , 4 , 5 , 6, 7 ")
    print(f"Player 1 has rolled", Player_1_roll_1, Player_1_roll_2, Player_1_roll_3, Player_1_roll_4, Player_1_roll_5, Player_1_roll_6, Player_1_roll_7 )
    print(f"Player 2 has rolled", Player_2_roll_1, Player_2_roll_2, Player_2_roll_3, Player_2_roll_4, Player_2_roll_5, Player_2_roll_6, Player_2_roll_7 )
    sys.exit()
elif player2_wins == 3:
    print("Player 2 is the showing some skill and is our new Master of Dices!")
    print(f"Rounds played:  1 , 2 , 3 , 4 , 5 , 6, 7 ")
    print(f"Player 1 has rolled", Player_1_roll_1, Player_1_roll_2, Player_1_roll_3, Player_1_roll_4, Player_1_roll_5, Player_1_roll_6, Player_1_roll_7 )
    print(f"Player 2 has rolled", Player_2_roll_1, Player_2_roll_2, Player_2_roll_3, Player_2_roll_4, Player_2_roll_5, Player_2_roll_6, Player_2_roll_7 )
    sys.exit()
elif player1_wins == player2_wins:
    print("Sooo Extiting with a tie..... Who will win in the end? ")
    
else:
    print("The match is still on who will win?")

# Round 8
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(1,100)
print("Player 1 rolled: ", player1_roll)

player2_roll = random.randint(1,100)
print("Player 2 rolled: ", player2_roll)

Player_1_roll_8 = player1_roll
Player_2_roll_8 = player2_roll

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins = player1_wins + 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player2_roll > player1_roll:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)

else: # player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
    

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the showing some skill and is our new Master of Dices! ")
    print(f"Rounds played:  1 , 2 , 3 , 4 , 5 , 6, 7, 8 ")
    print(f"Player 1 has rolled", Player_1_roll_1, Player_1_roll_2, Player_1_roll_3, Player_1_roll_4, Player_1_roll_5, Player_1_roll_6, Player_1_roll_7, Player_1_roll_8 )
    print(f"Player 2 has rolled", Player_2_roll_1, Player_2_roll_2, Player_2_roll_3, Player_2_roll_4, Player_2_roll_5, Player_2_roll_6, Player_2_roll_7, Player_2_roll_8 )
    sys.exit()
elif player2_wins == 3:
    print("Player 2 is the showing some skill and is our new Master of Dices!")
    sys.exit()
elif player1_wins == player2_wins:
    print("Sooo Extiting with a tie..... Who will win in the end? ")
    
else:
    print("The match is still on who will win?")

# Round 9
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(1,100)
print("Player 1 rolled: ", player1_roll)

player2_roll = random.randint(1,100)
print("Player 2 rolled: ", player2_roll)

Player_1_roll_9 = player1_roll
Player_2_roll_9 = player2_roll

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins = player1_wins + 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player2_roll > player1_roll:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)

else: # player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
    

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the showing some skill and is our new Master of Dices! ")
    print(f"Rounds played:  1 , 2 , 3 , 4 , 5 , 6, 7, 8, 9 ")
    print(f"Player 1 has rolled", Player_1_roll_1, Player_1_roll_2, Player_1_roll_3, Player_1_roll_4, Player_1_roll_5, Player_1_roll_6, Player_1_roll_7, Player_1_roll_8, Player_1_roll_9 )
    print(f"Player 2 has rolled", Player_2_roll_1, Player_2_roll_2, Player_2_roll_3, Player_2_roll_4, Player_2_roll_5, Player_2_roll_6, Player_2_roll_7, Player_2_roll_8, Player_2_roll_9 )
    sys.exit()
elif player2_wins == 3:
    print("Player 2 is the showing some skill and is our new Master of Dices!")
    print(f"Rounds played:  1 , 2 , 3 , 4 , 5 , 6, 7, 8, 9 ")
    print(f"Player 1 has rolled", Player_1_roll_1, Player_1_roll_2, Player_1_roll_3, Player_1_roll_4, Player_1_roll_5, Player_1_roll_6, Player_1_roll_7, Player_1_roll_8, Player_1_roll_9 )
    print(f"Player 2 has rolled", Player_2_roll_1, Player_2_roll_2, Player_2_roll_3, Player_2_roll_4, Player_2_roll_5, Player_2_roll_6, Player_2_roll_7, Player_2_roll_8, Player_2_roll_9 )
    sys.exit()
elif player1_wins == player2_wins:
    print("Sooo Extiting with a tie..... Who will win in the end? ")
    
else:
    print("The match is still on who will win?")

# Round 10
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(1,100)
print("Player 1 rolled: ", player1_roll)

player2_roll = random.randint(1,100)
print("Player 2 rolled: ", player2_roll)

Player_1_roll_10 = player1_roll
Player_2_roll_10 = player2_roll

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins = player1_wins + 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player2_roll > player1_roll:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)

else: # player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
    

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the showing some skill and is our new Master of Dices! ")
    print(f"Rounds played:  1 , 2 , 3 , 4 , 5 , 6, 7, 8, 9, 10 ")
    print(f"Player 1 has rolled", Player_1_roll_1, Player_1_roll_2, Player_1_roll_3, Player_1_roll_4, Player_1_roll_5, Player_1_roll_6, Player_1_roll_7, Player_1_roll_8, Player_1_roll_9, Player_1_roll_10 )
    print(f"Player 2 has rolled", Player_2_roll_1, Player_2_roll_2, Player_2_roll_3, Player_2_roll_4, Player_2_roll_5, Player_2_roll_6, Player_2_roll_7, Player_2_roll_8, Player_2_roll_9,  Player_2_roll_10 )
    sys.exit()
elif player2_wins == 3:
    print("Player 2 is the showing some skill and is our new Master of Dices!")
    print(f"Rounds played:  1 , 2 , 3 , 4 , 5 , 6, 7, 8, 9, 10 ")
    print(f"Player 1 has rolled", Player_1_roll_1, Player_1_roll_2, Player_1_roll_3, Player_1_roll_4, Player_1_roll_5, Player_1_roll_6, Player_1_roll_7, Player_1_roll_8, Player_1_roll_9, Player_1_roll_10 )
    print(f"Player 2 has rolled", Player_2_roll_1, Player_2_roll_2, Player_2_roll_3, Player_2_roll_4, Player_2_roll_5, Player_2_roll_6, Player_2_roll_7, Player_2_roll_8, Player_2_roll_9,  Player_2_roll_10 )
    sys.exit()
elif player1_wins == player2_wins:
    print("Sooo Extiting with a tie..... Who will win in the end? ")
    
else:
    print("The match is still on who will win?")

# Round 11
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(1,100)
print("Player 1 rolled: ", player1_roll)

player2_roll = random.randint(1,100)
print("Player 2 rolled: ", player2_roll)

Player_1_roll_11 = player1_roll
Player_2_roll_11 = player2_roll

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins = player1_wins + 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player2_roll > player1_roll:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)

else: # player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
    

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the showing some skill and is our new Master of Dices! ")
    print(f"Rounds played:  1 , 2 , 3 , 4 , 5 , 6, 7, 8, 9, 10, 11 ")
    print(f"Player 1 has rolled", Player_1_roll_1, Player_1_roll_2, Player_1_roll_3, Player_1_roll_4, Player_1_roll_5, Player_1_roll_6, Player_1_roll_7, Player_1_roll_8, Player_1_roll_9, Player_1_roll_10, Player_1_roll_11 )
    print(f"Player 2 has rolled", Player_2_roll_1, Player_2_roll_2, Player_2_roll_3, Player_2_roll_4, Player_2_roll_5, Player_2_roll_6, Player_2_roll_7, Player_2_roll_8, Player_2_roll_9,  Player_2_roll_10, Player_2_roll_11 )
    sys.exit()
elif player2_wins == 3:
    print("Player 2 is the showing some skill and is our new Master of Dices!")
    print(f"Rounds played:  1 , 2 , 3 , 4 , 5 , 6, 7, 8, 9, 10, 11 ")
    print(f"Player 1 has rolled", Player_1_roll_1, Player_1_roll_2, Player_1_roll_3, Player_1_roll_4, Player_1_roll_5, Player_1_roll_6, Player_1_roll_7, Player_1_roll_8, Player_1_roll_9, Player_1_roll_10, Player_1_roll_11 )
    print(f"Player 2 has rolled", Player_2_roll_1, Player_2_roll_2, Player_2_roll_3, Player_2_roll_4, Player_2_roll_5, Player_2_roll_6, Player_2_roll_7, Player_2_roll_8, Player_2_roll_9,  Player_2_roll_10, Player_2_roll_11 )
    sys.exit()
elif player1_wins == player2_wins:
    print("Sooo Extiting with a tie..... Who will win in the end? ")
    
else:
    print("The match is still on who will win?")