# 미래 도시  | 난이도 ★★ | M 기업 코딩테스트
'''
양방향, 모든 비용은 1로 통일
회사원 A는 1번회사에서 출발 -> K번 회사에서 소개팅후 -> X번 회사에서 방문판매한다.
최소 이동 경로를 출력하는 프로그램을 작성하라.

회사의 개수 N, 통로의 개수 M이 입력으로 들어온다.
만약 x번 회사에 도달할 수 없다면 -1을 출력한다.
'''

'''
앞의 예제 코드들은 단방향 예제인데 양방향으로 바꾸기!
중간에 반드시 거쳐야하는 노드가 존재함.
1->k가 최소이고, k->x가 최소이면 최종적으로 최소이다.
N, M <= 100 이기때문에 N^3을 해도 1,00
'''
## 답안예시_____________________________________________________________________
# 플로이드 워셜 알고리즘 사용

INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0

for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1 # 양방향 일 때는 b, a 도 입력시켜준다.

# x와 k 입력받기(최종 목적지, 거쳐갈 회사)
x, k = map(int, input().split())

for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 모든 경우를 구한 뒤 필요한 값만 빼내서 쓴다. 1->k + k->x
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우 -1 출력
if distance >= INF:
  print("-1")
else:
  print(distance)
    