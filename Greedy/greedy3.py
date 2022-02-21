# 숫자 카드

## 내 답안___________________________________________________
n, m = map(int, input().split())
min_v = []
result = 0

for i in range(n):
  # 전체 카드를 저장하는게 아니고 3개씩(한 행)덮어써짐.
  data = list(map(int, input().split()))
  min_v.append(min(data))


result = max(min_v) # 최솟값 리스트 중에서 최댓값을 뽑아냄.

print("최종 선택 카드: ", result)


## 답안 예시1. min()함수 이용_________________________________
# n, m = map(int, input().split())

# result = 0
# for i in range(n):
#   data = list(map(int, input().split()))
#   min_v = min(data)
#   result = max(result, min_v)
  
# print("최종 선택 카드: ", result)


## 답안 예시2. 2중 반복문______________________________________

