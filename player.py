import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

class Player:

  move_allowed = True

  def __init__(self, name):
    self.name = name

    self.is_game_running = True

    self.pos_i, self.pos_j = 0, 0
    self.met_i, self.met_j = 0, 0

  def win(self):
    self.move_allowed = False
