# 못생긴 수 | 난이도 1.5 | Google 인터뷰
'''
n번째 못생긴 수를 찾는 프로그램을 작성하세요.
2,3,5만을 소인수로 갖는 수.
1은 못생긴 수라고 가정한다.
'''
## 내 답안_______________________________________
n = int(input())
dp = [0] * (n + 1) # 못생긴 수를 담을 리스트
dp[1] = 1

for i in range(2, n + 1): # 2~n까지
  min_value = 1e9
  for j in range(1, n):
    # 이전값보다는 크면서 min인 값을 넣는다.
    if dp[j] * 2 > dp[i - 1]:
      mul_2 = dp[j] * 2
    else:
      mul_2 = 1e9
    if dp[j] * 3 > dp[i - 1]:
      mul_3 = dp[j] * 3
    else:
      mul_3 = 1e9
    if dp[j] * 5 > dp[i - 1]:
      mul_5 = dp[j] * 5
    else:
      mul_5 = 1e9
      
    min_value = min(min_value, mul_2, mul_3, mul_5)
  dp[i] = min_value

print(dp[n])

## 답안예시_________________________________________________
n = int(intput())

ugly = [0] * n
ugly[0] = 1

# 2,3,5배를 위한 인덱스
i2 = i3 = i5 = 0
# 처음에 곱셈값을 초기화
next2, next3, next5 = 2, 3, 5

'''
 ugly = [1, 2, 3, ]
 next2, next3, next5 = 4, 6, 5

'''
for l in range(1, n):
  ugly[l] = min(next2, next3, next5)
  if ugly[l] == next2:
    i2 += 1
    next2 = ugly[i2] * 2
  if ugly[l] == next3:
    i3 += 1
    next3 = ugly[i3] * 3
  if ugly[l] == next5:
    i5 += 1
    next5 = ugly[i5] * 5

print(ugly[n - 1])
    