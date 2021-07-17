board = [[]*10 for _ in range(10)]

for i in range(10):
  board[i]= list (map(int, input().split()))

xs = 1
ys = 1

board[xs][ys] = 9

while True:
  if(board[xs][ys]==2):
    board[xs][ys] = 9
    break
  if(board[xs][ys+1]!=1):
    board[xs][ys] = 9
    ys += 1
  else:
    if(board[xs+1][ys] != 1):
      board[xs][ys] = 9
      xs += 1
    else:
      board[xs][ys]=9
      break
for i in range(10):
  for j in range(10):
    print(board[i][j], end =' ')
  print()





