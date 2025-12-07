import random

#Global Function for ship movement
def move_ship(ship, direction, other_ship):
    """Move a ship one cell in specified direction on a 5x5 grid. Ship can
    overlap mines and lucky rest but not over other players own ship or over
    grid boundaires. 
    
    Parameters:
        ship (list of tuple): coordinates of the ship to move. 
        direction (str): direction of the ship (up, down, left, right).
        other_ship (list of tuple): coordinate of other ship the player has not moved.
    
    Returns:
        new_ship (list of tuple): updated coordiantes of moved ship if validly moved,
        if not original coordiantes remain.
        message (str): messages indicating the result of a move.
    """
    if direction == "up":
        new_ship = [(r-1, c) for r, c in ship]
    elif direction == "down":
        new_ship = [(r+1, c) for r, c in ship]
    elif direction == "left":
        new_ship = [(r, c-1) for r, c in ship]
    elif direction == "right":
        new_ship = [(r, c+1) for r, c in ship]
    else: 
        return ship, "Invalid Direction"
    
    #Checks for boundray of the grid
    for r, c in new_ship:
        if r < 0 or r > 4 or c < 0 or c > 4:
            return ship, "Cannot Move!: reached the edge of board."
   
   #Checks collision with other ship
    for pos in new_ship:
        if pos in other_ship:
            return ship, "Collision Imminent!: pick another direction."
    
    return new_ship, "Ship moved successfully!"





class Board: 
    """Represents the 5x5 Battleship game board for a single player. Tracks a player's
    ships, hidden sea mines, and a lucky rest cell placed at random.
    
    Attributes:
        size (int): the size of the broad (5x5 grid)
        ship1 (list of tuple): coordinates of the first ship.
        ship2 (list of tuple): coordinates of the second ship. 
        mines (list of tuple): coordinates of hidden sea mines.
        lucky (tuple or None): coordinate of the lucky rest.
        occupied (set of tuple): all occupied coordinates (ship, mines, lucky rest)
    """
    
    
    def __init__(self, size =5):
        """Initalize empty board."""
        self.size = size
        self.ship1 = []
        self.ship2 = []
        self.mines = []
        self.lucky = None
        self.occupied = set()
        
        
    def get_avaliable_postions(self):
        """Returns a list of all unoccupied coordinates on the board.
        
        Returns:
            list of tuple: coordinates that are not part of any ship.
        """
        all_coords = [(r, c) for r in range(self.size) for c in range(self.size)]
        ships_coords = set(self.ship1 + self.ship2)
        return [coord for coord in all_coords if coord not in ships_coords]
     
     
    def validate_ship(self, start, direction, length):
        """Validates ship placement to fit the board and aviod overlap.
        
        Parameters:
            start (tuple): starting coordinate (row, col) of the ship.
            direction (str): 'h' for horizontal or 'v' for vertical placement.
            length (int): length of the ship.
            
        Returns:
            list of tuple or None: valid coordinates for the ship, None if placement
            is not possible.
        """
        r, c = start 
        
        #Horizontal Ship
        if direction == "h":
            #Shift left if it would go off board
            if c + length - 1 >=self.size:
                c = self.size - length 
              
            #Check for overlap and try to move left if needed     
            while c >=0:
                cells = [(r, c + i) for i in range(length)]
                if all (cell not in self.occupied for cell in cells):
                    return cells
                c -= 1
            return None
        
        # Vertical ship
        else:
            if r + length - 1 >= self.size:
                r = self.size - length

            while r >= 0:
                cells = [(r + i, c) for i in range(length)]
                if all(cell not in self.occupied for cell in cells):
                    return cells
                r -= 1  
            return None
    
    
    def manual_place_ship(self, ship_name, length=2):
        """Allow player to manually place ship starting postitions.
        
        Parameters:
            ship_name (str): name of the ship used for prompts.
            length (int): length of ship (2 by default)
        
        Returns:
            list of tuple: coordinates of the successfully placed ship.
        """
        print(f"\nPlace {ship_name}(length{length})")
        
        while True:
            try: 
                available = [(r, c) for r in range(self.size) for c in range(self.size)
                             if (r, c) not in self.occupied]
                print("Available coordiantes to place the ship:", available)
                
                r, c = map(int, input("Enter starting coordinate (row col): ").split())
                direction = input("Direction (h for horizontal, v for vertical): ").lower()
                if direction not in ("h", "v"):
                    print("Invalid direction. Try again.")
                    continue
                
                cells = self.validate_ship((r, c), direction, length)
                if cells is None:
                    print("Invalid placement. Try again.")
                    continue
                
                #Place ship
                self.occupied.update(cells)
                print(f"{ship_name} placed at {cells}")
                return cells
            except ValueError:
                print("Invalid input. Enter two numbers seperated by a space.")
    

    def place_mines(self, num_mines=2):
        """Randomly place hidden sea mines on the board, mines do not overlap with
        other mines or ships
        
        Parameters: 
            num_mines (int): number of mines to place (2 by default).
        """
        while len(self.mines) < num_mines:
            r = random.randint(0, self.size -1)
            c = random.randint(0, self.size -1)
            if (r, c) not in self.occupied:
                self.mines.append((r,c))
                self.occupied.add((r, c))
                

    def place_lucky(self):
        """Randomly place a lucky rest cell on the board, rest does not overlap with
        ships or mines.
        """
        while True:
            r = random.randint(0, self.size -1)
            c = random.randint(0, self.size -1)
            if (r, c) not in self.occupied:
                self.lucky = ((r,c))
                self.occupied.add((r, c))
                break
    
 
 
 
            
class Player:
    """Represents a battleship player, each player has a name, board, can 
    place there ships, and move them during the game.
    
    Attributes:
        name (str): name of player.
        board (Board): the player's game board.
    """
    
    
    def __init__(self, name):
        """Initialize a player with a name and an empty board.
        
        Parameters:
            name (str): name of the player.
        """
        self.name = name
        self.board = Board()
    
    
    def setup(self):
        """Sets up player board by manually placing ships and randomly placing mines 
        and lucky rest cell.
        
        Side effects:
            updates self.board.ship1, self.board.ship2, self.board.mines, and
            self.board.lucky.
            prints setup prompts and confirmations to the terminal.
        """
        print(f"\n{self.name} Setup")
        self.board.ship1 = self.board.manual_place_ship("Ship 1")
        self.board.ship2 = self.board.manual_place_ship("Ship 2")
        self.board.place_mines()
        self.board.place_lucky()
        print(f"{self.name}'s setup is complete! Sea Mines and Lucky Rest have been placed.")
    
    
    def move_ship(self, ship_number, direction):
        """Moves one of the player's ships in the specified direction.
        
        Parameters:
            ship_number (int): the ship to move (1 or 2).
            direction (str): direction to move the ship (up, down, left, right).
        
        Returns:
            new_ship (list of tuple): updated coordinates of the mved ship.
            message (str): message describing the result of the move.
        """
        if ship_number == 1:
            current_ship = self.board.ship1
            other_ship = self.board.ship2
        else:
            current_ship = self.board.ship2
            other_ship = self.board.ship1
        
        new_ship, message = move_ship(current_ship, direction, other_ship)
        
        if "successfully" in message:
            if ship_number == 1:
                self.board.ship1 = new_ship
            else:
                self.board.ship2 = new_ship
                
        return new_ship, message
    
    



class BattleshipGame:
    """Represents a battleship game between two players.
    
    Attributes:
        player1 (Player): the first player.
        player2 (Player): the second player.
    """
    
    
    def __init__(self):
        """Initializes the Battleship game with two players named "Player 1" and 
        "Player 2".
        """
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
    
    
    def setup_game(self):
        """Sets up the game by configuring both players' boards.Player can set
        ships manually.Randomly places sea mines and lucky rest cell for each player."""
        self.player1.setup()
        self.player2.setup()
    
   
    def play_turn(self, player):
        """Executes a single turn for a player, allowing them to move ships.
        
        Parameters: 
            player (Player): the player whose turn is being executed.
        
        Side effects:
            updates the positions of teh players ships.
            prints movement prompts and results to terminal.
        """
        print(f"\n{player.name}'s Turn")
        
        for ship_number in [1,2]:
            while True:
                direction = input(f"Enter direction to move ship{ship_number}(up, down, left, right) or 's' to skip: ").strip().lower()
                
                if direction == 's':
                        print(f"Ship {ship_number} skipped")
                        break
                    
                if direction not in ["up", "down", "left", "right"]:
                    print("Invalid. Please type up, down, left, or right")
                    continue 
                
                new_pos, message = player.move_ship(ship_number, direction)
                
                print(f"Ship 1 Position: {player.board.ship1}")
                print(f"Ship 2 Position: {player.board.ship2}")
                print(message)
                
                if "successfully" in message:
                    break
                
         

#Terminal Testing   
if __name__ == "__main__":
    """Runs the Battleship game in the terminal."""
    
    game = BattleshipGame()
    game.setup_game()
    
    players = [game.player1, game.player2]
    turn = 0
    
    while True:
        current_player = players[turn % 2]
        
        game.play_turn(current_player)
        
           # Display message for testing
        print(f"{current_player.name} end of turn postions:")
        print("Ship 1:", current_player.board.ship1)
        print("Ship 2:", current_player.board.ship2)

        # Optionally quit
        cont = input("Continue game? (y/n): ").strip().lower()
        if cont == 'n':
            print("Game Exited.")
            break

        turn += 1
    
 
    
          
  

        
        
        

    


