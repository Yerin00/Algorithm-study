## 서로소 집합
'''
서로소 집합: 공통원소가 없는 두 집합
ex) {1, 2} 와 {3, 4}

<알고리즘>
1. union(합집합) 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인한다.
 1-1. A와 B의 루트 노트 A`, B`를 찾는다.
 1-2. A`를 B`의 부모노드로 설정한다.(B`가 A`를 가리키도록 한다.)
2. 모든 union(합집합) 연산을 처리할 때 까지 1번 과정을 반복한다.

<입력>
노드의 개수 v, 간선(union연산)의 개수 e
union할 두 노드 번호
<출력>
각 원소가 속한 집합:
부모 테이블:
'''
##10-1.py____________________________________________________________
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  if parent[x] != x:
    return find_parent(parent, parent[x]) # ★ 여기도 리턴임!!!
  return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 노드의 개수와 union연산의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 어차피 자기자신으로 초기화할 건데 왜 0으로 초기화하지?

# 부모 테이블상에서 부모를 자기자신으로 초기화
for i in range(1, v + 1):
  parent[i] = i

# union 연산을 각각 수행
for _ in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)
    
# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합:', end='')
for i in range(1, v + 1):
  print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블:', end='')
for i in range(1, v + 1):
  print(parent[i], end=' ')


  
## 10-2.py____________________________________________________________
'''
경로 압축 기법 소스코드
10-1의 코드에서는
1 <- 1
1 <- 2 <- 3 <- 4 <- 5
로 연결되어있어서 부모 노드를 순서대로 거슬러 올라가야하므로 최대 O(V)의 시간이
소요될 수 있다.

경로 압축 기법에서는 find 함수를 재귀적으로 호출한 뒤 부모 테이블값을 갱신하면 각각의 노드들이 자신의 부모노드를 직접 참조하게 되므로 시간을 절약할 수 있다.
'''
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

  
## 10-3.py____________________________________________________________
'''
개선된 서로소 집합 알고리즘 소스코드
'''
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 노드의 개수와 union연산의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 어차피 자기자신으로 초기화할 건데 왜 0으로 초기화하지?

# 부모 테이블상에서 부모를 자기자신으로 초기화
for i in range(1, v + 1):
  parent[i] = i

# union 연산을 각각 수행
for _ in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)
    
# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합:', end='')
for i in range(1, v + 1):
  print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블:', end='')
for i in range(1, v + 1):
  print(parent[i], end=' ')

## 10-4.py____________________________________________________________
'''
서로소 집합을 활용한 사이클 판별 소스코드
'''
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 노드의 개수와 union연산의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 어차피 자기자신으로 초기화할 건데 왜 0으로 초기화하지?

# 부모 테이블상에서 부모를 자기자신으로 초기화
for i in range(1, v + 1):
  parent[i] = i

cycle = False # 사이클 발생 여부

# union 연산을 각각 수행
for _ in range(e):
  a, b = map(int, input().split())
  # 사이클이 발생한 경우 종료
  if find_parent(parent, a) == find_parent(parent, b):
    cycle = True
    break
  # 사이클이 발생하지 않았다면 union 수행
  else:
    union_parent(parent, a, b)

if cycle:
  print("사이클이 발생했습니다.")
else:
  print("사이클이 발생하지않았습니다.")
