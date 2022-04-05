# 공유기 설치 | 난이도 ★★
'''
★떡볶이 떡 만들기와 비슷한 파라메트릭 유형 문제
집의 위치가 주어지고 집에 공유기를 설치한다.
가장 인접한 두 공유기 사이 거리의 최댓값을 출력하라

입력: 집의 수, 공유기 수, 집의 위치
'''
# 데이터 입력받기
import sys # ★sys.stdin.readline으로 입력받지않으면 시간초과남
f = sys.stdin.readline
n, c = map(int, f().split())
array = []
for _ in range(n):
  array.append(int(f()))
array.sort()

## 내 답안________________________________________________________
'''
gap을 이진탐색한다 (힌트)
이진탐색을 계속 할수록 최적의 값이 나올 것이다.
'''

## 답안예시1. ____________________________________________________와 어렵다. 답지보고도 헷갈렸다.
start = 1 # 가능한 최소 거리
end = array[-1] - array[0] # 가능한 최대 거리 ※array[-1]은 마지막 요소의 값을 뜻함
result = 0

while start <= end:
  mid = (start + end) // 2 # mid는 가장 인접한 두 공유기 사이의 거리를 의미
  value = array[0]
  count = 1
  # mid 값을 이용해 공유기 설치
  for i in range(1, n):
    if array[i] >= value + mid:
      value = array[i]
      count += 1
  if count >= c: # c개 이상의 공유기를 설치할 수 있는 경우 거리를 증가시킴
    start = mid + 1
    result = mid # 최적의 결과 저장
  else: # c개 이상의 공유기를 설치할 수 없는 경우 거리를 감소시킴
    end = mid - 1

print(result)