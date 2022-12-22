import re
from collections import deque

class Room:
      def __init__(self, name, flow, tunnels):
            self.name = name
            self.flow = flow
            self.tunnels = tunnels

      def __repr__(self):
            return str(self.flow) + ', ' + str(self.tunnels)

max_pressure_elephant = 0
with open('input') as input:
      text = input.read()[:-1]
      rooms = text.split('\n')
      rooms = { re.findall(r'[A-Z]+', room)[1]: Room(re.findall(r'[A-Z]+', room)[1], int(re.search(r'\d+', room).group(0)), re.findall(r'[A-Z]+', room)[2:]) for room in rooms }

      def BFS(start):
            class Node:
                  def __init__(self, room):
                        self.name    = room
                        self.visited = False
                        self.path    = []
                        self.tunnels = rooms[room].tunnels

            nodes = {room: Node(room) for room in rooms}
            nodes[start].visited = True
            travel = deque([nodes[start]])

            while len(travel) > 0:
                  current = travel.popleft()
                  for room in current.tunnels:
                        if nodes[room].visited == False:
                              nodes[room].path = current.path + [nodes[room].name]
                              nodes[room].visited = True
                              travel += [nodes[room]]

            return {k: v.path for k, v in nodes.items()}

      valves = [room.name for room in rooms.values() if room.flow > 0]
      map    = {room: BFS(room) for room in ['AA'] + valves}

      def solve(room, time, closed, flow, total_flow):

            solution = total_flow + flow * time
            if time == 0 or closed == []:
                  return solution
            for destination in closed:
                  distance = len(map[room][destination])
                  time_taken = distance + 1
                  if time_taken <= time:
                        solution = max(solution, solve(destination, time - time_taken, [d for d in closed if d != destination], flow + rooms[destination].flow, total_flow + flow * time_taken))
            return solution

      max_pressure_elephant = solve('AA', 30, valves[:], 0, 0)
                        
with open('output', 'w') as output:
      output.write(str(max_pressure_elephant) + '\n')