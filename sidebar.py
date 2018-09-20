import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

import threading
import calendar
import time

class Sidebar(Gtk.Box):

  def __init__(self, players):
    
    Gtk.Box.__init__(self, orientation = Gtk.Orientation.HORIZONTAL)

    self.players = players

    self.timer1 = Gtk.Label()
    self.timer2 = Gtk.Label()
    self.info = Gtk.Label()

    self.pack_start(self.timer1, True, True, 0)
    self.pack_start(self.info, True, True, 0)
    self.pack_start(self.timer2, True, True, 0)

    self.info.set_label("Maze")

    self.beg_time = time.time()

    GObject.timeout_add(10, self.update)

  def update(self):
    if self.players[0].is_game_running == False:
      return False

    Time = time.time()

    if self.players[0].move_allowed == True:
      self.timer1.set_label( "Player X: %.2f" % (Time - self.beg_time) )
    if self.players[1].move_allowed == True:
      self.timer2.set_label( "Player O: %.2f" % (Time - self.beg_time) )

    return True
