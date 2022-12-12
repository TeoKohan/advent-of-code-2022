from collections import deque

class Cell:
      def __init__(self, value):
            self.value = ord(value) - ord('a')
            self.visited  = False
            self.distance = None
            self.N = []

with open('input') as input:
      text = input.read()
      grid = text.split('\n')[:-1]
      grid = [[i for i in line]for line in grid]

      n, m = len(grid), len(grid[0])

      for i in range(n):
            for j in range(m):
                  if grid[i][j] == 'S':
                        S = (i, j)
                        grid[i][j] = 'a'
                  if grid[i][j] == 'E':
                        E = (i, j)
                        grid[i][j] = 'z'
      
      grid = [[Cell(i) for i in line]for line in grid]

      for i in range(len(grid)):
            for j in range(len(grid[i])):
                  A = grid[i][j]
                  if i > 0:
                        B = grid[i-1][j]
                        A.N += [B] if A.value - B.value <= 1 else []
                  if j < m - 1:
                        B = grid[i][j+1]
                        A.N += [B] if A.value - B.value <= 1 else [] 
                  if i < n - 1:
                        B = grid[i+1][j]
                        A.N += [B] if A.value - B.value <= 1 else []
                  if j > 0:
                        B = grid[i][j-1]
                        A.N += [B] if A.value - B.value <= 1 else [] 

      E = grid[E[0]][E[1]]
      E.visited = True    
      E.distance = 0
      travel = deque([E])

      while len(travel) > 0:
            current = travel.popleft()
            for cell in current.N:
                  if cell.visited == False:
                        cell.distance = current.distance + 1
                        cell.visited = True
                        travel += [cell]
                        
with open('output', 'w') as output:
      output.write(str(grid[S[0]][S[1]].distance) + '\n')
      ground = [cell.distance for line in grid for cell in line if cell.value == 0 and cell.distance != None]
      output.write(str(min(ground)) + '\n')