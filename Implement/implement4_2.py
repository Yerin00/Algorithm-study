# 게임개발 | 실전문제 | 난이도 2
'''
NxM 직사각형 맵, 각 칸은 육지 또는 바다이다. 캐릭터는 동서남북 중 한 곳을 바라본다.

A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수이다. 바다로 된 공간에는 갈수없다.

1. 현재 위치에서 현재 방향을 기준으로 반시계 방향(90도)부터 갈곳을 정한다.
2. 캐릭터의 왼쪽 방향에 가보지않은 칸이 존재하면 왼쪽으로 회전 후 한칸 전진한다. 가보지않은 칸이 없다면 왼쪽으로 회전만 수행후 1단계로 돌아간다.
3. 만약 네 방향 모두 가본 칸이거나 바다로 되어있는 경우 바라본 방향을 유지한 채로 한 칸 뒤로 이동한 뒤 1단계로 돌아간다.
이때 뒤쪽이 바다인 경우면 **움직임을 멈춘다.**

위 과정을 반복수행 후 캐릭터가 방문한 칸의 수를 출력하라.
북, 동, 남, 서 -> 0, 1, 2, 3
육지, 바다 -> 0, 1
'''

n, m = map(int, input().split())
x, y, direction = map(int, input().split()) # 좌표와 바라보고있는 방향
graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

d = [[0] * m for _ in range(n)] # 방문 정보 처리
d[x][y] = 1 # 현재좌표 방문처리

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
  direction -= 1
  if direction == -1:
    direction = 3

# 시뮬레이션 시작
result = 1 # 방문한 칸의 수
turn_time = 0
while True:
  # 왼쪽으로 회전
  turn_left()
  # 가보지않은 칸 존재 -> 이동
  nx = x + dx[direction]
  ny = y + dy[direction]
  if d[nx][ny] == 0 and graph[nx][ny] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  # 가보지않은 칸 없거나 바다인 경우
  else:
    turn_time += 1
  # 네 방향 모두 갈수 없는 경우
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    # 뒤로 갈수있다면 뒤로 이동
    if graph[nx][ny] == 0:
      x = nx
      y = ny
    # 뒤가 바다인 경우 끝내기
    else:
      break
    turn_time = 0

print(result)