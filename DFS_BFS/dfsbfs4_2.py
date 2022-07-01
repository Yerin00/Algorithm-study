# 연구소
'''
0 빈칸, 1 벽, 2 바이러스
바이러스는 네 방향으로 모두 옮길수있음
벽 3개를 세워서 안전지역을 최대로 만들고 안전지역의 최대 칸수를 출력하라.

N x M 크기의 지도, (3 <= N, M <= 8)
'''
from collections import deque
from itertools import combinations
import copy

# 안전 영역의 개수 세는 함수
def safeZone(graph):
  count = 0
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        count += 1

  return count

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
  q = deque()
  q.append((x, y))
  while q:
    x, y = q.popleft()
    graph[x][y] = 2
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx and nx < n and 0 <= ny and ny < m and graph[x][y] == 0:
        q.append((nx, ny))
   
n, m = map(int, input().split())
graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))
graph_copy = copy.deepcopy(graph)


empty = []
virus = []
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      empty.append((i, j))
    elif graph[i][j] == 2:
      virus.append((i, j))

result = 1e9
all_cases = list(combinations(empty, 3))
for cases in all_cases:
  for x, y in cases:
    graph[x][y] = 1 # 벽 세우기
  for x, y in virus: # 모든 바이러스에서 바이러스 퍼뜨리기
    bfs(x, y)
  result = max(result, safeZone(graph)) # 안전지역의 개수 세기
  graph = copy.deepcopy(graph_copy) # 그래프 초기화
    
print(result)
