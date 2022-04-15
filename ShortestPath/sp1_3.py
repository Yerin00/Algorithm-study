# 최단경로
## 플로이드 워셜 알고리즘
'''
전체는 3중 for문, O(N^3)
<다익스트라 vs 플로이드 워셜>
- 그리디 vs 다이나믹 프로그래밍
- 1차원배열(출발지점이 정해져있음) vs 2차원 배열(모든 지점에서 모든 지점으로)
점화식: Dab = min(Dab, Dak + Dkb) = 'A에서 B로 가는 최소 비용' vs 'A에서 K를 거쳐 B로 가는 비용'중 더 작은 값으로 갱신한다.

K를 1부터 N까지 반복하면서, K를 제외한 N-1개의 노드 중 두개를 고르는 모든 경우를 고려해야한다.

알고리즘 자체는 간단하지만 시간복잡도가 N^3임에 주의해야한다.
'''

INF = int(1e9)

# 노드의 개수, 간선의 개수
n = int(input())
m = int(input())

# 2차원 리스트(그래프)를 만들고 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에게 가는 비용 0으로 초기화
for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a][b] = c

# 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
  for b in range(1, n + 1):
    if graph[a][b] == INF:
      print("INFINITY")
    else:
      print(graph[a][b], end=" ")
  print()
  
  