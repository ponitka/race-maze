import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from player import Player
from game import GameWindow
from maze import Maze

maze = Maze(41, 53) # must be odd

player1 = Player("player1")
player2 = Player("player2")

player1.pos_i, player1.pos_j = maze.starting_height, 0
player2.met_i, player2.met_j = maze.starting_height, 0

player2.pos_i, player2.pos_j = maze.starting_height, maze.width - 1
player1.met_i, player1.met_j = maze.starting_height, maze.width - 1

game = GameWindow(maze, [player1, player2])
def elo(abc):
  player1.is_game_running = False
  player2.is_game_running = False
  Gtk.main_quit()
game.connect("destroy", elo)
game.show_all()
Gtk.main()
