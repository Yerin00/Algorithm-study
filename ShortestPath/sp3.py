# 전보 | 난이도 ★★★ | 유명 알고리즘 대회
'''
N개의 도시, 단방향, 비용

C도시에서 보낸 메세지를 받게되는 도시의 개수와 도시들이 모두 메시지를 받기위해 걸리는 시간은 얼마인지 계산하는 프로그램을 작성하시오.

N, M: 도시의 개수, 통로의 개수, C: 메시지를 보내고자하는 도시C

N, M의 범위가 충분히 크기때문에 우선순위 큐를 이용하여 다익스트라 알고리즘을 작성. 
'''

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수, 시작 노드 번호를 입력받기
n, m, start = map(int, input().split())

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

count = 0 # 도달할 수 있는 노드의 개수
max_distance = 0 # 도달할 수 있는 노드 중에서 가장 멀리있는 노드와의 최단거리★
for i in range(1, n + 1):
  if distance[i] != INF:
    count += 1
    max_distance = max(max_distance, distance[i])
print(count - 1, max_distance) # count중에서 start노드는 제외해야하므로 1을 뺌


'''
도달할 수 있는 모든 도시가 메세지를 받기까지 걸리는 시간이라고하길래.. 각각.. 인줄 알았는데
아니었음. 도시 X에게 전해주면 그물망처럼 동시에 X 도시에서 다른 도시로 메세지가 퍼져나가기 때문임.
즉, 모든 도시가 메세지를 받기위해서는 가장 멀리있는 노드와의 최단거리만큼의 시간이 걸림.

'''