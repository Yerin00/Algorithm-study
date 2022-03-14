# 탐색 알고리즘 DFS, 깊이우선탐색

# 인접행렬방식, adjacency matrix
# 인덱스로 두 노드 사이의 연결을 바로 확인 할 수 있다.

INF = 999999999 # 무한

graph = [
  [0, 7, 5],
  [7, 0, INF],
  [5, INF, 0]
]

print(graph)

# 인접리스트방식, adjacency list
# 노드 수가 많을 때 메모리 차지 적게한다.

# 행이 3개인 2차원 리스트
graph = [[] for _ in range(3)]

# 노드 0에 연결된 정보(노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1
graph[1].append((0, 7))

# 노드 2
graph[2].append((0, 5))

print(graph)

# 예제____________________________________________________
# DFS 메서드 정의
def dfs(graph, v, visited):
  # 현재 노드 방문 처리
  visited[v] = True
  print(v, end=' ')
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

# 리스트 자료형
graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False]*9

dfs(graph, 1, visited)