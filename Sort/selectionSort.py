# 선택정렬
'''
항상 가장 작은 것을 찾아 맨 앞으로 보내는 정렬 방법.
시간 복잡도 O(N^2)
'''

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(array)):
  min_index = i
  for j in range(i+1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  # 파이썬은 스와프 코드가 존재해서 간단하게 리스트의 원소 위치를 바꿀수있다. 
  array[i], array[min_index] = array[min_index], array[i]

print(array)