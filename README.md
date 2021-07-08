# RabbitGame

</br> Upon running the game with:
python rabbit_game.py

You will be prompted for 3 integers in turn, the number of rows, columns and holes.

Then the game will start.

Controls:

Pressing number h from 0 to H-1:
Will 'start controlling' hole h

Arrow Keys: will move the current controlled hole according to the arrow keys: the new space must keep the same parity as the old space

Enter: Given the current configuration of Holes, will make a move.

Delete: Will go back to how the game was before the most recent move.

Escape/CTRL+C: Will quit the game.

Grid: 'X' represents where the rabbit could be
      ' ' represents where the rabbit cannot be
      'h' represents the position of hole h currently (h is an integer 0 <= h < H 
