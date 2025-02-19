def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def is_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def has_full_board(board):
    return all(col != " " for row in board for col in row)


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    print("Tic-Tac-Toe Game")
    print_board(board)
    for t in range(9):
        player = players[t % 2]
        while 1:
            try:
                row, col = map(int, input(f"P {player}, row col (0-2): ").split())
                if board[row][col] == " ":
                    board[row][col] = player
                    break
                else:
                    print("Nope. Again.")
            except:
                print("Wrong. 0-2 pls.")
        print_board(board)
        if is_winner(board, player):
            print(f"P {player} wins!")
            return
        if has_full_board(board):
            print("Draw!")
            return
    print("Draw!")


tic_tac_toe()
