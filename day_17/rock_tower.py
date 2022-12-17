import re

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

ROCKS = [
      [
            ['.','.','.','.'],
            ['.','.','.','.'],
            ['.','.','.','.'],
            ['#','#','#','#']
      ],
      [
            ['.','.','.','.'],
            ['.','#','.','.'],
            ['#','#','#','.'],
            ['.','#','.','.']
      ],
      [
            ['.','.','.','.'],
            ['.','.','#','.'],
            ['.','.','#','.'],
            ['#','#','#','.']
      ],
      [
            ['#','.','.','.'],
            ['#','.','.','.'],
            ['#','.','.','.'],
            ['#','.','.','.']
      ],
      [
            ['.','.','.','.'],
            ['.','.','.','.'],
            ['#','#','.','.'],
            ['#','#','.','.']
      ],
]

class Board:
      def __init__(self, wind, rocks):
            self.wind = wind
            self.wind_pointer = 0
            self.rocks = rocks
            self.rock_pointer = 0
            self.top = 0
            self.board = []

      def __repr__(self):
            return str(self.board)

      def get_rock(self):
            rock = self.rocks[self.rock_pointer]
            self.rock_pointer = (self.rock_pointer + 1) % len(self.rocks)
            return rock

      def get_wind(self):
            wind = self.wind[self.wind_pointer]
            self.wind_pointer = (self.wind_pointer + 1) % len(self.wind)
            return wind

      def drop_rock(self):
            rock = self.get_rock()
            while (len(self.board) < self.top + 7):
                  self.board += [['.'] * 7]

            cursor = V2(2, self.top + 3)
            
            def push(cursor, direction, rock):
                  for x, y in [(x, y) for x in range(4) for y in range(4)]:
                        y = 3 - y
                        if rock[y][x] == '#':
                              if cursor.x + direction.x < 0 or cursor.x + x + direction.x > 6 or cursor.y + direction.y < 0:
                                    return False
                              V = V2(x, 3 - y)
                              P = cursor + direction + V
                              if self.board[P.y][P.x] == '#':
                                    return False
                  return True
            
            wind = V2(1, 0) if self.get_wind() == '>' else V2(-1, 0)
            cursor = cursor + wind if push(cursor, wind, rock) else cursor
            while push(cursor, V2(0, -1), rock):
                  cursor += V2(0, -1)
                  wind = V2(1, 0) if self.get_wind() == '>' else V2(-1, 0)
                  cursor = cursor + wind if push(cursor, wind, rock) else cursor

            for x, y in [(x, y) for x in range(4) for y in range(4)]:
                  if rock[y][x] == '#':
                        V = V2(x, 3-y)
                        P = cursor + V
                        self.board[P.y][P.x] = '#'
                        self.top = max(self.top, P.y+1)

height_2022 = 0
height_1000000000000 = 0
with open('input') as input:
      wind  = input.read()[:-1]
      board = Board(wind, ROCKS)

      for i in range(2022):
            board.drop_rock()
      height_2022 = board.top

      n = 23 * 75
      board = Board(wind, ROCKS)
      rock_count = 0
      remaining = 1000000000000 % n
      
      for i in range(remaining):
            board.drop_rock()
            rock_count += 1
      
      class Step:
            def __init__(self, wind, top):
                  self.wind = wind
                  self.top = top
            def __eq__(self, B):
                  return self.wind == B.wind and self.top == B.top
            def __repr__(self):
                  return str(self.wind) + ', ' + str(self.top)

      x, y, z = Step(-3, 0), Step(-2, 0), Step(-1, 0)
      while x.wind != y.wind or y.wind != z.wind or y.top - x.top != z.top - y.top:
            for i in range(n):
                  board.drop_rock()
                  rock_count += 1
            x, y, z = y, z, Step(board.wind_pointer, board.top)
      
      remaining = 1000000000000 - rock_count
      increment = z.top - y.top

      height_1000000000000 = board.top + increment * (remaining // n)


      
with open('output', 'w') as output:
      output.write(str(height_2022) + '\n')
      output.write(str(height_1000000000000) + '\n')