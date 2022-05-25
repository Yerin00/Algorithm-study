# 정확한 순위 | 난이도 ★★ | K 대회
'''
점수는 없고 n명의 성적을 비교한 결과만 m개있다.
a->b 로 화살표는 a가 b 보다 성적이 낮다는뜻이다.
정확한 순위를 구할 수 있는 학생의 수를 출력하라.

학생 수 n은 500이하 이므로 플로이드 워셜 알고리즘를 이용한다.
'''
INF = int(1e9)
graph[[INF] * (n + 1) for _ in range(n + 1)]
n, m = map(int, input().split())

# 자기 자신으로 가는 루트 0으로 초기화
for a in range(n + 1):
  for b in range(n + 1):
    if a == b:
      graph[a][b] = 0

# 성적비교 입력받기
for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1

# 플로이드 워셜 알고리즘 수행
  
for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
      
result = 0
# 각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 체크
for i in range(1, n + 1):
  count = 0
  for j in range(1, n + 1):
    # i로 들어오거나 나가는 모든 화살표의 개수 count
    if graph[i][j] != INF or graph[j][i] != INF:
      count += 1
    # n번
    if count == n:
      result += 1

print(result)