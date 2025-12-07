#Main Submition

# Natalie Siliezar

import random 
 
def set_up():
    """Set of battle-ship grid board"""
    board = [(r, c) for r in range (5) for c in range (5)]
    occupied = set()

    def random_cell():
        """Build list of avaliable coordinates not occuppied"""
        choices = [pos for pos in board if pos not in occupied]
        return random.choice(choices)
    
    def place_ship(length = 2):
        """Place a ship given the length (2 cells) horizontally or vertically"""
        while True: 
            start = random_cell()
            row, col = start
            direction = random.choice(["horizontal","vertical"])
            
        #Possible Coordinates for ship
            if direction == "horizontal":
                ship_cells = [(row, col + i) for i in range(length) if col + i < 5]
            else: 
                ship_cells = [(row + i, col) for i in range(length) if row + i < 5]
        
        #Make sure no overalpping occurs
            if len(ship_cells) == length and all(cell not in occupied for cell in ship_cells):
                occupied.update(ship_cells)
                return ship_cells 
    
    
    
    #Player ships       
    ship1 = place_ship(2)
    ship2 = place_ship(2)
    
    #Create and place mines (1 cell)
    mines = []
    for _ in range(2):
        mine = random_cell()
        mines.append(mine)
        occupied.add(mine)
        
    #Create and place lucky grid (1 cell)
    lucky = random_cell()
    occupied.add(lucky)
    
    #Testing to make sure all pieces return (will hide mines and lucky grid later).
    return {
        "ship1": ship1,
        "ship2": ship2,
        "mines": mines,
        "lucky": lucky
    }



def move_ship(ship, direction, other_ship):
    """Move ship one cell in any valid direction. Can over lap
    mines and lucky grid, but not the other ship
    
    Parameters:
        ship: ship of the player that will move. 
        direction: movement of ship (up, down, left, right)
        other_ship: ship of the player that has not moved.
    
    """
    #Compute new direction/coordinates
    if direction == "up":
        new_ship = [(r-1, c) for r, c in ship]
    elif direction == "down":
        new_ship = [(r+1, c) for r, c in ship]
    elif direction == "left":
        new_ship = [(r, c-1) for r, c in ship]
    elif direction == "right":
        new_ship = [(r, c+1) for r, c in ship]
    else: 
        return ship 
    
    #Check board grid boundaries
    for r, c in new_ship:
        if r < 0 or r > 4 or c < 0 or c > 5:
            return ship, "Cannot Move!: reached the edge of board."
    #Check for collision with other ship
    for pos in new_ship:
        if pos in other_ship:
            return ship, "Collision Imminent!: pick another direction."
    
    #Valid direction
    return new_ship, "Ship moved successfully!"
  
  
  #----------------------------------------------------------

# Jishan winner function
def check_winner(opponent_ships, hits):
    """Return True if all opponent ships are sunk."""
    for ship in opponent_ships:
        if not all(pos in hits for pos in ship):
            return False
    return True    
#------------------------------------
#display function 
def print_board(ships, mines, lucky, hits, size=5):
    board = [["~" for _ in range(size)] for _ in range(size)]

    for r, c in hits:
        board[r][c] = "X"

    for ship in ships:
        for r, c in ship:
            board[r][c] = "S"

    for r, c in mines:
        board[r][c] = "M"

    lr, lc = lucky
    board[lr][lc] = "L"

    print("\n     1 2 3 4 5")
    for i in range(size):
        row_values = " ".join(board[i])
        print(f"{i+1} | {row_values}")
    print()
#------------------------------------


#Test in Terminal 
if __name__ == "__main__":
    setup = set_up()
    print ("Game Set, Here are your starting positions!:")
    print(setup)

#Loop for player: choose ship, then move ship in chosen direction.
while True: 
    
    ship_choice = input("Move ship 1 or 2? (input 1, 2, or 'q' to exit game): ").strip()
    if ship_choice.lower() == 'q':
        print("Game Exited")
        break
    if ship_choice not in ["1", "2"]:
        print ("Invalid. Please type in 1 or 2.")
        continue 
    
    ship = 'ship1' if ship_choice == "1" else 'ship2'
    other_ship = 'ship2' if ship_choice == "1" else 'ship1'
    
    direction = input ("Enter direction to move (up, down, left, or right): ").strip().lower()
    if direction not in ["up", "down", "left", "right"]:
        print ("Invalid. Please type in up, down, left, or right")
        continue 
    
    #Move the ship and show update 
    setup[ship], message = move_ship(setup[ship], direction, setup[other_ship])
    
    #Show updated coordinates of ship moved w/ message from move_ship
    print(f"{ship.capitalize()} New Position: {setup[ship]}")
    print(message)
#-------------------------------------------------------------------------
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
  #---------------------------------------------------------------------------
#Anzhi

BOARD = 5
SHIPS = 2
SHIP_LENGTHS = [2, 3]
MINES = 2
LUCKY = 1

def lucky_reset(ships, used_space, board_size=BOARD):
    
    forbidden = set(used_space)

    new_ships_coor = []

    for ship in ships:
        length = len(ship)

        while True:
            start_r = random.randint(0, board_size - 1)
            start_c = random.randint(0, board_size - 1)

            direction = random.choice(["h", "v"])

            candidate = []
            valid = True

            for i in range(length):
                if direction == "h":
                    r = start_r
                    c = start_c + i
                else:
                    r = start_r + i
                    c = start_c

                
                if r < 0 or r >= board_size or c < 0 or c >= board_size:
                    valid = False
                    break

              
                if (r, c) in forbidden:
                    valid = False
                    break

                candidate.append((r, c))

            if not valid:
                continue
            new_ships_coor.append(candidate)

            for cell in candidate:
                forbidden.add(cell)

            break

    return new_ships_coor
