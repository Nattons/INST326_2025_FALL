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

def validate_input(player_input, board_size=5):
    """
    Validates a coordinate input like '2,3' and converts it to (row, col).
    Ensures the input is properly formatted and inside the 5x5 board.

    Args:
        player_input (str): The coordinate typed by the player (ex: '2,3')
        board_size (int): Size of the board (default 5)

    Returns:
        tuple or None: (row, col) if valid, otherwise None.
    """

    if not player_input:
        print("Enter a coordinate like 2,3.")
        return None

    move = player_input.replace(" ", "")

    # Must contain a comma
    if "," not in move:
        print("Invalid format. Use x,y like 2,3.")
        return None

    parts = move.split(",")

    # Must have two numbers
    if len(parts) != 2 or not parts[0].isdigit() or not parts[1].isdigit():
        print("Invalid format. Coordinates must be numbers (0–4).")
        return None

    x = int(parts[0])
    y = int(parts[1])

    # Check board boundaries
    if not (0 <= x < board_size and 0 <= y < board_size):
        print("Out of bounds. Coordinates must be between 0 and 4.")
        return None

    # Convert to (row, col)
    return (y, x)


def is_repeated_move(coords, used_space):
    """
    Check if the coordinate was already entered.
    
    Args:
        coords (tuple): The (row, col) coordinate
        used_space (set): All previously guessed coordinates

    Returns:
        bool: True if coordinate already used, else False.
    """
    return coords in used_space


def check_grid(player_input, used_space=None, enemy_ships=None, board_size=5):
    """
    Checks if a move is valid, new, and determines hit or miss.

    Args:
        player_input (str): The x,y coordinate input by the player
        used_space (set): Coordinates already guessed
        enemy_ships (set): Enemy ship positions

    Returns:
        tuple or None: Valid (row, col) coordinate or None if invalid
    """

    used_space = set() if used_space is None else used_space
    enemy_ships = set() if enemy_ships is None else enemy_ships

    coords = validate_input(player_input, board_size)

    if coords is None:
        return None  # Input invalid

    # Check duplicate move
    if is_repeated_move(coords, used_space):
        print("You already played that coordinate.")
        return None

    # Record move
    used_space.add(coords)

    row, col = coords

    # Hit or miss logic
    if coords in enemy_ships:
        print(f"HIT at ({col},{row})!")
    else:
        print(f"Miss at ({col},{row}).")

    # Show full move history
    print("\nPrevious moves:")
    for (r, c) in sorted(used_space):
        print(f"({c},{r})", end=" ")
    print("\n")

    return coords
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
