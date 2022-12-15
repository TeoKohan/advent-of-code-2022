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

class SensorBeacon:
      def __init__(self, sx, sy, bx, by):
            self.sensor = V2(sx, sy)
            self.beacon = V2(bx, by)
            self.range  = V2.distance(self.sensor, self.beacon)

class Line:
      def __init__(self, left, right):
            self.left = left
            self.right = right

      def __eq__(self, B):
            return self.left == B.left and self.right == B.right

      def __iter__(self):
            for i in range(self.left, self.right + 1):
                  yield i

      def __repr__(self):
            return f'[{self.left} - {self.right}]'

      def length(self):
            return abs(self.left - self.right) + 1

      def intersects(A, B):
            return (A.right >= B.left and A.left <= B.right) or (A.left <= B.right and A.right >= B.left)

      def join(self, lines):
            L = []
            for line in lines:
                  if Line.intersects(self, line):
                        self.left  = min(self.left,  line.left)
                        self.right = max(self.right, line.right)
                  else:
                        L += [line]
            return L + [self]


with open('input') as input:
      text = input.read()[:-1]
      sensors_beacons = text.split('\n')

      sensors_beacons = [ re.findall(r'-?\d+', sensor_beacon) for sensor_beacon in sensors_beacons ]
      sensors_beacons = [ SensorBeacon(*list(map(int, sensor_beacon))) for sensor_beacon in sensors_beacons ]

      def beaconfree(depth):
            lines = []
            for sb in sensors_beacons:
                  if sb.range >= abs(sb.sensor.y - depth):
                        lines = Line(sb.sensor.x - sb.range + abs(sb.sensor.y - depth), sb.sensor.x + sb.range - abs(sb.sensor.y - depth)).join(lines)
            lines.sort(key = lambda l: l.left)
            return lines

      depth = 2000000
      free_space = sum([line.length() for line in beaconfree(depth)])
      sensors = {tuple(sb.sensor) for sb in sensors_beacons if sb.sensor.y == depth and any([Line.intersects(Line(sb.sensor.x, sb.sensor.x), line) for line in beaconfree(depth)]) }
      beacons = {tuple(sb.beacon) for sb in sensors_beacons if sb.beacon.y == depth and any([Line.intersects(Line(sb.beacon.x, sb.beacon.x), line) for line in beaconfree(depth)]) }
      free_space -= len(sensors) + len(beacons)

      n = 4000000
      tuning_frequency = 0
      for depth in range(0, n+1):
            
            def clamp(L):
                  R = []
                  for l in L:
                        if Line.intersects(Line(0, 0), l):
                              l = Line(0, l.right)
                        if Line.intersects(Line(n, n), l):
                              l = Line(l.left, n)
                        R += [l]
                  return R

            free = beaconfree(depth)
            free = clamp(free)
            if sum([line.length() for line in free]) != n+1:
                  tuning_frequency = (free[0].right + 1) * n + depth
                  break

with open('output', 'w') as output:
      output.write(str(free_space) + '\n')
      output.write(str(tuning_frequency) + '\n')