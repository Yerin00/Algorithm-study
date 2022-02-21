# 거스름돈
## 답안 예시1.
n = 1260
count = 0

coin_types = [500, 100, 50, 10]  # 값이 큰 순서대로 리스트 생성
for coin in coin_types:
    count += n // coin
    n %= coin

print(count)
