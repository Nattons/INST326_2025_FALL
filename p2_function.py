
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
    


