# 토마토
'''
https://www.acmicpc.net/problem/7569
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들이 익게된다.
위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯방향에 있는 토마토는 인접한 토마토이다.

철수는 창고에 보관된 토마토들이 며칠 후에 다 익게 되는지 최소 일수를 알고싶어한다.
단, 일부 칸에는 토마토가 들어있지 않을 수도 있다.

상자의 크기 M(가로 칸의 수), N(세로 칸의 수)과 쌓아올려지는 상자의 수 H
(단, 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100 이다.)
가장 밑의 상자부터 가장 위의 상자까지에 저장된 토마토들의 정보가 주어진다.
정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
저장될 때부터 모든 토마토가 익어있다면 0을 출력하고, 토마토가 모두 익지 못하면 -1을 출력한다.

# 이렇게는 list index out of range 발생
# for k in range(h):
#   for i in range(n):
#     data[k][i].append(list(map(int, input().split())))
'''
from collections import deque
import sys

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

# bfs 함수
def bfs():
  while q:
    z, x, y = q.popleft()
    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]
      if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h: # 범위 내에 있고
        if data[nz][nx][ny] == 0: # 안익은 토마토라면
          data[nz][nx][ny] = data[z][x][y] + 1 # 익게만들기
          q.append([nz, nx, ny])
        


# main
m, n, h = map(int, input().split()) # 열, 행, 높이
q = deque([]) # []를 넣고 안넣고의 차이가 뭐지?

data=[]
check = False # 안 익은 토마토가 하나라도 있는가
for k in range(h):
  line = []
  for i in range(n):
    line.append(list(map(int, sys.stdin.readline().split())))
    for j in range(m):
      if line[i][j] == 1: # 익은 토마토면
        q.append([k, i, j]) # 높이, 행, 열
      elif line[i][j] == 0: # 안 익은 토마토면
        check = True
  data.append(line)

if check == False: # 안 익은 토마토가 없으면
  print(0)
  exit(0)
else: # 아니면 bfs실행
  bfs()
  result = 0
  for k in range(h):
    for i in range(n):
      for j in range(m):
        if data[k][i][j] == 0: # 안 익은 토마토 있으면
          print(-1)
          exit(0)
      result = max(result, max(data[k][i]))

print(result- 1)

'''
for i in graph:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        day = max(day,max(j))
'''

        

    


  
    
  