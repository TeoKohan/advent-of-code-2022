full_overlap = 0
partial_overlap = 0

with open('input') as input:
      text = input.read()
      pairs = text.split('\n')[:-1]
      pairs = [pair.split(',') for pair in pairs]
      pairs = [(list(map(int, x.split('-'))), list(map(int, y.split('-')))) for x, y in pairs]
      for (a, b), (x, y) in pairs:
            if a >= x and b <= y or x >= a and y <= b:
                  full_overlap += 1
            if a <= y and b >= x or x <= b and y >= a:
                  partial_overlap += 1
with open('output', 'w') as output:
      output.write(str(full_overlap)+'\n' + str(partial_overlap)+'\n')