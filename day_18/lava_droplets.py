from collections import deque
from enum import Enum

class V3:
      def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

      def __add__(self, B):
            return V3(self.x + B.x, self.y + B.y, self.z + B.z)
      
      def __sub__(self, B):
            return V3(self.x - B.x, self.y - B.y, self.z - B.z)

      def distance(A, B):
            return abs(A.x - B.x) + abs(A.y - B.y) + abs(A.z - B.z)

      def __repr__(self):
            return f'({self.x}, {self.y}, {self.z})'

      def __iter__(self):
            yield self.x
            yield self.y
            yield self.z

class Material(Enum):
      Lava  = 0,
      Steam = 1
D = [V3(1, 0, 0), V3(-1, 0, 0), V3(0, 1, 0), V3(0, -1, 0), V3(0, 0, 1), V3(0, 0, -1)]

in_out_surface = 0
out_surface = 0
with open('input') as input:
      droplets = input.read()[:-1]
      droplets = droplets.split('\n')
      droplets = [V3(*list(map(int, drop.split(',')))) for drop in droplets] 
      
      d_min = V3(min([drop.x for drop in droplets]), min([drop.y for drop in droplets]), min([drop.z for drop in droplets])) - V3(1, 1, 1)
      d_max = V3(max([drop.x for drop in droplets]), max([drop.y for drop in droplets]), max([drop.z for drop in droplets])) + V3(1, 1, 1)

      board = {tuple(drop) : Material.Lava for drop in droplets}
      for drop in droplets:
            for dir in D:
                  in_out_surface += 0 if tuple(drop + dir) in board else 1
      
      board[tuple(d_min)] = Material.Steam
      steam = deque([d_min])
      while len(steam) > 0:
            active = steam.popleft()
            for dir in D:
                  candidate = active + dir
                  if d_min.x <= candidate.x <= d_max.x and d_min.y <= candidate.y <= d_max.y and d_min.z <= candidate.z <= d_max.z and tuple(candidate) not in board:
                        board[tuple(candidate)] = Material.Steam
                        steam += [candidate]
      
      for drop in droplets:
            for dir in D:
                  out_surface += 1 if tuple(drop + dir) in board and board[tuple(drop + dir)] == Material.Steam else 0

with open('output', 'w') as output:
      output.write(str(in_out_surface) + '\n')
      output.write(str(out_surface) + '\n')