"""EX02 - One Shot Battleship.""" 

__author__ = "730553436"
"""Codes for the the places to get hit in the battleship."""
grid_size: int = 4
correct_row: int = 3
correct_column: int = 2

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# input the row 
row_input: int = int(input("Guess a row: "))
while row_input > grid_size or row_input < 1:
    row_input = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

# input the column 
column_input: int = int(input("Guess a column: "))
while column_input > grid_size or column_input < 1:
    column_input = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

r: int = 1
while r <= grid_size:
    output: str = ""
    c: int = 1 
    if r == row_input:
        while c <= grid_size:
            if c == column_input:
                if row_input == correct_row and column_input == correct_column:
                    output += RED_BOX
                else:
                    output += WHITE_BOX
            else:
                output += BLUE_BOX
            c += 1
    else:
        while c <= grid_size:
            output += BLUE_BOX
            c += 1
    print(output)
    r += 1

# identify whether or not the battleship was hit or not
if row_input == correct_row and column_input == correct_column:
    print("Hit!")
elif row_input == correct_row:
    print("Close! Correct row, wrong column.")
elif column_input == correct_column:
    print("Close! Correct column, wrong row.")
else: 
    print("Miss!")
