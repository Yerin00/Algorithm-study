# 탐색 알고리즘 BFS, 너비우선탐색
from collections import deque

# BFS 메서드
def bfs(graph, start, visited):
  queue = deque([start]) # queue에 [1]이 저장됨
  # 현재 노드 방문 처리
  visited[start] = True

  # queue가 빌때까지 반복
  while queue:
    # 큐에서 하나의 원소를 뽑아 출력
    v = queue.popleft()
    print(v, end=' ')
    # 해당 원소와 연결된, 방문하지않은 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1,7]
]

visited = [False]*9

bfs(graph,1,visited)