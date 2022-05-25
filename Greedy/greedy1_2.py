# 거스름돈 | 예제
'''
주어진 돈이 N, 거스름돈: 500원, 100원, 50원, 10
거슬러줘야할 동전의 최소개수
'''
n = int(input())
result = 0 # 동전의 개수
if n >= 500:
  result += n // 500
  n = n - (n // 500) * 500
if n >= 100:
  result += n // 100
  n = n - (n // 100) * 100
if n >= 50:
  result += n // 50
  n = n - (n // 50) * 50
if n >= 10:
  result += n // 10

print(result)

# 답안예시_______________________

n = int(input())
result = 0
coins = [500, 100, 50, 10]
for coin in coins:
  result += n // coin
  n %= coin # n -= (n // coin) * coin