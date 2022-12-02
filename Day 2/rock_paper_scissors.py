play_sum     = 0
strategy_sum = 0

with open('input') as input:
      text = input.read()
      rounds = text.split('\n')[:-1]
      rounds = [tuple(round.split(' ')) for round in rounds]

      for round in rounds:
            opponent, player = ord(round[0]) - ord('A'), ord(round[1]) - ord('X')

            #COLUMN DICTATES ROCK PAPER OR SCISSORS
            play_sum += player + 1
            if player == opponent:
                  play_sum += 3
            elif (opponent + 1) % 3 == player:
                  play_sum += 6
            else:
                  pass

            #COLUMN DICTATES LOSE TIE OR WIN
            if player == 0:
                  strategy_sum += ((opponent + 2) % 3) + 1
            elif player == 1:
                  strategy_sum += 3 + (opponent + 1)
            else:
                  strategy_sum += 6 + ((opponent + 1) % 3) + 1
                  
with open('output', 'w') as output:
      output.write(str(play_sum)+'\n'+str(strategy_sum)+'\n')