## Rock Paper Scissors

A simple command-line Rock Paper Scissors game written in Python. You play one round against the computer, which picks its move at random.

### Requirements
Python 3.6 or newer (uses f-strings)
No external dependencies
How to run
bash
python main.py

Replace main.py with the name of your script file if it differs.

### How to play
Run the script.
Type rock, paper or scissors when prompted (case-insensitive).
The game prints both choices and the result.
Example
Pick a rock, paper scissor: rock
You: rock
CPU: scissor
Win
Rules
Your move	Beats
rock	scissors
paper	rock
scissors	paper
Same choice as the CPU: Draw
Your move beats the CPU's: Win
Otherwise: Lose

Any input other than the three valid choices prints Invalid and the game ends.
