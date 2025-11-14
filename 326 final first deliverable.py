import random

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
            
                

