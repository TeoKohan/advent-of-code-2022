import re
import os
clear = lambda: os.system('clear')

class V2:
      def __init__(self, x, y):
            self.x = x
            self.y = y

      def __add__(self, B):
            return V2(self.x + B.x, self.y + B.y)

      def distance(A, B):
            return abs(A.x - B.x) + abs(A.y - B.y)

      def __repr__(self):
            return f'({self.x}, {self.y})'

      def __iter__(self):
            yield self.x
            yield self.y

class SensorBeacon:
      def __init__(self, sx, sy, bx, by):
            self.sensor = V2(sx, sy)
            self.beacon = V2(bx, by)
            self.range  = V2.distance(self.sensor, self.beacon)

with open('input') as input:
      text = input.read()[:-1]
      rocks = text.split('\n')
      rocks = [line.split('->') for line in rocks]
      rocks = [[V2(*list(map(int, coord.split(',')))) for coord in line] for line in rocks]

      xs = [v.x for line in rocks for v in line]
      ys = [v.y for line in rocks for v in line]
      min_x, max_x = min(xs), max(xs)
      max_y = max(ys)

      sand_grid = [ ['.'] * (max_x - min_x + 1) for _ in range(max_y + 1)]
      for line in rocks:
            for i in range(len(line) - 1):
                  v, w = line[i], line[i+1]
                  if v.x == w.x:
                        for y in range(min(v.y, w.y), max(v.y, w.y) + 1):
                              sand_grid[y][v.x - min_x] = '#'
                  if v.y == w.y:
                        for x in range(min(v.x, w.x), max(v.x, w.x) + 1):
                              sand_grid[v.y][x - min_x] = '#'
      sand_grid[0][500 - min_x] = 'S'

      G = [line[:] for line in sand_grid]

      def print_grid(grid):
            for line in grid:
                  print(''.join([c for c in line]))

      def place_sand(x, y, grid):
            if y+1 > max_y:
                  return False
            elif grid[y+1][x] == '.':
                  return place_sand(x, y+1, grid)
            elif x-1 < 0:
                  return False
            elif grid[y+1][x-1] == '.':
                  return place_sand(x-1, y+1, grid)
            elif x+1 > max_x - min_x:
                  return False
            elif grid[y+1][x+1] == '.':
                  return place_sand(x+1, y+1, grid)
            else:
                  grid[y][x] = '█'
                  return True

      void_grains = 0
      while place_sand(500 - min_x, 0, G):
            void_grains += 1

      G = [line[:] for line in sand_grid] + [['.'] * len(G[0])] + [['#'] * len(G[0])]
      max_y += 2

      fill_grains = 0
      while G[0][500 - min_x] == 'S':
            if place_sand(500 - min_x, 0, G):
                  fill_grains += 1
            else:
                  G = [['.'] + line + ['.'] for line in G[:-1]] + [['#'] * (len(G[0]) + 2)]
                  min_x, max_x = min_x - 1, max_x + 1

with open('output', 'w') as output:
      output.write(str(void_grains) + '\n')
      output.write(str(fill_grains) + '\n')