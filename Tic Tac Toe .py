#!/usr/bin/env python
# coding: utf-8

# Tic Tac Toe game

# In[1]:


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all(square == player for square in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_tie(board):
    return all(all(square != "" for square in row) for row in board)

def main():
    board = [["" for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)
        player = players[current_player]
        print(f"Player {player}'s turn")

        while True:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == "":
                break
            else:
                print("Invalid move. Try again.")

        board[row][col] = player

        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 1 - current_player

if __name__ == "__main__":
    main()


# In[ ]:




