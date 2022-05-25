# 1이 될 때까지 | 2018 E 기업 알고리즘 대회 | 난이도 ★
'''
어떠한 수 N이 1이 될 때까ㅣㅈ 다음의 두 과정 중 하나를 반복적으로 선택
1. N에서 1을 뺀다.
2. N을 K로 나눈다.

1번 혹은 2번의 과정을 수행해야하는 횟수의 최솟값을 출력한다.
'''

#________________________

n, k = map(int, input().split())
result = 0

while n >= k:
  while n % k != 0:
    n -= 1
    result += 1
  n //= k
  result += 1

while n > 1:
  n -= 1
  result += 1

print(result)

#__________________________________

n, k = map(int, input().split())
result = 0

while True:
  # 나누어떨어질때까지 1씩 빼기
  target = (n // k) * k
  result += (n - target)
  n = target
  # 안 나눠질때 break
  if n < k:
    break
  result += 1
  n //= k

# 1씩 빼기
result += (n - 1)
print(result)