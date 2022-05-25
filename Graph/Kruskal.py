## 신장 트리
# 크루스칼 알고리즘(Kruskal Algorithm)
'''
- 신장트리: 모든 정점에 대한 최소한의 연결만을 남긴 그래프
- 모든 도시를 연결할 때, 최소한의 비용으로 연결

- 그리디 알고리즘
- 가장 거리가 짧은 간선부터 집합에 추가하되, 사이클을 발생시키는 간선은 제외한다. -> 항상 최적의 해
- 최적 간선의 수 = 노드의수 - 1

1. 오름차순으로 정렬
2. 사이클 발생시키는지 확인
  1) 사이클 발생X -> 최소 신장 트리에 포함함.
  2) 사이클 발생O -> 최소 신장 트리에 포함하지않음.
3. 모든 간선에 대하여 2번을 반복
'''
# 10-5.py
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  # 루트 노드가 아니면, 루트노드 찾을때까지 재귀호출
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b: # a가 더 작으면
    parent[b] = a
  else: # b가 더 작거나 같으면
    parent[a] = b


# 노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
  parent[i] = i

# 간선 정보 입력받기
for _ in range(e):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b)) # 비용순 정렬을 위해 첫번째 원소 = cost로 설정

# 정렬
edges.sort()

# 간선을 하나씩 확인하며 수행
for edge in edges:
  cost, a, b = edge
  # 사이클이 발생하지 않는 경우에만 집합에 포함
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

print(result)