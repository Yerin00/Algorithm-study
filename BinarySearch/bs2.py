# 떡볶이 | 난이도 ★★ | 실전문제
'''
떡의 개수, 요청한 떡의 길이
각각 떡의 개별길이

적어도 M만큼의 떡을 가져가려면 절단기 높이를 어떻게 설정해야할까
'''
## 내 오답...
n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

start = 0
end = n - 1
result = array[n - 1]

while start >= end:
  mid = (start + end) // 2
  if array[mid]:
    start = mid - 1
  else:

  for i in range(mid, end + 1):
    if array[i] >= result:
      sum += array[i] - result
  # 자른떡이 요구한 m보다 크거나 같으면 절단기 길이 return
  if sum >= m:
    return result
  else:
    result -= 1


print(result)

## 답안예시_____________________
'''
- 정렬이 안되어있는데 어떻게 이진탐색을 하는거지?
- 이진탐색을 사용하지않으면 시간초과남

- 중간점 값이 절단기의 길이가 됨.
떡들을 이진탐색하는게 아니라 절단기의 길이가 대상이 됨.
'''
n, m = map(int, input().split())
array = list(map(int, input().split()))
# 절단기 적절 높이를 찾기 위한 범위 설정
start = 0
end = max(array)
# 절단기 높이 갱신할 변수
result = 0
while start <= end:
  # 손님이 가져갈 떡의 길이 계산할 변수
  dduk = 0
  mid = (start + end) // 2
  for x in array:
    if x > mid:
      dduk += (x - mid)
  if dduk < m:
    end = mid - 1
  else:
    result = mid
    start = mid + 1

print(result)


