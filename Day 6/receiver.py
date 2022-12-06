with open('input') as input:
      text = input.read()

      def different(n):
            for i in range(n, len(text)):
                  substring = text[i-n:i]
                  D = { }
                  for char in substring:
                        if char in D.keys():
                              D[char] += 1
                        else:
                              D[char] = 1
                  if len(D.keys()) >= n:
                        return i

with open('output', 'w') as output:
      output.write( str(different(4)) + '\n' + str(different(14)) +'\n')