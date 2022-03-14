# 게임개발 | 실전 | 난이도★★
## 답안예시1._________________________________________________
n, m = map(int,input().split())

# 방문한 위치 저장용 맵, 0으로 초기화
d = [[0]*m for _ in range(n)]
# 현재 위치 입력
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보 입력
array = []
for i in range(n):
  array.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3 # 순환

# 시뮬레이션 시작
count = 1 # 방문한 칸 수
turn_time = 0 # 한 자리서 회전 수
while True:
  # 왼쪽으로 회전
  turn_left()
  print()
  # next_x, next_y
  nx = x + dx[direction] 
  ny = y + dy[direction]
  print("nx, ny:",nx, ny)
  # 가보지 않았고, 이동 가능한가
  if d[nx][ny] == 0 and array[nx][ny] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0 # 이동 후 초기화
    continue
  # 가보지않은 칸이 없거나 바다인 경우
  else:
    turn_time += 1
  
  if turn_time == 4:
    nx = x - dx[direction] 
    ny = y - dy[direction]
    # 뒤로 갈 수 있다면 이동(바다x)
    if array[nx][ny] == 0:
      x = nx
      y = ny
    else:
      break
    turn_time = 0 # 뒤로 백 후 초기화

print(count)


## 오답노트___________________________________________________

# n, m = map(int, input().split())
# x, y, d = map(int, input().split())
# tempx, tempy = 0, 0

# Map = []
# for i in range(n):
#   Map.append(list(map(int, input().split())))

# # 북(0), 동(1), 남(2), 서(3)
# dx = [0, 1, 0, -1]
# dy = [-1, 0, 1, 0]

# # 방문한 칸의 수, 지금 현재 서있는 위치도 포함
# result = 1 
# # check = 0
# ## 오답노트
# while True:
#   count = 0 # 네 방향 체크
#   # 왼쪽으로 네번 돌고 다 1이면 마지막 쳐다보는 방향 뒤로 1칸 백
#   for direction in reversed(range(d + 1, d + 5)):    
#     # 왼쪽으로 회전후 이동한 좌표
#     direction = direction % 4
#     tempx = x + dx[direction]
#     tempy = y + dy[direction]
    
#     # 갈 수 있는 곳이 있는가
#     if Map[tempx][tempy] == 0:
#       # yes. 이동 & 방문칸수 증가
#       x = tempx
#       y = tempy
#       Map[x][y] = 2 # 가본칸은 2로 변경
#       result += 1
#     else: 
#       # No. count 증가, 종료조건 확인
#       count += 1
#       if count == 4:
#         # 네칸 다 이동 불가면 보고있는 방향에서 뒤로 한칸 이동
#         x = x - dx[direction]
#         y = y - dy[direction]
#         if Map[x][y] == 1:
#           # 뒤로 이동 후 바다면 break
#           # check = 1
#           break

# print(result)
