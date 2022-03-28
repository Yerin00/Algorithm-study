# 퀵 정렬
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# 파이썬의 장점을 이용한 퀵정렬
'''
효율성 측면에서는 원래의 퀵정렬보다 안좋지만 코드가 간결하고 기억하기쉽다.
'''
def quick_sort(array):
  if len(array) <= 1:
    return array
  pivot = array[0]
  tail = array[1:]

  left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
  right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

  return quick_sort(left_side) + [pivot] + quick_sort(right_side)