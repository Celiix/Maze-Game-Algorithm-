# Author Celisha Daramy - 1340551

##### SOURCES #####
#astar.py - Jan Shah
#https://www.pygame.org/project/3437 - Jack Folsom
#https://github.com/ashrafsusts19/python-sample-codes-zadeed/blob/master/Pygame/Mage%20Generator.py - ashrafsusts19
#https://gist.github.com/FrankRuis/4bad6a988861f38cf53b86c185fc50c3 - FrankRuis
#https://github.com/john-science/mazelib/blob/main/docs/MAZE_GEN_ALGOS.md#backtracking-generator - john-science
#https://www.webucator.com/article/python-color-constants-module/ - webucator
########################################

#### THE SET UP ####

# Here is all the modules that will be used throughout the code with the addition of the pygame for visualisation. 
import pygame
import random
from random import choice
import time
import pygame as pg
pygame.init()
pygame.mixer.init()


# This section of the code is to set up the pygame window that will display when the code is running. Here I have set the Height and Width of the window and also the  Fps (frames per second), this will increase or decrease the speed of frame rate of the maze game, I gave the Fps an averagr and commonly use number to make the program look smoother and to build, solove and complete the maze effifcently. I have also used the set caption fuunction to name the game as the window appears. The clock varible is used for the class Clock object to track the time but it's multi use can help aid the game's frame rate. 
Width = 500
Height = 500
Fps = 60 
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption ("Assignment - Maze Game - Celisha Daramy ")
clock = pygame.time.Clock()

done = False

# This section shows the varibles I shall use within this program. Varibles with empty brackets will be an empty list until I call or use it for value within the code. The x and y varibles is the axis of where it is going to be the positioned of where the starting (finishing point) of the maze. The w is the widith of each cells in the maze, this is first displayed by 20 x 20 squares when the program first starts to run.
x = 0                   
y = 0                    
w = 20                   
grid = []
visited = []
stack = []
solution = {}

#This small section is the chosen colours I will use and to be displayed in the maze game.
Blue = (25,25,112)
Red = (220,20,60)
Purple = (180,82,205)
Green = (50,205,50)


# Here in this part of the code is where the grid is to be built, x is coordinated to the start of the position whilst y will start a new row each time to form the grid. By using one of the colours from the previous section to out the each of the cell squares (all four sides) to make it visible, this will repeat and add to the grid list (Line) as the cell will move to a new position, the grid will also be constructed within the range I have plaaced.
def build_grid(x, y, w):
    for i in range(1,21):
        x = 20                                                            
        y = y + 20                                                        
        for c in range(1, 21):   
            pygame.draw.line(screen, Blue, [x + w, y + w], [x, y + w])  
            pygame.draw.line(screen, Blue, [x, y + w], [x, y])       
            pygame.draw.line(screen, Blue, [x, y], [x + w, y])           
            pygame.draw.line(screen, Blue, [x + w, y], [x + w, y + w])    
            grid.append((x,y))                                            
            x = x + 20                                                    


# Here the section is about the pathway. The first part of the code is used to draw the width of a single cell within the grid and this will update as the program is running.
#The second part of this code chanages the colour of the pathway when a single cell is vistied thus leaving a trail for the pathway and making a ramdomised maze.
#The last section of this code is the solution of showing after the maze is created, the shortest path to find the end of the maze. By using the recursive backtracker algoritm (A randomised version of the depth-first search algorithm) the solution is automatically found after the program has generated a maze. 
#All of this will be updated as the program carries by using the function pygame.display.update() 
def single_cell( x, y):
    pygame.draw.rect(screen, Red, (x + 1, y + 1, 18, 18), 0)          
    pygame.display.update()


def backtracking_cell(x, y):
    pygame.draw.rect(screen, Purple, (x + 1, y + 1, 18, 18), 0)        
    pygame.display.update()                                        


def solution_cell(x,y):
    pygame.draw.rect(screen, Green, (x + 8, y + 8, 5, 5), 0)             
    pygame.display.update()                                        



# These series of coding allows the program to draw the shape more of the width of the cell and animates this as the walls will remove so the maze path will continue like a long rectangle.
def push_down(x, y):
    pygame.draw.rect(screen, Purple, (x +  1, y + 1, 19, 39), 0)
    pygame.display.update()
def push_up(x, y):
    pygame.draw.rect(screen, Purple, (x + 1, y - w + 1, 19, 39), 0)    
    pygame.display.update()                                              
def push_right(x, y):
    pygame.draw.rect(screen, Purple, (x + 1, y + 1, 39, 19), 0)
    pygame.display.update()
def push_left(x, y):
    pygame.draw.rect(screen, Purple, (x - w +1 , y + 1, 39, 19), 0)
    pygame.display.update()

### THE MAZE ###


# Within this section of the program the start posititon of the maze is shown and the start cell will be added into the stack 'list' (the stack varible that was shown in THE SET UP section of the program) once cell is visited, it will go into the visted list. This will loop until the the stack becomes empty.
def carve_out_maze(x,y):
    single_cell(x, y)                                              
    stack.append((x,y))                                            
    visited.append((x,y))                                          
    while len(stack) > 0:                                          

# Whilst the previous code is running, here is the program or condintions the code goes through within the grid. It will check if any of the surrounding cells are available (right, left, down and up) is available and if the cell is obtainable then it will be added to the cell list. This will happen until all cells are not obtainable.        
        time.sleep(.07)                                            
        cell = []                                                  
        if (x + w, y) not in visited and (x + w, y) in grid:       
            cell.append("right")                                   

        if (x - w, y) not in visited and (x - w, y) in grid:       
            cell.append("left")

        if (x , y + w) not in visited and (x , y + w) in grid:     
            cell.append("down")

        if (x, y - w) not in visited and (x , y - w) in grid:      
            cell.append("up")


# Here is where the code will look to see if the cell list has nothing inside it, when confirmed it will then select a random cell within the list.
        if len(cell) > 0:                                          
            cell_chosen = (random.choice(cell))                    

            if cell_chosen == "right":                  # if the right cell is chosen (same thing for left, up or down), call upon the "push_...
                                                        # " function for that specific cell. (right, left, up or down)
                push_right(x, y)                        
                solution[(x + w, y)] = x, y             # The solution variable then becomes the dictionary key, this then becomes a...
                                                        # new cell and current cell within the maze grid.

                x = x + w                               # The cell then becomes the current cell in use.
                visited.append((x, y))                  # This is then added to the visited list
                stack.append((x, y))                    # To which it takes position as the current cell on to the stack list.

            elif cell_chosen == "left":
                push_left(x, y)
                solution[(x - w, y)] = x, y
                x = x - w
                visited.append((x, y))                 # This process is repeated for all of the of the other directions (left, up and down)
                stack.append((x, y))

            elif cell_chosen == "up":
                push_up(x, y)
                solution[(x , y - w)] = x, y
                y = y - w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "down":
                push_down(x, y)
                solution[(x , y + w)] = x, y
                y = y + w
                visited.append((x, y))
                stack.append((x, y))

        else:
            x, y = stack.pop()                # When there is no cells to obtain one will be popped from the stack list
            single_cell(x, y)                 # This function will display the back tracking pathway
            time.sleep(.05)                                       
            backtracking_cell(x, y)           # When the maze is showing the recursive back tracking the colour of the cell will momentarily...
                                              #change to the colour chosen from the colours varible (from THE SET UP section) 


### DEPTH FIRST - BACK TRACKING ALGORITHM ###
def plot_route_back(x,y):
    solution_cell(x, y)              # This line of code will have the list of everything to find a pathway from 
                                     #the end to the start of the maze
    while (x, y) != (20,20):         
        x, y = solution[x, y]        
        solution_cell(x, y)           
        time.sleep(.1)

# Here is where the maze will start at the beggining of the maze with the inclusion of calling the other functions.
x, y = 20, 20                   
build_grid(40, 0, 20)             
carve_out_maze(x,y)               
plot_route_back(400, 400)         


### MAIN GAME LOOP ### 

# All of code will be function whilst program is running true or being operational and when the maze is complete the user can close the window.
running = True
while running:
    clock.tick(Fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   