# 부품 찾기 | 난이도 1.5 | 실전문제
'''
리스트에 값이 있으면 yes, 없으면 no를 반환
'''

n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
request = list(map(int, input().split()))

## 방법 1. 재귀함수_______________________
def binary_search(array, target, start, end):
  if start > end:
    return "no"
  mid = (start + end) // 2
  if array[mid] == target:
    return "yes"
  elif array[mid] > target:
    return binary_search(array, target, start, mid - 1) # ★ 리턴을 해줘야한다고..?
  else:
    return binary_search(array, target, mid + 1, end)
    
for i in range(m):
  print(binary_search(array, request[i], 0, n-1))
  
## 방법 2. 계수정렬_______________________

## 방법 3. 집합_______________________
