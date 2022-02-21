# 1이 될 때 까지
## 답안 예시2.
n, k = map(int, input().split())
result = 0

while True:
  # -1 빼기
  target = (n // k) * k
  result += (n - target)
  n = target

  # n이 k보다 작으면 빠져나오기
  if n < k:
    break

  result += 1
  n //= k

result += (n - 1)
print(result)


## 내 답안______________________________________
# 단순하지만 반복문을 많이 돌게됨, 반복문 한번에 연산 한번.
# n, k = map(int, input().split())
# result = 0
# while n != 1:
#   if n % k == 0:
#     n = n / k
#     result += 1
#   else:
#     n = n - 1
#     result += 1

# print(result)