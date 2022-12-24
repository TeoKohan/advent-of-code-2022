import re
from enum import Enum

class Tile(Enum):
    Empty = 0
    Wall  = 1

class Direction(Enum):
    top   = ( 0, -1)
    right = ( 1,  0)
    bot   = ( 0,  1)
    left  = (-1,  0)

class Cell:
    def __init__(self, content, x, y):
        self.x = x
        self.y = y
        self.content = content
        self.N = { }
        self.D = { D.value: D.value for D in Direction }

    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ', ' + self.content + ')'

class Face:
    def __init__(self, cells):
        self.cells = cells
        for i, j in [(i, j) for i in range(0, 50) for j in range(0, 50)]:
            self.cells[i][j].N[( 0, -1)] = self.cells[i-1][j] if i >  0 else None
            self.cells[i][j].N[( 1,  0)] = self.cells[i][j+1] if j < 49 else None
            self.cells[i][j].N[( 0,  1)] = self.cells[i+1][j] if i < 49 else None
            self.cells[i][j].N[(-1,  0)] = self.cells[i][j-1] if j >  0 else None
        self.border = {
            ( 1,  0): [cells[ i][49] for i in range(50)],
            ( 0,  1): [cells[49][ j] for j in range(50)],
            (-1,  0): [cells[ i][ 0] for i in range(50)],
            ( 0, -1): [cells[ 0][ j] for j in range(50)]
        }

    def connect(A, B, v, w, cross = False):
        v = v.value
        w = w.value
        for i in range(50):
            A.border[v][i].N[v] = B.border[w][(49 - i) if cross else i]
            A.border[v][i].D[v] = (-w[0], -w[1])
            B.border[w][i].N[w] = A.border[v][(49 - i) if cross else i]
            B.border[w][i].D[w] = (-v[0], -v[1])

facing = {
        ( 1,  0): 0,
        ( 0,  1): 1,
        (-1,  0): 2,
        ( 0, -1): 3
    }

planar_password = 0
cubic_password = 0
with open('input') as input:
    text  = input.read()[:-1]
    maze, directions = text.split('\n\n')
    maze  = [line for line in maze.split('\n')]
    faces = [
        Face([[Cell(maze[i][j], j, i) for j in range(50 , 100)] for i in range(0  , 50 )]),
        Face([[Cell(maze[i][j], j, i) for j in range(100, 150)] for i in range(0  , 50 )]),
        Face([[Cell(maze[i][j], j, i) for j in range(50 , 100)] for i in range(50 , 100)]),
        Face([[Cell(maze[i][j], j, i) for j in range(0  , 50 )] for i in range(100, 150)]),
        Face([[Cell(maze[i][j], j, i) for j in range(50 , 100)] for i in range(100, 150)]),
        Face([[Cell(maze[i][j], j, i) for j in range(0  , 50 )] for i in range(150, 200)])
    ]
    directions = re.findall(r'\d+|L|R', directions)

    #     00001111
    #     00001111
    #     00001111
    #     00001111
    #     2222
    #     2222
    #     2222
    #     2222
    # 33334444
    # 33334444
    # 33334444
    # 33334444
    # 5555
    # 5555
    # 5555
    # 5555

    def solve(directions, faces):
        cell = faces[0].cells[0][0]
        direction = (1, 0)
        for command in directions:
            if command.isnumeric():
                for _ in range(int(command)):
                    if cell.N[direction].content != '#':
                        direction, cell = cell.D[direction], cell.N[direction]
                    else:
                        break
            elif command == 'L':
                direction = (direction[1], -direction[0])
            elif command == 'R':
                direction = (-direction[1], direction[0])
        return (cell.y + 1) * 1000 + (cell.x + 1) * 4 + facing[direction]

    Face.connect(faces[0], faces[4], Direction.top  , Direction.bot  )
    Face.connect(faces[0], faces[1], Direction.right, Direction.left )
    Face.connect(faces[0], faces[2], Direction.bot  , Direction.top  )
    Face.connect(faces[0], faces[1], Direction.left , Direction.right)

    Face.connect(faces[1], faces[1], Direction.top  , Direction.bot  )

    Face.connect(faces[2], faces[2], Direction.right, Direction.left )
    Face.connect(faces[2], faces[4], Direction.bot  , Direction.top  )

    Face.connect(faces[3], faces[5], Direction.top  , Direction.bot  )
    Face.connect(faces[3], faces[4], Direction.right, Direction.left )
    Face.connect(faces[3], faces[5], Direction.bot  , Direction.top  )
    Face.connect(faces[3], faces[4], Direction.left , Direction.right)

    Face.connect(faces[5], faces[5], Direction.right, Direction.left )

    planar_password = solve(directions, faces)

    Face.connect(faces[0], faces[5], Direction.top  , Direction.left )
    Face.connect(faces[0], faces[1], Direction.right, Direction.left )
    Face.connect(faces[0], faces[2], Direction.bot  , Direction.top  )
    Face.connect(faces[0], faces[3], Direction.left , Direction.left,  cross = True )

    Face.connect(faces[1], faces[5], Direction.top  , Direction.bot  )
    Face.connect(faces[1], faces[4], Direction.right, Direction.right, cross = True)
    Face.connect(faces[1], faces[2], Direction.bot  , Direction.right)
    
    Face.connect(faces[2], faces[4], Direction.bot  , Direction.top  )
    Face.connect(faces[2], faces[3], Direction.left , Direction.top  )

    Face.connect(faces[3], faces[4], Direction.right, Direction.left )
    Face.connect(faces[3], faces[5], Direction.bot  , Direction.top  )

    Face.connect(faces[4], faces[5], Direction.bot  , Direction.right)

    cubic_password = solve(directions, faces)

with open('output', 'w') as output:
    output.write(str(planar_password) + '\n')
    output.write(str(cubic_password) + '\n')