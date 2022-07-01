# 블록 이동하기 | 2020 카카오 신입공채 1차 | 난이도 ★★★
'''
2x1크기의 로봇을 이동, 회전시켜서 (1, 1) -> (n, n) 위치로 이동시키는데 걸리는
최단시간을 출력하라.
0은 빈칸, 1은 벽이다.
'''
## 내 답안____________________________________________________________
# 네가지 방향(북, 동, 남, 서)
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# # 한칸 이동 함수
# def move(t, x1, y1, x2, y2):
#     for i in range(4):
#       nx1 = x1 + dx[i]
#       ny1 = y1 + dy[i]
#       nx2 = x2 + dx[i]
#       ny2 = y2 + dy[i]
#       # 이동 가능한 범위가 아니면 continue
#       if nx1 <= -1 or n <= nx1 or ny1 <= -1 or n <= ny1
#         or nx2 <= -1 or n <= nx2 or ny2 <= -1 or n <= ny2:
#         continue
#       # 두칸 다 빈칸이면
#       if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
#         move(t+1, nx1, ny1, nx2, ny2)
#       # 벽이면 이동하지않고 회전
#       else:
#         rotate(t+1, x1, y1, x2, y2)

# # 회전 함수
# def rotate(t, x1, y1, x2, y2):
#   # 가로일 때, 위로 회전
#   # 가로일 때, 아래로 회전
#   # 세로일 때, 오른쪽 회전
#   # 세로일 때, 왼쪽 회전
#   return True


# def solution(board):
#     # 로봇이 (N, N)에 도달했으면 시간 반환
#     if (x1 == n - 1 and y1 == n - 1) or (x2 == n - 1 and y2 == n - 1):
#       return t
#     # 아니면 이동
#     else:
#       move(t, x1, y1, x2, y2)
        

# result = 7
board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
x1, y1, x2, y2 = 0, 0, 0, 1 # 로봇의 위치
t = 0 # 시간 초기화
n = len(board[0])

print(solution(board))

'''
dfs의 핵심은 실제로 값을 넣어서 이동시키는게 아니라 다음에 실행할 재귀함수의 매개변수로 넘겨주는 것인 것 같다. 그러면 재귀함수 수행이 종료된 후 다시 나왔을 때, 간단하게 재귀함수에 들어가기 전 상태로 돌아갈 수 있는 것이다. 그 상태에서 또 다른 경우를 수행함으로써 탐색할 수 있다.
'''

## 답안예시_______________________________________________________
'''
비용이 모두 1로 동일한 최단거리 문제로 전형적인 BFS 탐색문제이다.
'''
from collections import deque

def get_next_pos(pos, board):
    next_pos = [] # 이동가능한 위치들
    pos = list(pos) # 집합 -> 리스트
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    
    # [상, 하, 좌, 우]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 모든 방향 확인
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x+dx[i], pos1_y+dy[i], pos2_x+dx[i], pos2_y+dy[i]
        # 빈칸이면
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            # 다음에 이동할 수 있는 위치 리스트에 집합으로 추가
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
    # 로봇이 가로로 놓여있는 경우
    if pos1_x == pos2_x:
        for i in [-1, 1]: # 위쪽으로 회전하거나, 아래쪽으로 회전
            if board[pos1_x+i][pos1_y] == 0 and board[pos2_x+i][pos2_y] == 0: # 위쪽 혹은 아래쪽 두 칸이 모두 비어있다면
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    # 로봇이 세로로 놓여있는 경우 
    elif pos1_y == pos2_y:
        for i in [-1, 1]: # 왼쪽으로 회전하거나, 오른쪽으로 회전
            if board[pos1_x][pos1_y+i] == 0 and board[pos2_x][pos2_y+i] == 0: # 왼쪽 혹은 오른쪽 두 칸이 모두 비어있다면
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
    # 현재 위치에서 이동할 수 있는 위치 반환
    return next_pos

def solution(board):
    n = len(board)
    # ★외벽을 1 로 만들어서 새로운 board를 생성한다.
    new_board = [[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
    q = deque()
    visited = []
    pos = {(1,1), (1,2)} # ★집합처리, 순서 바뀌어도 같음 -> 중복 방문 방지
    q.append((pos, 0)) # position, cost
    visited.append(pos) # 방문처리
    
    while q:
        pos, cost = q.popleft()
        if (n, n) in pos: # (n,n) 지점에 도달하면
            return cost
        for next_pos in get_next_pos(pos, new_board):
            # 방문하지 않은 지점이면
            if next_pos not in visited:
                # 큐에 삽입
                q.append((next_pos, cost+1))
                # 방문처리
                visited.append(next_pos)
    return 0