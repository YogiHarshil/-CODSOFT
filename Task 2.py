import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, is_maximizing):
    scores = {'X': 1, 'O': -1, 'Tie': 0}
    
    if is_winner(board, 'X'):
        return scores['X'] - depth
    elif is_winner(board, 'O'):
        return scores['O'] + depth
    elif is_board_full(board):
        return scores['Tie']
    
    empty_cells = get_empty_cells(board)
    if is_maximizing:
        max_eval = float('-inf')
        for cell in empty_cells:
            board[cell[0]][cell[1]] = 'X'
            eval = minimax(board, depth + 1, False)
            board[cell[0]][cell[1]] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for cell in empty_cells:
            board[cell[0]][cell[1]] = 'O'
            eval = minimax(board, depth + 1, True)
            board[cell[0]][cell[1]] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    best_val = float('-inf')
    best_move = None
    empty_cells = get_empty_cells(board)
    
    for cell in empty_cells:
        board[cell[0]][cell[1]] = 'X'
        move_val = minimax(board, 0, False)
        board[cell[0]][cell[1]] = ' '
        
        if move_val > best_val:
            best_move = cell
            best_val = move_val
    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    
    while True:
        print_board(board)
        user_row, user_col = map(int, input("Enter row and column (1, 2, or 3) separated by a space: ").split())
        user_row -= 1
        user_col -= 1
        if board[user_row][user_col] != ' ':
            print("Cell already occupied. Try again.")
            continue
        board[user_row][user_col] = 'O'
        
        if is_winner(board, 'O'):
            print_board(board)
            print("You win! Congratulations!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        print("Computer's turn:")
        computer_row, computer_col = get_best_move(board)
        board[computer_row][computer_col] = 'X'
        
        if is_winner(board, 'X'):
            print_board(board)
            print("Computer wins! Better luck next time.")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
