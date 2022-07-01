# 미로 탈출 | 실전문제 | 난이도★1.5
from collections import deque
## 오답노트
n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 정의
def bfs(graph, x, y, visited):
  queue = deque((x, y)) # 시작 위치 삽입
  visited[x][y] = True # 첫번째 방문처리
  result = 0 # 이동거리
  # queue가 빌때까지
  while queue:
    # pop
    x, y = queue.popleft()
    # 네 방향 확인, 1이면 큐에 삽입
    count = 0 # 네 방향 확인용
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 방문가능
      if graph[nx][ny] == 1:
        visited[nx][ny] = True # 방문처리
        graph.append((nx, ny))
        result += 1
        count += 1
      # 네방향 모두 확인, 갈 수 있는 곳x
      if count == 4:
        '''
BFS는 DFS처럼 한 갈래로 쭉쭉 가는게 아님. 재귀처럼 왔던길로 돌아 갈수 있는 것도 아님. 가까운 곳부터 queue에서 pop에서 세력을 넓혀나가듯 탐색하는 방법으로 갈라져 나온 곳으로 돌아가야하는데 result를 뺄수있는 방법이없음, 즉 잘못된 접근방법임..
          '''

  return result
  
visitied = [False] * 9
bfs(graph, 0, 0, visited)

## 답안예시_________________________________________________________
'''
경로를 이동하면서 방문처리할때 단순하게 1을 0으로 바꾸는게 아니라 계속해서 숫자를 1씩 증가시키면서 방문처리를 하기때문에 graph[x][y] 값을 확인하면(x,y)좌표가 몇번째 방문한 노드인지 바로 알수있게 한 점이 특이했다.
'''

from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  
  # queue가 빌때까지
  while queue:
    x, y = queue.popleft()
    # 네 방향 확인, 1이면 큐에 삽입
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 탐색 범위 밖이면 무시
      if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
        continue
      # 벽인 경우 무시, 이게 왜 꼭 있어야할까
      if graph[nx][ny] == 0:
        continue 
      if graph[nx][ny]== 1:
        graph[nx][ny] = graph[x][y] + 1 # 방문처리
        queue.append((nx, ny)) # 큐에 삽입

  # 우하단에있는 노드까지의 최단거리 return
  return graph[n-1][m-1]

# bfs 실행
print(bfs(0, 0))