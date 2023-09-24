import random

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join([f"{i * 3 + j + 1}" if cell == " " else cell for j, cell in enumerate(row)]))
        if i < 2:
            print("-" * 9)

def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def computer_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]

    # Randomly decide who starts
    current_player = random.choice(["X", "O"])

    while True:
        print_board(board)
        print(f"Current player: {current_player}")

        if current_player == "X":
            try:
                move = int(input("Enter position (1-9): "))
                if move < 1 or move > 9:
                    print("Invalid input. Position must be between 1 and 9.")
                    continue
                row, col = divmod(move - 1, 3)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
        else:
            row, col = computer_move(board)

        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Invalid move. Try again.")
            continue

        if is_winner(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "X" if current_player == "O" else "O"

if __name__ == "__main__":
    main()
