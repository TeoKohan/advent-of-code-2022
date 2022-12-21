O = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

class Monkey:
    def __init__(self, v):
        self.value = (lambda x: v) if type(v) is int else None
        if self.value == None:
            self.a, self.operation, self.b = v
            self.operation = O[self.operation]
    
    def get_value(self, monkeys):
        if self.value == None:
            self.value = lambda x: self.operation(monkeys[self.a].get_value(monkeys)(x), monkeys[self.b].get_value(monkeys)(x))
        return self.value

root_value = 0
human_value = 0
with open('input') as input:
    monkeys = input.read()[:-1]
    monkeys = monkeys.split('\n')
    monkeys = [monkey.split(': ') for monkey in monkeys]
    for monkey in monkeys:
        monkey[1] = Monkey(int(monkey[1])) if monkey[1].isnumeric() else Monkey(monkey[1].split(' '))
    simple_monkeys = {name: value for name, value in monkeys}
    complex_monkeys = {name: value for name, value in monkeys}

    root_value = round(simple_monkeys['root'].get_value(simple_monkeys)(0))

    complex_monkeys['humn'].value = lambda x: x

    A = complex_monkeys['root'].a
    B = complex_monkeys['root'].b
    position = 0
    speed    = 0
    accel    = 1
    distance = abs(complex_monkeys[A].get_value(complex_monkeys)(position) - complex_monkeys[B].get_value(complex_monkeys)(position))
    while distance > 0.01:
        speed    += accel
        position += speed
        D = abs(complex_monkeys[A].get_value(complex_monkeys)(position) - complex_monkeys[B].get_value(complex_monkeys)(position))
        if D <= distance:
            accel *= 1.1
        else:
            speed *= -0.5
            accel *= -0.5
        distance = D
    human_value = round(position)
    
with open('output', 'w') as output:
      output.write(str(root_value) + '\n')
      output.write(str(human_value) + '\n')