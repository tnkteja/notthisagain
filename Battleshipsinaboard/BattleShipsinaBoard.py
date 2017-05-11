if len(board) == 0: return 0
count = 0
for i,row in enumerate(board):
    for j,col in enumerate(row):
        if col == 'X' and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):
            count += 1
print count