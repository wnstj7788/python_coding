#N 입력 받기

n = int(input())

x,y = 1,1

moving =  input().split()

#이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_type = ['L','R','U','D']

#이동확인
for move in moving:
  #이동 후 좌표
  for i in range(len(move_type)):
    if move == move_type[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  # 벗어나는 공간 무시 
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  x,y = nx , ny   
print(x,y)
