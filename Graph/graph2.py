# 도시 분할 계획 | 기초 문제집 | 난이도 ★★
'''
N개의 집, 집들을 연결하는 M개의 길
양방향, 유지비용

- 마을을 두개의 마을로 분할하고자 한다.
- 마을에는 최소 한 개 이상의 집이 존재해야한다.
- 임의의 두집 사이에 경로가 항상 존재해야한다.
- 두 마을 사이의 길을 필요없다.

유지비 합의 최솟값을 출력하라.

★ 전체 그래프에서 2개의 최소 신장 트리 만들기★
-> 최소 신장 트리를 찾은 뒤 간선 중 가장 비용이 큰 간선을 제거한다.
'''
# 특정 원소가 속한 집합 확인 연산  
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 두 원소가 속한 집합 합치기 연산
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
    
# 집의 개수N, 길의 개수 M
v, e = map(int, input().split())
parent = [0] * (v + 1)

# 자기 자신으로 초기화
for i in range(1, v + 1):
  parent[i] = i

edges = [] # 간선 정보
result = 0 # 최소 신장 트리의 비용합

# 길의 정보(a, b집을 연결하는 길의 유지비 c)
for _ in range(e):
  cost, a, b = map(int, input().split())
  edges.append((cost, a, b)) # cost로 정렬하기 위해서 제일 앞에 둠

edges.sort() # 비용순으로 간선 정렬
last = 0 # 간선 중 가장 비용이 큰 간선 초기화

# 간선을 하나씩 확인
for edge in edges:
  cost, a, b = edge
  # 사이클이 발생하지않는 경우에만 집합에 포함
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost
    last = cost

print(result - last)