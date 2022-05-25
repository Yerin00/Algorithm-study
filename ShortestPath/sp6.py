# 화성탐사 | ACM-ICPC | 난이도 ★★
'''
NxN 2차원 공간, 각 칸을 지나기위한 비용이 존재함.
[0][0]에서 [N-1][N-1]로 이동하는 최소비용을 출력하는 프로그램을 작성하세요. ★상하좌우★ 1칸씩 이동가능.

< 입력 >
1. 테스트 케이스 수 T
2. 정수 N
3. N개 줄에 걸쳐 각 칸의 비용이 주어짐 -> 다익스트라 알고리즘

3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
'''
## 답안예시______________________________________________
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 북, 동, 남, 서
dx = [-1, 0, 1, 0] # 행
dy = [0, 1, 0, -1] # 열

for T in range(int(input())): # 테스트 케이스
  N = int(input())
  graph = []
  for i in range(N):
    graph.append(list(map(int, input().split())))
    
  distance = [[INF] * N for _ in range(N)]

  # 초기값(시작점) 설정
  x, y = 0, 0
  q = [(graph[x][y], x, y)]
  distance[x][y] = graph[x][y]

  while q:
    dist, x, y = heapq.heappop(q)
    if distance[x][y] < dist:
      continue
    for i in range(4): # 네 방향
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= or ny < 0 or ny >= N: # 범위를 벗어나면 무시
        continue
      cost = dist + graph[nx][ny]
      if cost < distance[nx][ny]:
        distance[nx][ny] = cost # 거리 갱신
        heapq.heappush(q, (cost, nx, ny)) # 우선순위 큐에 삽입
  print(distance[N-1][N-1])
      

  