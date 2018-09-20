import random

class Maze:
  
  def __init__(self, height, width):
    self.height = height
    self.width = width
    self.array = [[0 for i in range(self.width)] for j in range(self.height)]

    self.starting_height = self.height // 2
    if self.starting_height % 2 == 0:
      self.starting_height += 1

    self.borders = []

    for i in range(self.width):
      if (i != 0 and i != self.width-1) or 0 != self.starting_height:
        self.array[0][i] = 1
        if self.type(0, i) == "square":
          self.borders.append([0, i])
      if (i != 0 and i != self.width-1) or self.height-1 != self.starting_height:
        self.array[self.height-1][i] = 1
        if self.type(self.height-1, i) == "square":
          self.borders.append([self.height-1, i])

    for i in range(self.height):
      if i != self.starting_height:
        self.array[i][0] = 1
        self.array[i][self.width-1] = 1
        if self.type(i, 0) == "square":
          self.borders.append([i, 0])
        if self.type(i, self.width-1) == "square":
          self.borders.append([i, self.width-1])

    for i in range(self.height):
      for j in range(self.width):
        if self.type(i,j) == "square":
          self.array[i][j] = 1   

    self.visited = [[0 for i in range(self.width)] for j in range(self.height)]
    for bo in self.borders:
      self.visited[bo[0]][bo[1]] = 1

    random.shuffle(self.borders)
    for bo in self.borders:
      self.dfs(bo, False)

    rest = []
    for i in range(self.height):
      for j in range(self.width):
        if self.type(i, j) == "square":
          if self.visited[i][j] == False:
            rest.append([i, j])
    random.shuffle(rest)
    for pos in rest:
      self.dfs(pos, False)
  
  def dfs(self, pos, stop):
    self.visited[pos[0]][pos[1]] = 1

    if stop == True and random.randint(1, 3 * max(self.height, self.width)) == 1:
      return

    ds = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    random.shuffle(ds)
    for d in ds:
     if self.inside(pos[0] + 2*d[0], pos[1] + 2*d[1]):
        if not self.visited[pos[0] + 2*d[0]][pos[1] + 2*d[1]]:
          self.array[pos[0] + d[0]][pos[1] + d[1]] = 1    
          self.dfs([pos[0] + 2*d[0], pos[1] + 2*d[1]], True)
          if stop == True:
            return
          
  def inside(self, i, j):
    if 0 > i or i >= self.height:
      return False
    if 0 > j or j >= self.width:
      return False
    return True

  def type(self, i, j):
    if i % 2 == 0 and j % 2 == 0:
      return "square"
    if i % 2 == 1 and j % 2 == 0:
      return "vertical"
    if i % 2 == 0 and j % 2 == 1:
      return "horizontal"
    return "empty"

  def __getitem__(self, i):
    return self.array[i]
