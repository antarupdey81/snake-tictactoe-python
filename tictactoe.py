"""
Classic Tic-Tac-Toe in Python (Terminal Interactive)
Run with: python tictactoe.py
"""

def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board, player):
    win_coords = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_coords)

def check_tie(board):
    return all(cell in ['X', 'O'] for cell in board)

def play_game():
    board = [str(i + 1) for i in range(9)]
    current_player = "X"

    print("=== Welcome to Tic-Tac-Toe! ===")
    print("Enter cell numbers (1-9) to make your move.")

    while True:
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, choose a spot (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] in ['X', 'O']:
                print("Invalid move! Spot already taken or out of range. Try again.")
                continue
        except ValueError:
            print("Please enter a valid number between 1 and 9.")
            continue

        board[move] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        if check_tie(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
