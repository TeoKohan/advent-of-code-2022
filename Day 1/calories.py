values = []
with open('input') as input:
      text = input.read()
      elves = text.split('\n\n')
      elves = [list(map(lambda x : int(x) if x.isnumeric() else 0, elf.split('\n'))) for elf in elves]
      elves = [sum(calories) for calories in elves]
      for total in elves:
            values += [total]
            values = sorted(values)[-3:]
with open('output', 'w') as output:
      output.write(str(values[-1])+'\n'+str(sum(values))+'\n')