"""EX01 - Simple Battleship - A cute step toward Battleship.""" 

__author__ = "730553436"
"""Codes for the box colors in the battleship."""
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

"""Player 1 analysis of whether the number is between 1 and 4"""
player1_input: int = int(input("Pick a secret boat location between 1 and 4:"))
if player1_input < 1:
    print("Error! " + str(player1_input) + " too low!")
    exit()
if player1_input > 4:
    print("Error! " + str(player1_input) + " too high!")
    exit()
"""Player 2 analysis of whether the number is between 1 and 4"""
player2_input:int = int(input("Guess a number between 1 and 4:"))
if player2_input < 1:
    print("Error! " + str(player2_input) + " too low!")
    exit()
if player2_input > 4:
    print("Error! " + str(player2_input) + " too high!")
    exit()
"""Analysis of whether the number for Player 1 and 2 is the same or different."""
if player1_input == player2_input:
    print("Correct! You hit the ship.")
if player1_input != player2_input:
    print("Incorrect! You missed the ship.")
"""Printing the String of Boxes in the Terminal depending on the Ship Location."""
"""Analysis of Battleship if position 1 is hit."""
if (player2_input == 1):
    if (player1_input == player2_input):
        print(RED_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
    else:
        print(WHITE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
"""Analysis of Battleship if position 2 is hit."""
if (player2_input == 2):
    if (player1_input == player2_input):
        print(BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX)
    else:
        print(BLUE_BOX + WHITE_BOX + BLUE_BOX + BLUE_BOX)
"""Analysis of Battleship if position 3 is hit."""
if (player2_input == 3):
    if (player1_input == player2_input):
        print(BLUE_BOX + BLUE_BOX + RED_BOX + BLUE_BOX)
    else:
        print(BLUE_BOX + BLUE_BOX + WHITE_BOX + BLUE_BOX)
"""Analysis of Battleship if position 4 is hit."""
if (player2_input == 4):
    if (player1_input == player2_input):
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + RED_BOX)
    else:
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + WHITE_BOX)


     

      