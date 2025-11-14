
#Endrias

def check_grid(player_input, used_space=None, enemy_ships=None, board_size = 5):
    
    """
    The code will attempt to check if the player is making a valid move
    Purpose of the code:
    Checks if the grid is used, availalbe, or hit/miss.
    
    Args:
        player_input (str): The input coordinates entered by the player
                    ex.include ("A3,C1,E5")
        used_space (set): A set a tuples for row and column for 
                            already played moves.
        enemy_ships (set): A tuples for the location of the enemy ships 

    Returns:
        tuple or None: The (row, col) index if the move 
        is valid, otherwise None.
    """
    used_space = set() if used_space is None else used_space
    enemy_ships = set() if enemy_ships is None else enemy_ships
        
    letters = ['A', 'B', 'C', 'D', 'E']
    

    if not player_input:
        print("For example, enter something like A3 or E5.")
        return None
    
    move = player_input.strip().upper()

    # split it into column and row
    col = move[0]
    if len(move) < 2 or col not in letters or not move[1:].isdigit():
        print("The formate is Invalid. Use A–E and 1–5.")
        return None

    row = int(move[1:]) - 1
    col_index = letters.index(col)

    # checking bounds
    if row < 0 or row >= board_size:
        print("You are out of bounds, row is betweem 1 and 5")
        return None

    # checking if the space is already used
    if (row, col_index) in used_space:
        print("You have played this move already")
        return None

    # record move played
    used_space.add((row, col_index))

    # checking for hits
    if (row, col_index) not in enemy_ships:
        print(f"You missed, better luck next time {col}{row + 1}.")
    else:
        print(f" Hit!!! you just hit opponent ship {col}{row + 1}.")

    # Shows the player past moves
    print("\nPrevious moves:")
    for (r, c) in sorted(used_space):
        print(f"{letters[c]}{r + 1}", end=" ")
    print("\n")


    return (row, col_index)
