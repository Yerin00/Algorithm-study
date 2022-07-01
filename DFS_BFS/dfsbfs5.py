# 경쟁적 전염 | 핵심유형 | 난이도 ★★
'''
N x N 크기의 시험관
바이러스의 종류: 1~K
매초 마다 모든 바이러스가 상하좌우의 방향으로 증식(번호가 낮은 바이러스가 먼저 증식함)

S초가 지난후 (X, Y)에 존재하는 바이러스의 종류를 출력하는 프로그램 작성.
존재하지않는다면 0을 출력

'''
## 답안예시__________________________________________________________
from collections import deque
n, k = map(int, input().split())

graph = [] # N x N
data = [] # 바이러스 정보

for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(n):
    if graph[i][j] != 0: # 바이러스가 존재하면
      data.append((graph[i][j], 0, i, j)) # 바이러스 번호, 시간, x, y좌표
data.sort() # 정렬 후 큐로 옮기기
q = deque(data)
    
# S초 후 구해야하는 x, y 좌표
target_s, target_x, target_y = map(int, input().split())

# 4가지 방향(북, 동, 남, 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1] 

# BFS(너비우선탐색)
while q:
  virus, s, x, y = q.popleft()
  # S초가 지나거나 q가 빌때까지 반복
  if s == target_s:
    break
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx and nx < n and 0 <= ny and ny < n: # 빼먹지마. 중요!
      if graph[nx][ny] == 0:
        graph[nx][ny] = virus
        data.append((virus, s+1, nx, ny)) # 아 시간처리를 이렇게 하네..진짜 괜찮은 방법이다..

print(graph[target_x - 1][target_y - 1])