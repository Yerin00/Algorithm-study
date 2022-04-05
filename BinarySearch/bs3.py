# 정렬된 배열에서 특정 수의 개수 구하기
n, x = map(int, input().split())
array = list(map(int, input().split()))

## 내 답안_____________________________________________
# x의 시작 인덱스
def first_x(array, x, start, end):
  mid = (start + end) // 2
  if start > end:
    return None
  if array[mid] == x:
    '''
    ★x가 몇개 있을지 모르기때문에 비효율적인 방법.. 이진탐색으로 한번 찾는다고해서 끝이 아니다. 첫번째 인덱스가 나올때까지 이진탐색햐야한다. 고로 별로 안좋은 코드
      '''
    i = mid
    while array[i] == x:

      # 한칸씩 앞으로 이동하면서 첫 x의 인덱스를 찾는다.
      i -= 1
      if i <= 0:
        break
    return i + 1 # 인덱스 반환
  elif array[mid] > x:
    return first_x(array, x, start, mid - 1)
  else:
    return first_x(array, x, mid + 1, end)

# x의 끝 인덱스
def last_x(array, x, start, end):
  mid = (start + end) // 2
  if start > end:
    return None
  if array[mid] == x:
    i = mid
    while array[i] == x:
      # 한칸씩 앞으로 이동하면서 첫 x의 인덱스를 찾는다.
      i += 1
      if i >= n:
        break
    return i - 1
  elif array[mid] > x:
    return last_x(array, x, start, mid - 1)
  else:
    return last_x(array, x, mid + 1, end)

# 재귀함수 실행-> 값이 x인 시작과 끝 인덱스 찾기
first_index = first_x(array, x, 0, n - 1)
if first_index != None:
  last_index = last_x(array, x, 0, n - 1)
  result = last_index - first_index + 1
  print("x의 등장 횟수:",result)
else:
  print(-1)
    
## 답안예시1. 정석적인 방법______________________________________________________
# 값이 x인 원소의 개수를 세는 메서드
def count_by_value(array, x):
  n = len(array)

  a = first_x(array, x, 0, n - 1)
  if a == None:
    return 0
  b = last_x(array, x, 0, n - 1)

  return b - a + 1
  
# x의 시작 인덱스
def first_x(array, x, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  if (mid == 0 or x > array[mid - 1]) and array[mid] == x:
    return mid
  elif array[mid] >= x: # x값을 찾아도 첫번째가 아니면 또 이진탐색을 함
    return first_x(array, x, start, mid - 1)
  else:
    return first_x(array, x, mid + 1, end)

# x의 끝 인덱스
def last_x(array, x, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  if (mid == n - 1 or x < array[mid + 1])and array[mid] == x:
    return mid
  elif array[mid] > x:
    return last_x(array, x, start, mid - 1)
  else:
    return last_x(array, x, mid + 1, end)

# 실행
count = count_by_value(array, x)
if count == 0: # 값이x인 원소가 존재하지않는다면
  print(-1)
else:
  print(count)

## 답안예시2. bisect : O(logN) ★____________________________
from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
  right_index = bisect_right(array, right_value)
  left_index = bisect_left(array, left_value)
  return right_index - left_index

count = count_by_range(array, x, x)

if count == 0:
  print(-1)
else:
  print(count)