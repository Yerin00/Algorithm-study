# 뱀 | 삼성전자 SW 역량테스트 | 난이도★★
'''
게임에 뱀이 나와서 기어다니는데 사과를 먹으면 뱀의 길이가 늘어난다.
뱀이 벽또는 자기자신의 몸과 부딪히면 게임이 끝난다.
NxN 정사각 보드, 몇몇 칸에는 사과가 놓여져있다.
보드의 상하좌우에는 벽이있다. 뱀의 초기위치는 왼쪽 상단끝이고 뱀의 길이는 1로 시작한다. 뱀은 처음에 오른쪽 방향을 보고있다.
뱀은 매초마다 이동한다.
- 몸길이를 늘려 머리를 다음칸에 위치시킵니다.
- 이동한 칸에 사과가 있다면 그 칸의 사과는 없어지고 꼬리는 움직이지않습니다.
- 사과가 없다면 몸길이를 줄여서 꼬리가 위치한 칸을 비워줍니다. 즉 몸길이는 변하지않습니다.

사과의 위치와 뱀의 이동 경로가 주어질때 이 게임이 몇초에 끝나는지 계산하시오.

< 입력 >
보드의 크기 N, 사과의 개수 K
사과의 위치 행, 열
뱀의 방향 전환 횟수 L,
방향 전환 정보 정수 X, 문자 C(L, D 90도 회전)

'''
# N x N graph 초기화하기
n = int(input())
graph = []
for i in range(n + 2):
  for j in range(n + 2):
    # 범위 밖이면 벽(=1) 설정
    if i == 0 or j == 0 or i == n + 1 or j == n + 1: 
      graph[i][j] = 1
    else:
      graph[i][j] = 0
# 사과 입력받기
k = int(input())
apple = []
for i in range(k):
  x, y = map(int, input().split())
  apple[x][y] = 1

t = 0 # 현재 시간
dir = 1 # 현재방향
x, y = 1, 1 # 시작 위치
e_x, e_y = 1, 1 # 꼬리의 위치
# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


l = int(input()) # 방향전환 횟수
for i in range(l):
  time, direction = input().split()
  time = int(time)
  while t < time:
    # 전진
    nx = x + dx[dir]
    ny = y + dy[dir]
    if graph[nx][ny] == 0:
      x = nx
      y = ny
    if apple[x][y] != 1: # 사과가 없으면

    t += 1

  # 방향 전환
  if direction == 'L':

  elif direction == 'D':