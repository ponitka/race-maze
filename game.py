import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from board import Board
from sidebar import Sidebar

class GameWindow(Gtk.Window):

  def __init__(self, maze, players):
    Gtk.Window.__init__(self, title = "Maze")
    self.set_border_width(20)
    
    self.players = players

    self.box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 20)
    self.add(self.box)
  
    self.sidebar = Sidebar(self.players)
    self.box.pack_start(self.sidebar, True, True, 0)

    self.board = Board(maze, self.players, self)
    self.box.pack_start(self.board, True, True, 0)

    self.connect("key-press-event", self.press)

  def press(self, widget, event):
    keyval = event.keyval
    keyval_name = Gdk.keyval_name(keyval)
    state = event.state

    if keyval_name == "w":
      self.board.move("Up", self.players[0])
    if keyval_name == "a":
      self.board.move("Left", self.players[0])
    if keyval_name == "s":
      self.board.move("Down", self.players[0])
    if keyval_name == "d":
      self.board.move("Right", self.players[0])

    if keyval_name in ["Up", "Down", "Left", "Right"]:
      self.board.move(keyval_name, self.players[1])
