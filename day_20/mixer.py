class Chain:
      def __init__(self, list):
            self.start = None
            self.end   = None
            self.len   = 0
            for n in list:
                  self.push_back(n)
      
      def __iter__(self):
            n = self.start
            for _ in range(self.len):
                  yield n
                  n = n.next

      def __getitem__(self, key):
            return self.start.walk(key)

      def __repr__(self):
            return '[' + ', '.join([str(n) for n in self]) + ']'

      def push_back(self, n):
            n = Number(n)
            self.start = n if self.start == None else self.start
            self.end   = n if self.end   == None else self.end

            self.end.next = n
            n.previous = self.end
            n.next = self.start
            self.start.previous = n

            self.end = n
            self.len += 1

      def find_first_index(self, key):
            for i in range(self.len):
                  if self[i].value == key:
                        return i
            return None

      def pop(self, n):
            if n is self.start:
                  self.start = n.next
            self.len -= 1
            return n.pop()

      def insert_after(self, p, n):
            p.insert(n)
            self.len += 1
            
class Number:
      def __init__(self, value):
            self.previous = None
            self.value    = value
            self.next     = None

      def __repr__(self):
            return str(self.value)

      def walk(self, value):
            node = self
            while value != 0:
                  if value > 0:
                        node = node.next
                        value -= 1
                  if value < 0:
                        node = node.previous
                        value += 1
            return node

      def pop(self):
            self.previous.next = self.next
            self.next.previous = self.previous
            return self.value

      def insert(self, value):
            value.previous = self
            value.next = self.next
            self.next.previous = value
            self.next = value

simple_decode = 0
complex_decode = 0
with open('input') as input:
      numbers = input.read()[:-1]
      numbers = numbers.split('\n')
      numbers = [int(n) for n in numbers]

      simple_mix  = Chain(numbers)
      simple_order = [n for n in simple_mix]

      complex_mix = Chain(numbers)
      complex_order = [n for n in complex_mix]

      def mix(order, numbers):
            for n in order:
                  v = numbers.pop(n) 
                  v = (abs(v) % (len(order) - 1)) * (1 if v > 0 else -1)
                  node = n.walk(v - (0 if v > 0 else 1))
                  numbers.insert_after(node, n)
      
      def decode(numbers):
            z = numbers.find_first_index(0)
            return numbers[z+1000].value + numbers[z+2000].value + numbers[z+3000].value

      mix(simple_order, simple_mix)
      simple_decode = decode(simple_mix)

      decryption_key = 811589153

      for n in complex_order:
            n.value *= decryption_key
      for i in range(10):
            mix(complex_order, complex_mix)
            print(f'{i+1}/10')
      complex_decode = decode(complex_mix)

with open('output', 'w') as output:
      output.write(str(simple_decode) + '\n')
      output.write(str(complex_decode) + '\n')