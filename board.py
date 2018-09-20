import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from square import Square

class Board(Gtk.Box):
  
  def __init__(self, maze, players, window):
    Gtk.Box.__init__(self, orientation = Gtk.Orientation.VERTICAL)

    self.maze = maze

    self.array = []
    for i in range(maze.height):
      self.array.append([])
      for j in range(maze.width):
        self.array[i].append(Square(i, j, window))

    self.array[players[0].pos_i][players[0].pos_j].set_property("is_player_%s" % players[0].name, True)
    self.array[players[1].pos_i][players[1].pos_j].set_property("is_player_%s" % players[1].name, True)

    for i in range(maze.height):
      box = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)
      for j in range(maze.width):
        box.pack_start(self.array[i][j], True, True, 0)
      self.pack_start(box, True, True, 0)

    for i in range(maze.height):
      for j in range(maze.width):
        if maze[i][j] == 1:
          self.array[i][j].set_property("state", True)
        else:
          self.array[i][j].set_property("state", False)

  def move(self, direction, Player):
    if Player.move_allowed == False:
      return False
    
    if direction == "Up":
      d = [-1, 0]
    if direction == "Down":
      d = [+1, 0]
    if direction == "Right":
      d = [0, +1]
    if direction == "Left":
      d = [0, -1]

    if self.maze.inside(Player.pos_i + d[0], Player.pos_j + d[1]) == False:
      return False
    if self.array[Player.pos_i + d[0]][Player.pos_j + d[1]].get_property("state") == True:
      return False
    if (Player.pos_i + d[0]) % 2 == 0 and (Player.pos_j + d[1]) % 2 == 0:
      return False

    self.array[Player.pos_i][Player.pos_j].set_property("is_player_%s" % Player.name, False)
    self.array[Player.pos_i + d[0]][Player.pos_j + d[1]].set_property("is_player_%s" % Player.name, True)

    Player.pos_i += d[0]
    Player.pos_j += d[1]
    if (Player.pos_i, Player.pos_j) == (Player.met_i, Player.met_j):
      Player.win()
  
    return True
