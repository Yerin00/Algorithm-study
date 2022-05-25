# 팀 결성 | 핵심유형 | 난이도 ★★
'''
0~N번 까지의 번호를 가진 학생들.
처음에는 모두 다른 팀으로 구분되어 총 N + 1개의 팀이 존재함.
선생님이 팀합치기 연산과 같은 팀 여부 확인 연산을 사용할 수 있다.

같은 팀 여부 확인 연산에 대하여 한줄에 하나씩 YES, NO를 결과로 출력한다.
'''
# 팀 합치기 연산
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
    
# 팀 확인 연산  
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]
  
# 노드의 개수, 연산의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1)

# 자기 자신으로 초기화
for i in range(v + 1):
  parent[i] = i

for _ in range(v + 1):
  command, a, b = map(int, input().split())
  # 팀 합치기 연산
  if command == 0:
    union_parent(parent, a, b)

  # 같은 팀 여부 확인
  elif command == 1:
    if find_parent(parent, a) == find_parent(parent, b):
      print('YES')
    else:
      print('NO')
  
    