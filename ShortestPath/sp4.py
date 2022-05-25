# 플로이드 | 핵심유형 | 난이도 1.5
'''
n개의 도시(<=100), m개의 버스(<=100,000), 모든 버스마다 비용이 정해져있음.
★모든 도시의 쌍 (A, B)★에 대해서 최소비용을 구하는 프로그램을 작성하세요.

< 입력 >
- n
- m
- 시작도시, 도착도시, 비용

* 시작도시와 도착도시를 연결하는 노선은 하나가 아닐수도있다.
'''
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기자신으로 가는 비용 0으로 초기화
for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0

for _ in range(m):
  a, b, c = map(int, input().split())
  # 가장 짧은 간선 정보만 저장
  if c < graph[a][b]:
    graph[a][b] = c


  
  

