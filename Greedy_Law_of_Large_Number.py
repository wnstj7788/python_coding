# 나눠서 입력 받기
n,m,k = map(int, input().split())

date= list(map(int,input().split()))

date.sort()

one_big = date[n-1]
two_bing = date[n-2]

sum = 0

while True:
  for i in range(k):
    if m == 0 :
      break
    sum += one_big
    m -=1
  if m == 0:
    break
  sum += two_bing
  m -= 1
print(sum)

  
  
  