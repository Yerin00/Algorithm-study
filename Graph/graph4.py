# 여행계획 | 핵심유형 | 난이도 ★★
'''
<입력>
N개의 도시, 여행계획에 속한 도시의 수 M개
NxN 행렬에 임의의 두 여행지가 서로 연결되어있는지 여부 정보(0 or 1)

여행가능 -> YES
여행불가능-> NO

를 출력하라
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

n, m = map(int,input().split())
# parent 초기화
parent = [0] * (n + 1)
for i in range(1, n + 1):
  parent[i] = i
  
# union 연산을 각각 수행
for i in range(n):
  data = list(map(int, input().split()))
  for j in range(n):
    if data[j] == 1:
      union_parent(parent, i + 1, j + 1) # 노드의 번호가 1~N 이므로 각각1씩 더해준다.
  
# 여행 계획 입력
plan = list(map(int, input().split()))

result = True
# 여행계획에 속하는 모든 노드의 루트가 동일한지 확인
for i in range(m - 1):
  if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
    result = False

# 결과 출력
if result:
  print("YES")
else:
  print("NO")