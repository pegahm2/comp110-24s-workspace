"""EX03 - Functional Battleship.""" 
import random 

__author__ = "730553436"


def input_guess(grid_size: int, row_or_column: str) -> int: 
    """Function Name for input_guess for battleship."""
    assert row_or_column == "row" or row_or_column == "column"
    
    prompt: str = ""
    if row_or_column == "row":
        prompt = "Guess a row: "
    else:
        prompt = "Guess a column: "
    guess: int = int(input(prompt))

    while not (0 < guess <= grid_size):
        """Print out the grid."""
        guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    return guess


def print_grid(grid_size: int, row_guess: int, column_guess: int, correct_guesses: bool) -> None: 
    """Function Name for print_grid for battleship."""
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"

    r: int = 1
    while r <= grid_size:
        output: str = ""
        c: int = 1 
        if r == row_guess:
            while c <= grid_size:
                if c == column_guess:
                    if correct_guesses:
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


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Function Name for correct_guess for battleship."""
    if secret_row == row_guess and secret_column == column_guess:
        return True
    else:
        return False
    

def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Function for main in battleship."""
    turn_num: int = 1
    
    while turn_num <= 5:

        print(f"=== Turn {turn_num}/5 ===")
        row_guess = input_guess(grid_size, "row")
        col_guess = input_guess(grid_size, "column")

        print_grid(grid_size, row_guess, col_guess, row_guess == secret_row and col_guess == secret_column)
        
        if correct_guess(secret_row, secret_column, row_guess, col_guess):
            print("Hit!")
            print(f"You won in {turn_num}/5 turns!")
            turn_num = 6
        else:
            print("Miss!")

        turn_num += 1

    if turn_num == 6:    
        print("X/5 - Better luck next time!")


if __name__ == "__main__":
    """Randomized Grid Size in Game."""
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))
