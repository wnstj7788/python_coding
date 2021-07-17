# 나눠서 입력 받기
n,m,k = map(int, input().split())

# 데이터를 리스트로 저장
date= list(map(int,input().split()))

# 오름차순 정렬
date.sort()

#가장 큰 수 2개를 추림 
one_big = date[n-1]
two_bing = date[n-2]
#
sum = 0
# m에 맞게 더한 후 2번 쨰로 큰 값을 더해줌 
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

  
  
  