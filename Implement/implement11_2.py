# 치킨 배달 | 삼성전자 SW 역량테스트 | 난이도★1.5
'''
hint: 콤비네이션 사용
N x N 인 도시는 빈칸, 치킨집, 집 중 하나이다. (r, c) 행렬로 나타내며 1부터 시작한다.
집과 가장 가까운 치킨집 사이의 거리 = 치킨거리
도시의 치킨거리는 모든 집의 치킨거리의 합.

|r - r| + |c - c|로 구한다.
도시의 치킨집중에 M개만 남기고 폐업시킬때 도시의 치킨거리의 최솟값을 출력한다.
'''
from itertools import combinations # 치킨집을 뽑는 조합

# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#   graph.append(list(map(int, input().split())))
n, m = 5, 2
graph = [[0,2,0,1,0],
        [1,0,1,0,0],
        [0,0,0,0,0],
        [2,0,0,1,1],
        [2,2,0,1,2]]


house = [] # 집
chicken = [] # 치킨집
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      house.append((i, j))
    if graph[i][j] == 2:
      chicken.append((i, j))

chicken_m = list(combinations(chicken, m))
def get_sum(case):
  sum = 0 # 도시의 치킨거리
  for hx, hy in house:
    temp = 1e9
    for cx, cy in case:
      temp = min(temp, abs(hx - cx) + abs(hy - cy))
    
    sum += temp
  return sum

result = 1e9 # 도시의 치킨거리의 최솟값
for case in chicken_m:
  result = min(result, get_sum(case))

print(result)