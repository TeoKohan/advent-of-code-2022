with open('input') as input:
      text = input.read()
      instructions = text.split('\n')[:-1]

      CRT = [[' '] * 40 for i in range(6)]

      def draw_to_monitor(cycle, X):
            print(cycle)
            row    = cycle // 40
            column = cycle %  40
            CRT[row][column] = '#' if abs(column - X) <= 1 else '.'

      cycle = 1
      X = 1
      buffer = [0, 0]

      signal_strength = [0]

      for I in instructions:
            if I == 'noop':
                  V = None
            else:
                  print(I)
                  V = int(I.split(' ')[1])
            signal_strength += [cycle * X]
            cycle += 1
            draw_to_monitor(cycle - 2, X)
            if V != None:
                  signal_strength += [cycle * X]
                  cycle += 1
                  draw_to_monitor(cycle - 2, X)
                  X += V

      print(signal_strength[20], signal_strength[60], signal_strength[100], signal_strength[140], signal_strength[180], signal_strength[220])
      print(sum([signal_strength[20], signal_strength[60], signal_strength[100], signal_strength[140], signal_strength[180], signal_strength[220]]))

      CRT = [''.join(line) for line in CRT]   
      for line in CRT:
            print(line)
#with open('output', 'w') as output:
#      output.write( str(rope_visited(2)) + '\n' + str(rope_visited(10)) +'\n')