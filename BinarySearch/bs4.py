# 고정점 찾기
'''
고정점: 인덱스 == 값
최대 1개
없으면 print -1
'''
n = int(input())
array = list(map(int, input().split()))

start = 0
end = n -1
while start <= end:
  mid = (start + end) // 2
  if array[mid] == mid : # 고정점이면 고정점 출력
    print("고정점: ", mid)
    break
  elif array[mid] < mid: # 인덱스의 값이 더 크면 오른쪽 탐색
    start = mid + 1
  else: # 인덱스 값이 더 작으면 왼쪽 탐색
    end = mid - 1
if start > end:
  print(-1)
    