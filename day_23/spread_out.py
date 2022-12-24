import re
from enum import Enum
from collections import Counter

class V2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, v):
        return type(v) is V2 and self.x == v.x and self.y == v.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, B):
        return V2(self.x + B.x, self.y + B.y)

    def distance(A, B):
        return abs(A.x - B.x) + abs(A.y - B.y)

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __iter__(self):
        yield self.x
        yield self.y

class Proposition:
    propositions = [[V2(-1, -1), V2(-1, 0), V2(-1, 1)], [V2(1, -1), V2(1, 0), V2(1, 1)], [V2(-1, -1), V2(0, -1), V2(1, -1)], [V2(-1, 1), V2(0, 1), V2(1, 1)]]
    def cycle():
        Proposition.propositions = [Proposition.propositions[1], Proposition.propositions[2], Proposition.propositions[3], Proposition.propositions[0]]

free_space = 0
settled    = 0
with open('input') as input:
    lines = input.read()[:-1]
    lines = lines.split('\n')
    elves = { V2(i, j) for i in range(len(lines)) for j in range(len(lines[i])) if lines[i][j] == '#' }

    def print_elves(elves):
        min_x, max_x = min([elf.x for elf in elves]), max([elf.x for elf in elves])
        min_y, max_y = min([elf.y for elf in elves]), max([elf.y for elf in elves])
        for x in range(min_x, max_x + 1):
            print(''.join(['#' if V2(x, y) in elves else '.' for y in range(min_y, max_y + 1)]))

    def simulate_round(elves):
        proposals = { }
        for elf in elves:
            proposals[elf] = None
            if all([elf + V2(i, j) not in elves for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0)]):
                continue
            for proposition in Proposition.propositions:
                if all([elf + direction not in elves for direction in proposition]):
                    proposals[elf] = proposition[1] 
                    break
        end_points = Counter([elf + proposals[elf] for elf in elves if proposals[elf] != None])
        Proposition.cycle()
        return { elf + proposals[elf] if proposals[elf] != None and end_points[elf + proposals[elf]] <= 1 else elf for elf in elves }

    for round in range(1, 11):
        elves = simulate_round(elves)
    min_x, max_x = min([elf.x for elf in elves]), max([elf.x for elf in elves])
    min_y, max_y = min([elf.y for elf in elves]), max([elf.y for elf in elves])
    free_space = (max_x - min_x + 1) * (max_y - min_y + 1) - len(elves)

    while True:
        E = simulate_round(elves)
        round += 1
        if elves == E:
            break
        elves = E
    settled = round

with open('output', 'w') as output:
    output.write(str(free_space) + '\n')
    output.write(str(settled) + '\n')