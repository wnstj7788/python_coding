"""
거스름돈으로 500,100,50,10을사용 할 수 있고 동전은 무한히 존재한다고 가정한다.
손님에게 거슬러 줘야 할 돈이 n원일 때 거슬러 워야할 동전의 최소 개수를 구하라
"""
n = 1260

count = 0

coin_types = [500,100,50,10]

for coin in coin_types:
  count += n //coin  #해당화폐로 거슬러 줄 수 있는 동전 수 
  n %= coin 

print(count)
 