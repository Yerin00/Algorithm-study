# 숨바꼭질 | 난이도 ★★ | USACO
'''
1~N번의 헛간중 하나를 골라 숨을수 있으며, 술래는 항상 1번에서 출발합니다.
전체 맵에는 두개의 헛간을 연결하는 총 M개의 양방향 통로가 존재.

최단거리가 가장 먼 헛간의 번호를 출력하라.

- 양방향, 비용1 동일
- 1번에서 출발
- N <= 20,000 M <= 50,000 숫자가 충분히 크기때문에 다익스트라 사용

헛간번호(만약 거리가 같은 헛간이 여러개면 번호가 가장 작은 헛간 출력),
헛간까지의 거리,
그 헛간과 같은 거리의 헛간 개수를 출력.

미래도시 문제와 조건은 비슷하지만 미래도시는
플로이드 워셜로 풀수있었음.

'''
import heapq


n, m = map(int, input().split())
INF =int(1e9)
graph = []
distance = [INF] * (n + 1)

# 자기 자신으로 가는 비용 0으로 초기화
for a in range(n):
  for b in range(n):
    if a == b:
      graph[a][b] = 0
      graph[b][a] = 0

# 통로 입력받기
for _ in range(m):
  a, b = map(int,input().split())
  graph[a][b] = 1

q = []
heapq.heappush(q, (1, 1, graph[x][y]))
while q:
  a, b, dist = heapq.heappop(q)
  # 이미 처리한 노드면 건너뛰기
  if distance[b] < dist :
    continue
  for i in range(n):
    cost = graph[i][b] + 1
    if cost < distance[b]:
      distance[b] = cost

max_value = distance[1]
max_index = 1
count = 0
for i in range(2, n + 1):
  if distance[i] > max_value:
    max_value = distance[i]
    max_index = i
    count = 0 # max_value 바뀔때마다 초기화(같은거리를 같는 헛간의 개수>>자기자신은 제외?)
  elif distance[i] == max_value:
    count += 1
    
print(max_index, max_value, count)



    
