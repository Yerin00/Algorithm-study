# 블록 이동하기 | 2020 카카오 신입공채 1차 | 난이도 ★★★
'''
2x1크기의 로봇을 이동, 회전시켜서 (1, 1) -> (n, n) 위치로 이동시키는데 걸리는
최단시간을 출력하라.
0은 빈칸, 1은 벽이다.
'''
from collections import deque
def get_next_pos(pos, board):
  next_pos = [] # 이동가능한 위치들
  pos = list(pos) # 집합 -> 리스트
  pos1_x, pos1_y, pos2_x, po2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

  # 상하좌우
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  # 상하좌우 확인 후 이동
  for i in range(4):
    pos1_next_x, pos1_next_y, pos2_next_x, po2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], po2_y + dy[i]
    # 빈칸이면
    if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][po2_next_y] == 0:
      # 다음에 이동할 수 있는 위치 리스트에 집합으로 추가
      next_pos.append({(pos1_next_x, pos1_next_y),(pos2_next_x, pos2_next_y)})

  # 로봇이 가로로 놓여있는 경우
  if pos1_x == pos2_x:
    for i in [-1, 1]:
      # 위쪽 혹은 아래쪽 두 칸이 모두 비어있다면
      if board[pos1_x+i][pos1_y] == 0 and board[pos2_x+i][pos2_y] == 0: 
        next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
        next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
  # 로봇이 세로로 놓여있는 경우
  elif pos1_y == pos2_y:
    for i in [-1, 1]: # 왼쪽으로 회전하거나, 오른쪽으로 회전
      # 왼쪽 혹은 오른쪽 두 칸이 모두 비어있다면
      if board[pos1_x][pos1_y+i] == 0 and board[pos2_x][pos2_y+i] == 0: 
        next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
        next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
  return next_pos

def solution(board):
  # 맵의 외곽에 벽(1)을 두는 형태로 맵 변형
  n = len(board)
  new_board = [[1] * (n+2) for _ in range(n+2)]
  for i in range(n):
    for j in range(n):
      new_board[i + 1][j + 1] = board[i][j]
  q = deque()
  visited = []
  pos = {(1, 1),(1, 2)} # 집합처리
  q.append((pos, 0)) # pos, cost
  visited.append(pos)

  while q:
    pos, cost = q.popleft()
    if (n, n) in pos: # (n, n) 지점에 도달하면
      return cost
    for next_pos in get_next_pos(pos, new_board):
      # 방문하지않은 지점이면
      if next_pos not in visitied:
        q.append((next_pos, cost + 1))
        visited.append(next_pos)
  return 0