# 카드 정렬하기 | 핵심유형 | 난이도 ★★
'''
각각 A, B장인 카드 묶음을 합쳐서 하나로 만들기위해서는 A + B 번의 비교를 해야한다.
N개의 묶음과 각 카드 묶음의 크기가 주어지면 최소 비교횟수를 출력하라
'''
## 답안예시___________________________________________우선순위 큐 사용
import heapq
n = int(input())

heap = []
for i in range(n):
  data = int(input())
  heapq.heappush(heap, data)

result = 0

# 원소가 1개 남을때까지
while len(heap) != 1:
  # 가장 작은 2개의 카드 묶음 꺼내기
  one = heapq.heappop(heap)
  two = heapq.heappop(heap)

  sum_value = one + two
  result += sum_value
  heapq.heappush(heap, sum_value)

print(result)

  



## 내 답안(오답)_____________________________계속 정렬하면서 항상 제일 작은거 두개를 가져와야함ㅇㅇ
# n = int(input())
# data = []
# for _ in range(n):
#   data.append(int(input()))

# # 오름차순 정렬
# data.sort()

# temp = 0
# sum = 0 # 최소 비교횟수
# # 비교횟수 구하기
# for i in range(len(data)):
#   temp = temp + data[i]
#   if i == 0:
#     continue
#   sum += temp

# print(sum)

  