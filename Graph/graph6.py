# 어두운 길 | 
'''
- N개의 집(1<= N <= 200,000)과 M개의 도로(N-1 <= M <= 200,000)
- 집: 0 ~ N-1번
- 특정한 도로의 가로등을 하루동안 켜기위한 비용 = 해당 도로의 길이
- 임의의 두 집에 대하여 가로등이 켜진 도로만으로 오갈 수 있다.
- 일부 가로등을 비활성화 -> 절약할 수 있는 최대 금액 출력
- 최소신장트리 문제(MST) 크루스칼 알고리즘, 그리디
'''

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

    
# 노드의 개수, 간선의 개수, A -> B 비용 C 입력받기
n, m = map(int, input().split())
# 집합의 부모 정보 리스트 초기화
parent = [0] * n
for i in range(n):
  parent[i] = i

# 간선 정보 입력받기
edges = []
cost = 0 # 모든 간선의 비용을 합한 값
for _ in range(m):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))
  sum += cost

# cost에 대하여 오름차순 정렬
edges.sort()

result = 0 # 가로등을 비활성화한 뒤의 비용
# 모든 간선에 대해 반복
for edge in edges:
  cost, a, b = edge
  # 사이클이 발생하지않으면
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)    
    result += cost

print(sum - result) # 원래의 비용 - 절약후 비용 = 절약된 비용