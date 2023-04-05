board =  [[' ', 0, 1, 2],
          [0, '-', '-', '-'],
          [1, '-', '-', '-'],
          [2, '-', '-', '-']]

def draw_board():
    print('-------------')
    for row in board:
        for cols in row:
            print(cols, end=' ')
        print()

def make_move(user):
    print('Enter x and y coordinate')

    x = int(input(f'User {user}, enter row number: '))
    y = int(input(f'User {user}, enter cols number: '))

    #for value in '012':
    #    if x!=value or y!=value:
    #       print('there is no such cell, please re-enter, 0<=x<=2 and 0<=y<=2')
    #      x = int(input(f'User {user}, enter new row number: '))
    #        y = int(input(f'User {user}, enter new cols number: '))
    #   else:
    #        board[x+1][y+1] = user
    board[x + 1][y + 1] = user

def check_win():
    for i in range(1, 4):
        if board[i][1] == board[i][2] == board[i][3] != '-':
            return board[i][1]

    for j in range(1, 4):
        if board[1][j] == board[2][j] == board[3][j] != '-':
            return board[1][j]

    if board[1][1] == board[2][2] == board[3][3] != '-' or \
       board[1][3] == board[2][2] == board[3][1] != '-':
        return board[2][2]
    return None

def play_game():
    for turn in range(10):
        player = 'X' if turn % 2 == 0 else 'O'
        draw_board()
        make_move(player)
        winner = check_win()
        if winner:
            print(f'Player {winner} wins!')
            break
    else:
        print('Draw!')

play_game()