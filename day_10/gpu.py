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
                  V = int(I.split(' ')[1])
            signal_strength += [cycle * X]
            cycle += 1
            draw_to_monitor(cycle - 2, X)
            if V != None:
                  signal_strength += [cycle * X]
                  cycle += 1
                  draw_to_monitor(cycle - 2, X)
                  X += V

with open('output', 'w') as output:
      output.write( str(sum([signal_strength[20], signal_strength[60], signal_strength[100], signal_strength[140], signal_strength[180], signal_strength[220]])) + '\n')
      for line in CRT:
            output.write(''.join(line) + '\n')