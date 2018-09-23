# race-maze
Race in the maze game implemented in Python 3 using GTK+ library with graphics made by myself.  <br />

Game is designed for two players. Board is a randomly generated maze. Goal of each player is to reach the starting position of his enemy faster than him (those positions are holes in the outer wall of the maze).

Game rules and controls:
<ul>
  <li>Use WASD to move a red (X) player.</li>
  <li>Use arrows to move a green (O) player.</li>
  <li>Players can occupy the same square at the same time.</li>
</ul>

To start the game run <code>main.py</code> in Python 3 (<code>$ python3 main.py</code>)

To install GTK+ on Ubuntu execute: <br />
<code>$ sudo apt install python-gi python-gi-cairo python3-gi python3-gi-cairo gir1.2-gtk-3.0</code>. <br />
For other platforms follow the instructions from https://pygobject.readthedocs.io/en/latest/getting_started.html.
