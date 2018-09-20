import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, GdkPixbuf, GLib, Gdk

import sys
import array

class Square(Gtk.Box):

  state = GObject.Property(type = bool, default = False)
  is_player_player1 = GObject.Property(type = bool, default = False)
  is_player_player2 = GObject.Property(type = bool, default = False)

  def __init__(self, i, j, window):
    Gtk.Box.__init__(self)

    self.connect("notify::state", self.update)
    self.connect("notify::is-player-player1", self.update)
    self.connect("notify::is-player-player2", self.update)
    
    self.i = i
    self.j = j
  
    self.default_image = "images/empty.png"
    self.player1_image = "images/player1.png"
    self.player2_image = "images/player2.png"
    self.player12_image = "images/player12.png"

    self.pixbuf = GdkPixbuf.Pixbuf.new_from_file(self.default_image)
    self.image = Gtk.Image.new_from_pixbuf(self.pixbuf)
    self.pack_start(self.image, True, True, 0)
    self.image.connect('size-allocate', self.update)

    if i % 2 == 0 and j % 2 == 0:
      self.active_image = "images/square.png"
    if i % 2 == 0 and j % 2 == 1:
      self.active_image = "images/horizontal.png"
    if i % 2 == 1 and j % 2 == 0:
      self.active_image = "images/vertical.png"
    if i % 2 == 1 and j % 2 == 1:
      self.active_image = "images/empty.png"

  def update(self, obj, gparamstring):
    if self.get_property("is_player_player1") == True:
      if self.get_property("is_player_player2") == True:
        path = self.player12_image
      else:
        path = self.player1_image
    else:
      if self.get_property("is_player_player2") == True:
        path = self.player2_image
      else:
        if self.get_property("state") == True:
          path = self.active_image
        else:
          path = self.default_image

    allocation = self.get_allocation()
    self.pixbuf = GdkPixbuf.Pixbuf.new_from_file(path)
    self.pixbuf = self.pixbuf.scale_simple(max(15, allocation.width), max(15, allocation.height), GdkPixbuf.InterpType.HYPER)
    self.image.set_from_pixbuf(self.pixbuf)
