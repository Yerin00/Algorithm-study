# 삽입 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
  for j in range(i, 0, -1): # i부터 1까지 감소하며 반복
    if array[j] < array[j-1]: # 한칸씩 왼쪽으로 이동, 왼쪽원소보다 자기가 더 작으면
      array[j], array[j-1] = array[j-1], array[j] # 왼쪽 원소와 스와프
    else: # 자기가 더 크거나 같으면 
      break

print(array)