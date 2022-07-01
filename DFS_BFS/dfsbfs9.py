# 인구 이동 | 삼성전자 SW 역량테스트 | 난이도 ★★
'''
N x N 크기의 땅이 있고 땅은 1x1개의 칸으로 나누어져있다.
각각의 땅에는 나라가 하나씩 존재하며 r행 c열에 있는 나라에는
A[r][c] 명이 살고있다.
인접한 나라 사이에는 국경선이 존재한다.

오늘부터 인구이동이 다음과 같이 진행되고 더이상 아래방법에 의해 인구이동이 없을때가지 지속된다.
- 국경선을 공유하는 두 나라의 인구 차이가 L명이상, R명이하라면 두 나라가 공유하는 국경선을 오늘 하루동안 연다.
- 열어야하는 국경선을 모두 연 뒤 인구이동을 시작한다.
- 이동가능한 나라를 오늘 하루동안은 연합이라고 한다.
- 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
- 연합을 해체하고 모든 국경선을 닫는다.

각 나라의 인구수가 주어졌을 때, 인구이동이 몇번 발생하는 지 구하는 프로그램을 작성하세요.

첫째줄에 N, L, R이 주어짐.
둘째줄부터 N개의 줄에 각 나라의 인구수가 주어진다.
'''
## 답안예시___________________________________--
from collections import deque

n, l, r = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def process(x, y, index):
  # (x, y)의 위치와 연결된 나라(연합) 정보 리스트
  united = []
  united.append((x, y))

  q = deque()
  q.append((x, y))
  union[x][y] = index # 현재 연합의 번호 할당
  summary = graph[x][y] # 현재 연합의 전체 인구 수
  count = 1 # 현재 연합의 국가 수

  # 큐가 빌 때까지 반복(BFS)
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
        if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
          q.append((nx, ny))
          # 연합에 추가
          union[nx][ny] = index
          summary += graph[nx][ny]
          count += 1
          united.append((nx, ny))
  # 연합 국가끼리 인구 분배
  for i, j in united:
    graph[i][j] = summary // count
  return count
  

total_count = 0

# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
  union = [[-1] * n for _ in range(n)]
  index = 0
  for i in range(n):
    for j in range(n):
      if union[i][j] == -1: # 해당 나라가 아직 처리되지 않았다면
        process(i, j, index)
        index += 1
  # 모든 인구 이동이 끝난 경우
  if index == n * n:
    break
  total_count += 1

# 인구 이동 횟수 출력
print(total_count)


  