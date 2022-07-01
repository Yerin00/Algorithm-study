# 로또 | 백준
'''
https://www.acmicpc.net/problem/6603
독일 로또는 {1, 2,..., 49}에서 6개의 수를 고른다.
로또 번호를 선택하는데 사용되는 가장 유명한 전략은 49가지 수 중 k개(k>6)의 수를 골라 집합 S를 만든 다음 그 수만 가지고 번호를 선택하는 것이다.

k와 집합 S가 주어졌을 때, 수를 고르는 모든 방법을 구하는 프로그램을 작성하시오.

7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0
'''
def dfs(depth, pos):
  if depth == 6: # 6개를 다 뽑았으면 출력
    print(*case)
    return 0
  for i in range(pos, k):
    case.append(data[i])
    dfs(depth + 1, i + 1)
    case.pop()

while True:
  data = list(map(int, input().split()))
  k = data.pop(0)
  # pop을 사용해 0번 인덱스 값을 제거함과 동시에 종료조건 확인, k= data[0] set_s = data[1:] 따로 슬라이싱 할 필요x
  if k == 0: 
    break
  case = []
  dfs(0, 0)
  print()



# 방법2 조합 이용___________________________________
# from itertools import combinations
# import sys
# input=sys.stdin.readline

# while 1:
#     arr = input().split()

#     if arr.pop(0) == '0':
#         break

#     for i in combinations(arr, 6):
#         print(" ".join(i))

#     print()
