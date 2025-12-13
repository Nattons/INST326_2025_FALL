INST326
Prof. Bills 
Final Project - README
Group Members: Endrias Alamerew, Jishan Farazi, An-Zhi Lu, Natalie Siliezar 
Group Name: 4Ships


Files In Repository 


.DS_Store
This file contains no text or code, it is an added file for the earliest testing in GitHub.


326 final first deliverable.py
Early code and function for lucky reset, was created as part of the first deliverable assignment. 


Main.py
This is our main code.


P_4_CheckingGrid.py
Early code and function for checking the grid, was created as part of the first deliverable assignment. 


Ship_Testing.py​​
Only testing code does not matter to the project.


Ship_teasting2.py
Only testing code does not matter to the project.


P2_function.py
Early code and function for ship direction, was created as part of the first deliverable assignment. 


Text_file.py
This file has nothing to do with the code


text_file_2.py
This file has nothing to do with the code










Run the Program 


1. Clone the repository from GitHub.
2. Open the Terminal.
3. Navigate to the project directory.
4. Run the program using: python main.py
This program does not take any command-line arguments.
All user input is handled interactively during gameplay.


Using Program 
Setup Phase
Each player places Ship 1 and Ship 2 on their board. You will be prompted to:
Enter starting coordinates (row  col), example (2 3)
Choose a direction: horizontal (h) or vertical (v)
Mines and a lucky cell are placed automatically.
Turn Phase
On your turn:
Move your ships (up, down, left, right) or skip movement with s.
Fire at enemy coordinates (row col).
Game Rules
A ship hit increases your score by 1. Sinking a ship increases your score by 5.
Hitting the lucky grid resets the enemy ship's positions.
Ships immobilized by mines cannot move.
The first player to sink all enemy ships wins.
End of Game
The game ends when all enemy ships are sunk or a player types quit when prompted.
Board Symbols
. : empty cell
S : ship (shown only when revealed)
H : hit
M : miss




Annotated bibliography
Brown, S. (2024, July 19). How to play the Battleship board game. The Spruce Crafts. https://www.thesprucecrafts.com/the-basic-rules-of-battleship-411069
This source was used to understand Battleship rules and guide the design of ship placement, firing, scoring, and movement mechanics in our text-based game.




Attribution
 
Method/Function
Primary Author
Techniques Demonstrated 
display_board
Jishan
keyword arguments
Main
Jishan
composition of two custom classes


get_avaliable_positions 
Natalie Siliezar 
comprehensions or generator expressions


play_turn 
Natalie Siliezar 
sequence unpacking
validate_ship_position
Endrias
Regular expressions
check_special_cells
Endrias
f-strings containing expressions
fire
Anzhi
Optional parameter
lucky_reset
Anzhi
set operations


