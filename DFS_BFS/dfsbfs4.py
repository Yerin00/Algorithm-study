# 연구소
'''
0 빈칸, 1 벽, 2 바이러스
바이러스는 네 방향으로 모두 옮길수있음
벽 3개를 세워서 안전지역을 최대로 만들고 안전지역의 최대 칸수를 출력하라.
'''
# from itertools import combinations

# n, m = map(int, input().split())
# graph = []

# # NxM 맵 입력받기
# for i in range(n):
#   graph.append(list(map(int, input().split())))

# 예제
# empty = []
# virus = []
# n, m =7, 7
# graph = [
#   [2, 0, 0, 0, 1, 1, 0],
#   [0, 0, 1, 0, 1, 2, 0],
#   [0, 1, 1, 0, 1, 0, 0],
#   [0, 1, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 1, 1],
#   [0, 1, 0, 0, 0, 0, 0],
#   [0, 1, 0, 0, 0, 0, 0]
# ]

# for i in range(n):
#   for j in range(m):
#     if graph[i][j] == 0:
#       empty.append((i, j))
#     elif graph[i][j] == 2:
#       virus.append((i, j))

# print(empty)
# print(virus)

# def dfs(x, y):
#   # 범위를 벗어나면
#   if x <= -1 or x >= n or y <= -1 or y >= m:
#     return False
#   # 벽이면
#   if graph[x][y] == 1:
#     return False
#   # 빈칸이면 바이러스 옮기기
#   if graph[x][y] == 0:
#     graph[x][y] = 2

#   '''
#   아.. 근데 바이러스를 옮긴다음 다시 되돌리는 코드도 있어야하는구나
#   그렇다하더라도 무한반복은 좀..? 어디서 나오는거야 대체...
#   '''
#   dfs(x+1, y)
#   dfs(x, y+1)
#   dfs(x-1, y)
#   dfs(x, y-1)
#   return True
  
  
# # 안전 지역 수의 최댓값  
# max = 0
      
# # 빈칸 중에서 3개의 조합을 뽑아냄
# empty_comb = list(combinations(empty, 3))

# 3개의 벽을 세울 수 있는 모든 경우의 수에 대해서
# [((1,2),(4,5),(8,2)),(),()]
# for comb in empty_comb:
#   # 안전 지역의 수 초기화
#   count = 0
#   # 벽세우기
#   for a, b in comb:
#     graph[a][b] = 1

#   # 값이 2인 지점(바이러스)에서부터 바이러스 전파
#   for x, y in virus:
#     dfs(x, y)
#   # 안전지역 count
#   for i in range(n):
#     for j in range(m):
#       if graph[i][j] == 0:
#         count += 1
#   if count > max:
#     max = count
#   # 벽 초기화
#   for a, b in comb:
#     graph[a][b] = 0


# # 안전 지역의 수
# print(max)

## 답안예시_______________________________________________
n, m = map(int, input().split())
data = []
temp = [[0] * m for _ in range(n)] # 벽 설취한 뒤 맵 리스트

for _ in range(n):
  data.append(list(map(int, input().split())))

# 4가지 이동방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# DFS로 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 0 and nx < n and ny >= 0 and ny < m:
      if temp[nx][ny] == 0:
        temp[nx][ny] = 2
        virus(nx, ny)

def get_score():
  score = 0
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        score += 1
  return score

# 울타리 설치하면서 매번 안전영역 크기 계산
def dfs(count):
  global result
  # 울타리가 3개 설치된 경우
  if count == 3:
    for i in range(n):
      for j in range(m):
        temp[i][j] = data[i][j]

    # 각 바이러스 위치에서 전파 진행
    for i in range(n):
      for j in range(m):
        if temp[i][j] == 2:
          virus(i, j)
    # 안전 영역의 최댓값 계산
    # result = max(result, get_score())
    value = get_score()
    if result < value:
      result = value
      for i in range(n):
        for j in range(m):
          print(temp[i][j], " ".join)
        print()
    return

  # 빈 공간에 울타리 설치
  for i in range(n):
    for j in range(m):
      if data[i][j] == 0:
        data[i][j] = 1
        count += 1
        dfs(count)
        # 초기화
        data[i][j] = 0
        count -= 1

dfs(0)
print(result)

  