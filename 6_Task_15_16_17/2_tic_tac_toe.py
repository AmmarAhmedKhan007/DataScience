
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_still_going = True

# Who is the winner
winner = None
# Tells us who the current player is (X goes first)
current_player = "X"

def play_game():

  # Show game board
  display_board()

  # Loop until the game stops (winner or tie)
  while game_still_going:

    handle_turn(current_player)
    check_if_game_over()
    flip_player()
  
  # Since the game is over, print the winner or tie
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")


# Display the game board on screen
def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")


# Handle a turn for an arbitrary player
def handle_turn(player):

  # Get position from player
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  valid = False
  while not valid:

    # Make sure the input is valid
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
 
    # Get correct index in our board list
    position = int(position) - 1

    # Make sure the spot is available on the board
    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")

  # Put game piece on the board
  board[position] = player

  # Show game board
  display_board()
# Check if the game is over
def check_if_game_over():
  check_for_winner()
  check_for_tie()

# Check if somebody has won
def check_for_winner():
  global winner
  # Check if there was a winner anywhere
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None

# Check the rows for a win
def check_rows():
  global game_still_going
  # Check if any of the rows have all the same value (not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  if row_1:
    return board[0] 
  elif row_2:
    return board[3] 
  elif row_3:
    return board[6] 
  else:
    return None

# Check columns for win
def check_columns():
  global game_still_going
  # Check if any of the columns have all the same value (not empty)
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False
  if column_1:
    return board[0] 
  elif column_2:
    return board[1] 
  elif column_3:
    return board[2] 
  else:
    return None

# Check the diagonals for a win
def check_diagonals():
  # Set global variables
  global game_still_going
  # Check if any of the columns have all the same value (not empty)
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  # If any row does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False
  if diagonal_1:
    return board[0] 
  elif diagonal_2:
    return board[2]
  else:
    return None

# Check if there is a tie
def check_for_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False
    return True
  else:
    return False

# Flip the current player from X to O, or O to X
def flip_player():
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"

play_game()