# 순차탐색 sequential search
# 7-1.py 순차 탐색 소스코드
def sequential_search(n, target, array):
  for i in range(n):
    if array[i] == target:
      return i + 1

print("생성할 원소의 갯수, 찾을 문자열:")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("원소의 개수만큼 문자열을 입력")
array = input().split()

print(sequential_search(n, target, array))