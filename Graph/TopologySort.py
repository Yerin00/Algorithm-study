## 위상정렬
'''
위상정렬 : 방향 그래프의 모든 노드를 방향성에 거스르지않도록 순서대로 나열하는 것

ex: 선수과목 고려한 학습순서 설정

1. 진입차수가 0인 노드를 큐에 넣는다.
2. 큐가 빌때까지 반복한다.
  2-1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
  2-2. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
'''
# 10-6.py
from collections import deque

# 노드의 개수와 간선의 개수를 입력받기
v, e = map(int, input().split())

# 모든 노드에 대한 진입 차수 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]

# 모든 간선 정보 입력받기
for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b) # a에서 b로 이동가능
  # 진입차수 1 증가
  indegree[b] += 1

def topology_sort():
  result = []
  q = deque()
  # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
  for i in range(1, v + 1):
    if indegree[i] == 0:
      q.append(i)
  # 큐가 빌 때까지 반복
  while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)
  for i in result:
    print(i, end=' ')

topology_sort()
  