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
    if (x<0 or x>2) or (y<0 or y>2):
        while True:
            print('Enter new value!')
            x = int(input(f'User {user}, enter row number: '))
            y = int(input(f'User {user}, enter cols number: '))
            if 0<=x<=2 and 0<=y<=2:
                break
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