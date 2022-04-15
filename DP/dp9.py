# 병사 배치하기 | 핵심유형 | 난이도 1.5
'''
- N명의 병사가 무작위로 나열됨. 전투력 높은 병사가 앞에 오도록 내림차순 배치하고자 함.
- 특정 위치의 병사는 열외 시켜서 병사 번호 이동 없이 자연히 내림차순이 되도록 해야함. 앞쪽에 있는 병사의 전투력이 항상 뒤쪽에 있는 병시보다 높아야한다.
- 동시에 남아있는 병사의 수가 최대가 되도록 하고싶다.
'''
## 답안예시_______________________________________________________
'''
가장 긴 증가하는 부분 수열(LIS) 알고리즘을 그대로 적용하면 풀 수 있다.
'''
n = int(input())
array = list(map(int, input().split()))
array.reverse()

dp = [1] * n
for i in range(1, n):
  for j in range(0, i):
    if array[j] < array[i]: # 오름차순이면 dp값을 증가시키면서 부분 수열을 이어간다. 오름차순이 아니면 그 값은 1 그대로 남겨두고 다음 값으로 넘어간다.
      dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))


## dp가 아닌방법으로도 풀리지않나 싶었는데 아니었다ㅎ____________________
# n = int(input())
# array = list(map(int, input().split()))
# count = 0

# i = 1
# while (i + count) < n:
#   if array[i] <= array[i - 1]:
#     i += 1
#     continue
#   else:
#     # i가 i - 2에 있는 값보다 작으면 i - 1을 빼는게 유리하다. 왜냐면 i가 i-1보다 크니까 뒤에 나오는 수들을 더 많이 포함할수있다.
#     if array[i] <= array[i - 2]:
#       array.remove(array[i - 1])
#       count += 1
#     else:
#       array.remove(array[i])
#       count += 1

# print(count)