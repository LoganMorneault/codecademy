# CodeCademy's 12th lesson in the Python 2 course. This is a pretty bare-bones implementation of Battleship
# The board is set to a fixed 5x5 and a single 1x1 ship is placed randomly within it. Players have 4 turns to guess the ship's location correctly.
# Again, very basic changes, although I may come back to this.

from random import randint

# board is a 2d list
board = []

# fills board with O's, which will be printed
for x in range(5):
  board.append(["O"] * 5)

# function for printing board
def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

# selects a random row to place the ship in
def random_row(board):
  return randint(0, len(board) - 1)

# selects a random column to place the ship in
def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board) # note: because the board is square in this implementation, you could just use random_row again

# For cheating
# print ship_row
# print ship_col

# Gameplay loop
for turn in range(4):

  # user input
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

# If guess is good
  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
    break

  else:
    # if guess is out of bounds
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print "Oops, that's not even in the ocean."

    # if guess is duplicate
    elif(board[guess_row][guess_col] == "X"):
      print "You guessed that one already."

    # general miss
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"

    # Print (turn + 1) here!
    if turn == 3:
      print "Game Over"
      break # Not sure why this wasn't included in the original
    print "Turn ", (turn + 1)
    print_board(board)
