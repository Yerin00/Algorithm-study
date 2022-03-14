# 뱀 | 삼성전자 SW 역량테스트 | 난이도★★
## 내 답안
# n = int(input())
# #방향

# x, y = 1, 1 # 시작점
# body = [[0]*(n+1) for _ in range(n+1)] # 뱀의 몸통위치
# body[1][1] = 1
# # k개의 사과와 사과의 위치
# k = int(input())
# apples = []
# for i in range(k):
#   apples.append(list(map(int,input().split())))

# # l번의 회전과 회전시각 
# l = int(input())
# rotations = []
# for i in range(l):
#   rotations.append(list(input().split()))
  
# print(rotations)

# # 한칸 이동

# # 회전함수

# # 게임종료 함수
# def gameover(nx, ny):
#   # NxN 보드를 벗어나거나 자신의 몸과 충돌한 경우
#   if  n < nx or nx < 1 or n <ny or ny < 1 or body[nx][ny] == 1:
#     return True
#   else:
#     return False

# # 게임이 시작된 후 지난 시간
# time = 1 
# while True:
  
#   # 게임 종료
#   if gameover()==True:
#     break
  

# print(time)

## 답안예시1.___________________________________________________
n = int(input())
k = int(input())
data = [[0]*(n+1) for _ in range(n+1)] # 맵 정보
info = [] # 방향 회전 정보

# 맵 정보(사과 있는 곳 1)
for _ in range(k):
  a, b = map(int, input().split())
  data[a][b] = 1

# 방향 회전 정보 입력
l = int(input)
for _ in range(l):
  x, c = input().split()
  info.append(int(x),c))

# 처음에 오른쪽을 보고 있으므로 동, 남, 서, 북 ★
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
  if c=='L':
    direction = (direction - 1) % 4
  else:
    direction = (direction + 1) % 4
  return direction

def simulate:
  x, y = 1, 1 # 뱀의 머리위치
  data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
  direction = 0 # 동쪽
  time = 0 # 게임 시작 후 지난 시간
  index = 0 # 다음에 회전할 정보
  q = [(x,y)] # 뱀이 차지하고있는 위치정보(꼬리가 앞쪽), 큐(FIFO)★★★
  while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
    if 1 <= nx and nx <= n and 1<= ny and ny<=n and data[nx][ny] !=2:
      # 사과가 없다면 이동 후 꼬리 제거★
      if data[nx][ny] == 0:
        data[nx][nx] = 2
        q.append((nx,ny)) # 머리의 다음 좌표 추가
        px, py = q.pop(0) # 꼬리쪽 좌표 pop
        data[px][py] = 0 # 꼬리 제거
      # 벽이나 뱀의 몸통과 부딪혔다면
      else:
        time += 1
        break
      x, y = nx, ny # 다음위치로 머리 이동
      time += 1
      if index < 1 and time == info[index][0]: # 회전할 시간인 경우 회전
        direction = turn(direction, info[index][1])
        index += 1
  return time

print(simulate())