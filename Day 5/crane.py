import re

with open('input') as input:

      text = input.read()
      crates, moves = text.split('\n\n')

      crates = crates.split('\n')
      crates = list(reversed(crates))
      numbers, crates = crates[0], crates[1:]
      stack_locations = [i for i in range(len(numbers)) if numbers[i].isnumeric()]

      stacks = ['']*9
      for i, line in [(i, line) for i in range(len(stack_locations)) for line in crates]:
            stacks[i] += line[stack_locations[i]] if line[stack_locations[i]] != ' ' else ''

      cratemover_9000, cratemover_9001 = stacks[::], stacks[::]
      
      moves = moves[:-1].split('\n')
      moves = [list(map(int, re.findall(r'\b\d+\b', move))) for move in moves]
      
      for n, a, b in moves:
            a = a - 1
            b = b - 1
            c = cratemover_9000[a][-n:][::-1]
            cratemover_9000[a] = cratemover_9000[a][:-n]
            cratemover_9000[b] = cratemover_9000[b] + c

      cratemover_9000 = ''.join([stack[-1] for stack in cratemover_9000])

      for n, a, b in moves:
            a = a - 1
            b = b - 1
            c = cratemover_9001[a][-n:]
            cratemover_9001[a] = cratemover_9001[a][:-n]
            cratemover_9001[b] = cratemover_9001[b] + c

      cratemover_9001 = ''.join([stack[-1] for stack in cratemover_9001])

with open('output', 'w') as output:
      output.write(cratemover_9000 +'\n' + cratemover_9001 +'\n')