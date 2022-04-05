# 이진 탐색 binarySearch
## 7-2.py 재귀함수로 구현한 이진 탐색 소스코드
def binary_search(array, target, start, end):
  if start > end: # ★ 찾으려는 원소가 없는 경우
    return None
  mid = (start + end) // 2 # 소수점 버림
  if target == array[mid]:
    return mid
  elif target < array[mid]: # 중간값보다 작으면
    binary_search(array, target, start, mid - 1)
  else:
    binary_search(array, target, mid + 1, end)

## 7-3.py 반복문으로 구현한 이진 탐색 소스코드
'''
while array[mid] == target: 을 조건으로 두면, 찾으려는 원소가 없는 경우 무한반복을 돌게된다. 그러므로 종료 조건으로 start와 end가 교차하는 것을 두는게 요점이다.
'''
def binary_search2(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] < target:
      start = mid + 1
    else:
      end = mid - 1
  return None


## 값 입력받고 함수 실행하기    
# 원소의 개수, 찾고자하는 target
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print(result + 1) # 인덱스 번호 + 1


## 빠르게 입력받기
## 7-4.py 한 줄 입력받아 출력하는 소스코드
import sys
input_data = sys.stdin.readline().rstrip()

print(input_data)

  