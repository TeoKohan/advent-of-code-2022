primes = [2, 3, 5, 7, 11, 13, 17, 19]

class Player:
      scared = False

class Value:
      def __init__(self, value):
            self.value = value
            self.modulo = { p: value % p for p in primes }

      def modify(self, f):
            if not Player.scared:
                  self.value = f(self.value)
            else:
                  for p in self.modulo:
                        self.modulo[p] = f(self.modulo[p]) % p

class Monkey:
      def __init__(self, values, operation, test):
            self.values = [Value(value) for value in values]
            self.operation = operation
            self.test = test
            self.nerves = False
            self.count = 0

      def link(self, true, false):
            self.true  = true
            self.false = false

      def inspect(self):
            for value in self.values:
                  self.count += 1
                  value.modify(self.operation)
                  if not Player.scared:
                        value.modify(lambda x: x//3)
                  (self.true if (value.value % self.test == 0 if not Player.scared else value.modulo[self.test] == 0) else self.false).values += [value]
            self.values = []

def solve(rounds):
      monkeys = [
            Monkey([57],                             lambda x: x * 13, 11),
            Monkey([58, 93, 88, 81, 72, 73, 65],     lambda x: x + 2 ,  7),
            Monkey([65, 95],                         lambda x: x + 6 , 13),
            Monkey([58, 80, 81, 83],                 lambda x: x * x ,  5),
            Monkey([58, 89, 90, 96, 55],             lambda x: x + 3 ,  3),
            Monkey([66, 73, 87, 58, 62, 67],         lambda x: x * 7 , 17),
            Monkey([85, 55, 89],                     lambda x: x + 4 ,  2),
            Monkey([73, 80, 54, 94, 90, 52, 69, 58], lambda x: x + 7 , 19)
      ]

      monkeys[0].link(monkeys[3], monkeys[2])
      monkeys[1].link(monkeys[6], monkeys[7])
      monkeys[2].link(monkeys[3], monkeys[5])
      monkeys[3].link(monkeys[4], monkeys[5])
      monkeys[4].link(monkeys[1], monkeys[7])
      monkeys[5].link(monkeys[4], monkeys[1])
      monkeys[6].link(monkeys[2], monkeys[0])
      monkeys[7].link(monkeys[6], monkeys[0])

      for round in range(rounds):
            for monkey in monkeys:
                  monkey.inspect()
      monkey_levels = sorted([monkey.count for monkey in monkeys])
      return monkey_levels[-1] * monkey_levels[-2]

with open('output', 'w') as output:
      output.write(str(solve(20)) + '\n')
      Player.scared = True
      output.write(str(solve(10000)) +'\n')