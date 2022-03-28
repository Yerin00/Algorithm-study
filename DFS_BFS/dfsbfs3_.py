# 특정거리의 도시 찾기
'''
도시의 수, 경로 수, 주어진 최단거리, 출발도시

bfs? dfs?

'''
## 답안예시___________________________________________


## 오답_______________________________________________
n, m, k, x = map(int, input().split())

# 그래프 입력받기
graph = []
for i in range(n):
  for j in range(m):
    # 출발, 도착 graph[a]는 a에서 갈수있는 도시의 리스트
    a, b = map(int, input().split())
    graph[a].append(b)

count = 0 # 거리계산

def dfs(x):
    # x에서 출발 출발
    for i in graph[x]:
      dfs(i)
    count += 1
    if count == k:
      return
    if count > k:
      return False

