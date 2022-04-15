# 방법2 9-2.py 개선된 다익스트라 알고리즘 코드________________________________
'''
우선순위 큐(heapq 라이브러리)를 사용하면 더 빠르게 최단경로를 구할 수 있다.
자동으로 내부에서 정렬을 해주기때문에 get_smallest_node()가 필요없다.

'''

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호 입력받기
start = int(input())
# 각 노드에 연결되어있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

def dijkstra(start):
  q = []
  # 시작 노드로 가기위한 최단 경로는 0으로 설정하여, 큐에 삽입
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q: # 큐가 비어있지않다면
    # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기
    dist, now = heapq.heappop(q)
    # 현재노드가 이미 처리된 적 있는 노드라면 무시
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1] # i[1]: 비용
      # 현재 노드를 거쳐서 다른노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
        
dijkstra(start)

# 모든 노드로 가기위한 최단 거리를 출력
for i in range(1, n + 1):
  # 도달할 수 없는 경우, 무한이라고 출력
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])