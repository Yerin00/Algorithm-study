# 음료수 얼려 먹기 | 실전문제 | 난이도★1.5
# DFS

n, m = map(int, input().split())

graph=[]
for i in range(n):
  graph.append(list(map(int,input()))) # 입력이 공백없이 들어오기때문에 input().split() 하면 안됨


def dfs(x, y):
  # NxM 범위를 벗어나는 경우 바로 종료
  if x <= -1 or n <= x or y <= -1 or m <= y:
    return False
  # 탐색 가능
  if graph[x][y] == 0:
    graph[x][y] = 1 # 방문완료 변경 
    # 남, 동, 북, 서 순서대로 네방향 체크
    dfs(x+1,y)
    dfs(x,y+1)
    dfs(x-1,y)
    dfs(x,y-1)
  else:
    return False
  
  return True

result = 0

for i in range(n):
  for j in range(m):
    # 탐색가능하면 dfs로 탐색
    if graph[i][j] == 0:
      if dfs(i, j) == True:
        result += 1

print(result)

## 답안예시1._______________________________

# n, m = map(int, input().split())

# graph=[]
# for i in range(n):
#     graph.append(list(map(int,input())))

# def dfs(x, y):
#     # NxM 범위를 벗어나는 경우 바로 종료
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#   # 탐색 가능
#     if graph[x][y] == 0:
#         graph[x][y] = 1 # 방문완료 변경 
#         # 상, 하, 좌, 우 순서대로 네방향 체크
#         dfs(x - 1, y)
#         dfs(x, y - 1)
#         dfs(x + 1, y)
#         dfs(x, y + 1)
#         return True
#     return False


# # 모든 노드에 대하여 음료수 채우기
# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j) == True:
#             result += 1

# print(result)

