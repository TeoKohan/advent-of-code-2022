with open('input') as input:
      text = input.read()
      moves = text.split('\n')[:-1]
      moves = [(move.split(' ')[0], int(move.split(' ')[1])) for move in moves]

      D = {
            'U': (0, -1),
            'R': (1, 0),
            'D': (0, 1),
            'L': (-1, 0)
      }

      def rope_visited(length):
            rope = [(0, 0)] * length
            visited = {(0, 0)}

            def distance(a, b):
                  return abs(a[0] - b[0]), abs(a[1] - b[1])

            def adjust_tail(H, T):
                  dis = distance(H, T)
                  if (dis[0] > 1 or dis[1] > 1):
                        if (dis[0] > 0):
                              T = (T[0] + (1 if T[0] < H[0] else -1), T[1])
                        if (dis[1] > 0):
                              T = (T[0], T[1] + (1 if T[1] < H[1] else -1))
                  return T

            for dir, n in moves:
                  for i in range(n):
                        rope[0] = rope[0][0] + D[dir][0], rope[0][1] + D[dir][1]
                        print('H:', rope[0])
                        for j in range (1, len(rope)):
                              rope[j] = adjust_tail(rope[j-1], rope[j])
                        print(rope[-1])
                        visited.add(rope[-1])

            return len(visited)
            
with open('output', 'w') as output:
      output.write( str(rope_visited(2)) + '\n' + str(rope_visited(10)) +'\n')