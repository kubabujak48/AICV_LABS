import numpy as np
import collections

def pathSearch(queue):
    if not queue:   # When all possible steps has been visited
        return
    step = queue[0]  # Check first possible step in the queue
    x, y = step[:2]  # Locate current position in the maze
    maze[x, y] = "+"  # Mark position where we have been

    # Checking move availability
    if(moveRules(x, y - 1) == True): # Go down
        queue.append([x, y - 1])

    if (moveRules(x, y + 1) == True):  # Go up
        queue.append([x, y + 1])

    if (moveRules(x + 1, y) == True):  # Go right
        queue.append([x + 1, y])

    if (moveRules(x - 1, y) == True):  # Go left
        queue.append([x - 1, y])
    # Reset queue
    queue.popleft()
    # Repeat steps
    pathSearch(queue)


def moveRules(x, y):
    if not (0 <= x < horizontal and 0 <= y < vertical):
        return False
    elif (maze[x, y] == "#" or maze[x,y] == "*"):
        return True
    else:
        return False


# Defining our maze
maze = np.array([["#", "#", "#", "*", "*", "*", "#", "#"],
                 ["#", "*", "*", "*", "#", "*", "#", "#"],
                 ["#", "*", "#", "#", "#", "*", "#", "#"],
                 ["*", "*", "*", "*", "#", "G", "#", "#"],
                 ["*", "#", "#", "#", "#", "*", "#", "#"],
                 ["*", "#", "#", "*", "*", "*", "#", "#"],
                 ["*", "#", "#", "*", "#", "#", "#", "#"],
                 ["S", "*", "*", "*", "#", "#", "#", "#"]])

# Defining dimensions
horizontal = 8
vertical = 8


# Find desired spots
for x in range(0, horizontal):
    for y in range(0, vertical):
        if(maze[x, y] == "G"):
            goal = [x, y]
        elif(maze[x, y] == "S"):
            start = [x, y]


#Main
queue = collections.deque([start])
print("Original maze:", maze, sep='\n')
pathSearch(queue)
print("Solution to the maze: ", maze, sep='\n')
