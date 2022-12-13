with open('input') as input:
      text = input.read()
      grid = text.split('\n')[:-1]
      grid = [[int(n) for n in line] for line in grid]

      n = len(grid)

      visible = [[False] * n for i in range(n)]
      Directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

      visible_trees = 0
      for i in range(n):
            height = [0, 0, 0, 0]
            for j in range(n):
                  k = n-1-j
                  visible[i][j] |= grid[i][j] >= height[0]
                  height[0]      = max(height[0], grid[i][j] + 1)
                  visible[j][i] |= grid[j][i] >= height[1]
                  height[1]      = max(height[1], grid[j][i] + 1)
                  visible[i][k] |= grid[i][k] >= height[2]
                  height[2]      = max(height[2], grid[i][k] + 1)
                  visible[k][i] |= grid[k][i] >= height[3]
                  height[3]      = max(height[3], grid[k][i] + 1)

      visible_trees = sum([sum([1 if v else 0 for v in line]) for line in visible])

      def walk(position, direction, height):
            i, j = position
            x, y = direction
            i, j = i + x, j + y
            if i < 0 or i >= n or j < 0 or j >= n:
                  return 0
            elif grid[i][j] >= height:
                  return 1
            else:
                  return 1 + walk((i, j), direction, height)

      max_scenic_score = 0
      for (i, j) in [(i, j) for i in range(n) for j in range(n)]:
            scenic_score = 1
            for dir in Directions:
                  scenic_score *= walk((i, j), dir, grid[i][j])
            max_scenic_score = max(max_scenic_score, scenic_score)
            
with open('output', 'w') as output:
      output.write( str(visible_trees) + '\n' + str(max_scenic_score) +'\n')