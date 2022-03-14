# 치킨 배달 | 삼성전자 SW 역량테스트 | 난이도★1.5
## 내답안________________________________________
# 콤비네이션 https://ourcstory.tistory.com/414
# 틀린이유: 각 집과 치킨거리가 최소가 되기만 하면 그 값을 구해서 더했다. 하지만 모든 집에대한 치킨거리를 합한게 최소가 되어야하지, 각각 집마다의 최소 치킨거리를 더하면 선택된 치킨집 조합도 제각각이기때문에 문제가 의도한 것이 아니다. 틀림. 
# from itertools import combinations

# n, m = map(int, input().split())
# data = [] # 지도
# chicken = [] # 치킨집 좌표(r, c)
# city_chicken_d = 0 # 도시의 치킨거리

# for i in range(n):
#   data.append(list(map(int, input().split())))
  
# for i in range(n):
#   for j in range(n):
#     if data[i][j] == 2:
#       chicken.append((i,j))

# # 전체 치킨집 중 M개의 치킨집을 뽑는 조합
# chicken_combinations = list(combinations(chicken,m))

# for i in range(n):
#   for j in range(n):
#     if data[i][j] == 1:
#       chicken_d = 999 # 집마다 초기화
#       # 모든 조합에 대한 치킨거리 중 최소 치킨거리를 도시의 치킨거리에 더함
#       # 여러 조합중 하나의 조합 선택
#       for ck in chicken_combinations:
#         # 하나의 조합에서 치킨집 하나씩 반복해서 가져옴
#         for k in range(len(ck)):
#           #print(ck[k][0], ck[k][1])
#           d = abs(i - ck[k][0])+ abs(j - ck[k][1])
#           chicken_d = min(chicken_d, d)

#       city_chicken_d += chicken_d

# print(city_chicken_d)

## 답안예시1. ___________________________________________________
from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []
for r in range(n):
  data = list(map(int, input().split()))
  for c in range(n):
    if data[c] == 1:
      house.append((r,c)) # 집
    elif data[c] == 2:
      chicken.append((r,c)) # 치킨 집

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합
candidates = list(combinations(chicken, m))

# 치킨 거리의 합을 계산하는 함수
# 치킨집 m개의 좌표들(하나의 조합)이 인자로 들어옴
def get_sum(candidate): 
  result = 0
  # 모든 집에 대하여
  for hx, hy in house:
    # 가장 가까운 집 찾기
    temp = 1e9
    for cx, cy in candidate:
      temp = min(temp, abs(hx-cx) + abs(hy-cy))
    # 가장 가까운 치킨집까지의 거리 더하기
    result += temp

  return result

# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
  # 모든 치킨집 조합에 대해 값을 구하고 그 중 최솟값으로 결정
  result = min(result, get_sum(candidate))

print(result)