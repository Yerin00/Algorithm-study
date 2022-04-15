# 가장 빠른길 찾기

## 다익스트라(Dijkstra) 최단경로 알고리즘
'''
- 그리디
- 출발지점이 정해진다. (start)
- 1차원 배열 distance의 값을 갱신시켜주며 최단 경로를 찾는다.
'''
# 방법1 9-1.py 간단한 다익스트라 알고리즘 코드________________________________
import sys
input = sys.stdin.readline
INF = int(1e9) # int로 형변환 원래 했었나...?

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())

# 시작 노드 번호를 입력받기
start = int(input())
graph = [[] for i in range(n + 1)]
# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

for _ in range(m):
  a, b, c = map(int, input().split())
  # a -> b 의 비용이 c
  graph[a].append((b, c))

# 방문하지않은 노드중에서 최단거리가 가장 짧은 노드의 번호를 반환
def get_smallest_node():
  min_value = INF
  index = 0
  for i in range(1, n + 1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijkstra(start):
  # 시작 노드에 대해 초기화
  distance[start] = 0
  visited[start] = True

  for j in graph[start]:
    distance[j[0]] = j[1] # j[0]: 도착노드, j[1]: 비용
  # 시작노드를 제외한 전체 n - 1개의 노드에 대해 반복
  for i in range(n - 1):
    # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문처리
    now = get_smallest_node()
    visited[now] = True

    # 현재 노드와 연결된 다른 노드 확인
    for j in graph[now]:
      cost = distance[now] + j[1]
      if cost < distance[j[0]]:
        distance[j[0]] = cost

dijkstra(start)

# 모든 노드로 가기위한 최단 거리를 출력
for i in range(1, n + 1):
  # 도달할 수 없는 경우, 무한(INFINITY)라고 출력
  if distance[i] == INF:
    print("INFINITY")
  # 도달할 수 있는 경우 거리를 출력
  else:
    print(distance[i])
  
