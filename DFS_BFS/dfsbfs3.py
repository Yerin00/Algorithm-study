# 특정거리의 도시 찾기
'''
1~N번까지의 도시와 M개의 단방향 도로가 존재한다.
모든 도로의 거리는 1이다. 특정 도시 X로부터 출발하여
도달할 수 있는 모든 도시 중에서 최단거리가 K인 모든 도시의 번호를 출력하는 프로그램을 작성하라.

도시의 수N, 도로 수M, 주어진 최단거리K, 출발도시X
둘째줄부터 M개의 줄에 걸쳐 자연수 A, B(A->B로 가는 단방향 도로 존재)
가 주어진다.

- 도시의 번호를 출력할 때는 오름차순으로 한줄에 하나씩 출력한다.
- 도달할 수있는 도시 중 최단거리가 K인 도시가 하나도 없으면 -1을 출력한다.
'''
## 답안예시___________________________________________
from collections import deque

n, m, k, x = map(int, input().split())
# 그래프 입력받기
graph = [[] for _ in range(n + 1)]
for i in range(n):
  for j in range(m):
    # 출발, 도착 graph[a]는 a에서 갈수있는 도시의 리스트
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# BFS 수행
q = deque([x])

while q:
  now = q.popleft()
  for next_node in graph[now]:
    # 아직 방문하지않은 도시면
    if distance[next_node] == -1:
      # 최단거리 갱신
      distance[next_node] = distance[now] + 1
      q.append(next_node)
      
# 최단거리가 K인 도시의 번호 출력
check = False
for i in range(1, n + 1):
  if distance[i] == k:
    print(i)
    check = True
    
if check == False:
  print(-1)
    
    
## 오답_______________________________________________
# n, m, k, x = map(int, input().split())

# # 그래프 입력받기
# graph = []
# for i in range(n):
#   for j in range(m):
#     # 출발, 도착 graph[a]는 a에서 갈수있는 도시의 리스트
#     a, b = map(int, input().split())
#     graph[a].append(b)

# count = 0 # 거리계산

# def dfs(x):
#     # x에서 출발 출발
#     for i in graph[x]:
#       dfs(i)
#     count += 1
#     if count == k:
#       return
#     if count > k:
#       return False

