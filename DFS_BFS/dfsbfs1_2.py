# 음료수 얼려 먹기 | 실전문제 | 난이도★1.5
'''
N x M 크기의 얼음틀이 있다.
구멍이 뚫려있는 부분은 0, 칸막이가 있는 부분은 1로 표시된다.
구멍 뚫린 부분이 상하좌우로 붙어 있는 경우 서로 연결된 것으로 간주한다. 이때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.
'''
n, m = 4, 5
graph = [[0,0,1,1,0],
        [0,0,0,1,1],
        [1,1,1,1,1],
        [0,0,0,0,0]]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[0] * m for _ in range(n)]

def dfs(x, y):
  if 0 <= x and x <= n and 0<= y and y <= m: # 범위를 벗어나면 바로 종료
    return False
  elif visited[x][y] == 0: # 범위 내에 있고 아직 방문 전이면
    visited[x][y] = 1
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if graph[nx][ny] == 0 and visited[nx][ny] == 0:
      dfs(nx, ny)
    else:
      return False
  return True


result = 0 # 아이스크림의 수
for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      result += 1

print(result)

# 내 답안(오답)_____________________________________________

# n, m = 4, 5
# graph = [[0,0,1,1,0],
#         [0,0,0,1,1],
#         [1,1,1,1,1],
#         [0,0,0,0,0]]

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# visited = [[0] * m for _ in range(n)]

# def dfs(graph, x, y, visited):
#   count = 0
#   visited[x][y] = 1
#   for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     if 0 <= nx and nx <= n and 0<= ny and ny <= m and graph[nx][ny] == 0:
#       if visited[nx][ny] == 0: # 아직 방문하지않았으면
#         return dfs(graph, nx, ny, visited)
#   count += 1
#   return count


# result = 0 # 아이스크림의 수
# for i in range(n):
#   for j in range(m):
#     result += dfs(graph, i, j, visited)

# print(result)