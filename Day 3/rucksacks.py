priority_sum = 0
group_sum    = 0

with open('input') as input:
      text = input.read()
      sacks = text.split('\n')[:-1]
      split = [tuple([sack[:len(sack) // 2], sack[len(sack) // 2:]]) for sack in sacks]

      def priority(item):
            return ord(item) - ord('A') + 27 if ord(item) <= ord('Z') else ord(item) - ord('a') + 1

      for A, B in split:
            D = { chr(key) : False for key in list(range(ord('A'), ord('Z') + 1)) + list(range(ord('a'), ord('z') + 1)) }

            for item in A:
                  D[item] = True
            for item in B:
                  if D[item] == True:
                        priority_sum += priority(item)
                        break
      
      for i in range(0, len(sacks), 3):
            D = { chr(key) : 0 for key in list(range(ord('A'), ord('Z') + 1)) + list(range(ord('a'), ord('z') + 1)) }

            A = sacks[i+0]
            B = sacks[i+1]
            C = sacks[i+2]

            for item in A:
                  D[item] = 1
            for item in B:
                  D[item] = 2 if D[item] >= 1 else 0
            for item in C:
                  if D[item] == 2:
                        group_sum += priority(item)
                        break

with open('output', 'w') as output:
      output.write(str(priority_sum)+'\n' + str(group_sum)+'\n')