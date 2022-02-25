# 볼링공 고르기 | 2019 SW 마에스트로 입학 테스트 | 난이도★(쉬움)
n, m = map(int, input().split())
data = list(map(int, input().split()))

## 내 답안.

# result = 0
# for i in data:
#   for j in data:
#     if i != j:
#       result += 1

# result = result // 2 # 순서는 상관없음. 조합이기 때문에 중복되는 경우의 수를 제거하기위해 2로 나눠줌.
# print(result)

## 답안예시1.
# 이중 for문이 없이 풀기

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
  array[x] += 1

result = 0
for i in range(1, m+1):
  n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
  result += array[i] * n # B가 선택하는 경우의 수와 곱하기

print(result)