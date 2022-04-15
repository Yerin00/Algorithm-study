# 퇴사 | 삼성전자 SW 역량테스트 | 난이도 ★★
'''
n+1일후에 퇴사예정이다. 퇴사 전까지 얻을수 있는 최대 이익을 계산하라.
1일부터 n일까지 주어진 업무마다의 걸리는 시간과 보상이 입력으로 들어온다.

'''
## 내 답안_______________________
# n = int(input())
# t = []
# p = []
# for i in range(n):
#   time, price = map(int, input().split())
#   t.append(time)
#   p.append(price)

# dp = [0] * n
# for i in range(1, n):
#   temp = [] # i를 돌때마다 초기화
#   dp[i] = dp[i - 1] # 전날 값으로 초기화
#   for j in range(0, i + 1): # i+1함으로써 i자신도 포함시킴(t=1인경우)
#     k = j + t[j] - 1 # j인덱스 + 걸리는 시간 - 1
#     if i == k: # 현재 위치에 완료되는 상담인가
#       temp.append(max(dp[i],dp[k-1] + p[k])) # k? k-1?
#   if temp: # empty list가 아니면
#     dp[i] = max(temp) # t가 1인경우 dp[k]가 자기자신이기 때문에 반복문을 돌며 dp[i]를 변경시키면 해당값에 영향을 미치므로 temp 리스트에 모두 저장한 후 반복문을 빠져나온 다음에 max로 최댓값을 뽑아 넣어주었다.

# print(dp[n - 1])

## 답안예시_________________________________________________
n = int(input())
t = []
p = []
dp = [0] * (n + 1)
max_value = 0

for i in range(n):
  x, y = map(int, input().split())
  t.append(x)
  p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
  time = t[i] + i
  # 상담이 기간안에 끝나는 경우
  if time <= n:
    #점화식에 맞게, 현재까지의 최고 이익 계산
    dp[i] = max(p[i] + dp[time], max_value)
    max_value = dp[i]
  # 상담이 기간을 벗어나는 경우
  else:
    dp[i] = max_value

print(max_value)