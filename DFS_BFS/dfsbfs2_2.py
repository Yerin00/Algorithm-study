# 미로 탈출 | 실전문제 | 난이도★1.5
'''
N x M 직사각형 미로에 갇혀있다. 미로에는 여러마리의 괴물이 있다.
동빈이는 (1,1)위치에 있으며 탈출구는 (N,M)위치에 있다.

- 한 번에 한 칸씩 이동
- 괴물이 있는 부분은 0, 괴물이 없는 부분은 1
동빈이가 탈출하기위해 움직여야하는 최소 칸의 개수를 구하시오.
(칸을 셀 때는 시작과 마지막 칸을 모두 포함해서 계산한다.)
'''
from collections import deque

n, m = 5, 6
graph = [[1,0,1,0,1,0],
        [1,1,1,1,1,1],
        [0,0,0,0,0,1],
        [1,1,1,1,1,1],
        [1,1,1,1,1,1]]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
  q = deque()
  q.append((x, y))

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 범위를 벗어나면 바로 종료
      if n <= nx or nx < 0 or m <= ny or ny < 0: 
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        q.append((nx, ny))
        
  return graph[n - 1][m - 1]
    

print(bfs(0, 0))