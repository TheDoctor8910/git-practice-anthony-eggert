def print_board(board):
    """
    Prints the board in a Tic-Tac-Toe grid.
    :param board: The game board
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def is_winner(board, player):
    """
    Checks if the current player has 3 spaces in a line on the board.
    :param board: The game board
    :param player: The current player
    :return: True if the player has three spaces in a line, False otherwise
    """
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def has_full_board(board):
    """
    Checks if all spaces on the board are full.
    :param board: The game board
    :return: True if there are no available spaces left, False otherwise
    """
    return all(col != " " for row in board for col in row)


def tic_tac_toe():
    """
    Plays a full game of Tic-Tac-Toe.
    """
    board, players = init_game()
    print("Tic-Tac-Toe Game")
    print_board(board)
    for turn in range(9):
        player = players[turn % 2]
        play_turn(board, player)
        print_board(board)
        if is_winner(board, player):
            print(f"P {player} wins!")
            return
        if has_full_board(board):
            print("Draw!")
            return
    print("Draw!")


def init_game():
    """
    Generates the initial board and player array
    :return: A 3x3 array representing each space on the board and an array containing the player symbols
    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    return board, players


def play_turn(board, player):
    """
    Handles user input for a single turn.
    :param board: The game board for recording player action
    :param player: The current player
    """
    while 1:
        try:
            row, col = map(int, input(f"P {player}, row col (0-2): ").split())
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("Nope. Again.")
        except ValueError:
            print("2 numbers pls.")
        except IndexError:
            print("Wrong. 0-2 pls.")


tic_tac_toe()
