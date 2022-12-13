total_sum = 0

class File:
      def __init__(self, size):
            self.size = size

class Directory:
      def __init__(self, parent):
            self.parent   = parent
            self.children = {}
            self.size     = 0
      
      def walk(self, name):
            if name not in self.children.keys():
                 self.children[name] = Directory(self)
            return self.children[name]

      def add_file(self, size, name):
            self.children[name] = File(int(size))

      def calculate_size(self):
            for child in self.children.values():
                  if type(child) is Directory:
                        child.calculate_size()
                  self.size += child.size

with open('input') as input:
      text = input.read()
      commands = text.split('$ ')[1:]
      commands = [command.split('\n')[:-1] for command in commands]
      commands = [command[1:] if command[0] == 'ls' else command[0].split(' ')[1] for command in commands]
      
      root = Directory(None)
      current = root
      for command in commands[1:]:
            if type(command) is list:
                  for file in command:
                        if file.split(' ')[0] != 'dir':
                              current.add_file(*file.split(' '))
            else:
                  current = current.walk(command) if command != '..' else current.parent
      root.calculate_size()
      
      def get_small_files(D):
            total_size = D.size if D.size <= 100000 else 0
            for child in D.children.values():
                  if type(child) is Directory:
                        total_size += get_small_files(child)
            return total_size

      required_space = 30000000 - (70000000 - root.size)
      def get_smallest_file(D):
            smallest = D.size if D.size >= required_space else 70000000
            for child in D.children.values():
                  if type(child) is Directory:
                        smallest = min(smallest, get_smallest_file(child))
            return smallest

with open('output', 'w') as output:
      output.write( str(get_small_files(root)) + '\n' + str(get_smallest_file(root)) +'\n')