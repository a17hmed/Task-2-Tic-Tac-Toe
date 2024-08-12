# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oenIBuVpbyKt_L1YHOMw5XXox3rxmBrX
"""

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows, columns, and diagonals
    lines = [board[i] for i in range(3)] + \
            [[board[j][i] for j in range(3)] for i in range(3)] + \
            [[board[i][i] for i in range(3)]] + \
            [[board[i][2-i] for i in range(3)]]

    for line in lines:
        if line.count(line[0]) == 3 and line[0] != " ":
            return line[0]
    if any(cell == " " for row in board for cell in row):
        return None
    return "Draw"

def minimax(board, depth, is_maximizing):
    scores = {'X': 10, 'O': -10, 'Draw': 0}
    winner = check_winner(board)
    if winner:
        return scores[winner]

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -float('inf')
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = 'X'
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter column (0, 1, 2): "))
        if board[row][col] == " ":
            board[row][col] = 'O'
        else:
            print("Cell already taken! Try again.")
            continue

        if check_winner(board):
            print_board(board)
            print(f"Game Over! {check_winner(board)} wins!")
            break

        move = best_move(board)
        if move != (-1, -1):
            board[move[0]][move[1]] = 'X'
        else:
            print("It's a draw!")
            break

        print_board(board)
        if check_winner(board):
            print(f"Game Over! {check_winner(board)} wins!")
            break

play_game()