<h2>Description</h2>
<p>
  Piway's Game of Life is a <a href="https://www.raspberrypi.org/">Raspberry Pi</a>-developed cellular automaton <a href="https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life">Conway's Game of Life</a>-style game made in <a href="https://www.python.org/">Python</a> using <a href="https://www.pygame.org/">pygame</a>. Therefore, graphics and visual resources are at their minimum, extracting the most performance from the computer.
</p>
<h2>Play</h2>

```bash
# clone the game's repository
$ git clone https://github.com/ojpbarbosa/piway.git

# cd into the game's directory
$ cd piway

# create the game's virtual environment
$ python -m venv --prompt piway .venv

# activate the game's virtual environment
$ source ./.venv/bin/activate
# or
$ ./.venv/Scripts/activate.bat

# install the game's required libraries
$ pip install -r requirements.txt

# launch the game
$ python ./piway/main.py
```

<h2>Stack</h2>
<ul>
  <li><a href="https://www.python.org/">Python</a></li>
  <li><a href="https://www.pygame.org/">pygame</a></li>
</ul>

<h2>References</h2>
<ul>
  <li><a href="https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life">Conway's Game of Life</a></li>
  <li><a href="https://www.raspberrypi.org/">Raspberry Pi</a></li>
</ul>

<h2>Resources</h2>
<ul>
  <li><a href="http://www.superluigibros.com/downloads/fonts/emulogic_font.zip">Emulogic Font</a> by <a href="http://www.superluigibros.com/">Super Luigi Bros</a>
</ul>
