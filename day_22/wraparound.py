import re
from enum import Enum

class Tile(Enum):
    Empty = 0,
    Wall  = 1

class Cell:
    def __init__(self, content):
        self.content = content
        self.D = { }

with open('input') as input:
    text = input.read()[:-1]
    maze, directions = text.split('\n\n')
    maze = [line for line in maze.split('\n')]
    n = len(maze)
    m = len(maze[0])
    maze = {(i, j): Cell(maze[i][j]) for i in range(len(maze)) for j in range(len(maze[i])) if maze[i][j] != ' '}
    directions = re.findall(r'\d+|L|R', directions)

    for i in range(n):
        j = 0
        while (i, j) not in maze:
            j += 1
        start = (i, j)
        while (i, j+1) in maze:
            maze[(i, j)]  .D[( 1, 0)] = maze[(i, j+1)]
            maze[(i, j+1)].D[(-1, 0)] = maze[(i, j  )]
            j += 1
        end = (i, j)
        maze[start].D[(-1, 0)] = maze[end]
        maze[end  ].D[( 1, 0)] = maze[start]
    for j in range(m):
        i = 0
        while (i, j) not in maze:
            i += 1
        start = (i, j)
        while (i+1, j) in maze:
            maze[(i, j)]  .D[(0,  1)] = maze[(i+1, j)]
            maze[(i+1, j)].D[(0, -1)] = maze[(i, j  )]
            i += 1
        end = (i, j)
        maze[start].D[(0, -1)] = maze[end]
        maze[end  ].D[(0,  1)] = maze[start]

    position = maze[sorted(maze)[0]]
    direction = (1, 0)
    for command in directions:
        if command.isnumeric():
            for _ in range(int(command)):
                position = position.D[direction] if position.D[direction].content != '#' else position
        elif command == 'L':
            direction = (-direction[1], -direction[0])

    #(1, 0) -> (0, -1)
    #(-1, 0) -> (0, 1)
    #(0, 1) -> (-1, 0)

    print(start)
#with open('output', 'w') as output:
#    output.write(str(root_value) + '\n')
#    output.write(str(human_value) + '\n')