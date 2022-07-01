# 촌수계산
'''
https://www.acmicpc.net/problem/2644
부모와 자식 : 1촌
여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.

사람들은 1~n의 번호로 표시된다.
- 사람의 수 n
- 촌수를 계산해야하는 서로 다른 두 사람의 번호
- 부모 자식 관계의 개수 m
- 부모 자식 관계 x, y(부모, 자식)
- 각 사람의 부모는 최대 한명만 주어진다.

두 사람이 어떤 관계도 없는 경우에는 -1을 출력한다.
'''


## 답안예시_______________________________________
import sys
sys.setrecursionlimit(300000)

def dfs(node):
    for n in graph[node]:
        if check[n] == 0:
            check[n] = check[node]+1
            dfs(n)
            
n = int(input())
graph = [[] for _ in range(n+1)]
s, e = map(int, input().split())
for _ in range(int(input())):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
check = [0]*(n+1)
dfs(s)
print(check[e] if check[e] > 0 else -1)





## 오답____________________
'''
전형적인 DFS문제인데 DFS 알고리즘에 대해 숙지가 안되어서 DFS개념과 BFS개념을 섞어서 풀다보니 이상하게 꼬인 것 같다.
'''
# import sys
# sys.setrecursionlimit(300000)

# n = int(input())
# a, b = map(int, input().split())
# m = int(input())
# graph = [[0] * (n + 1) for _ in range(n + 1)]
# for i in range(m):
#   x, y = map(int, input().split())
#   graph[x][y] = 1 # 부모, 자식 관계가 존재
#   graph[y][x] = 1

# def dfs(k, dist): # 촌수
#   # 종료조건
#   if graph[k][b] == 1 or graph[b][k] == 1: # k와 b가 부모 혹은 자식 관계라면
#     print(dist)
#     return 0
#   for i in range(1, n + 1): # k가 i의 부모라면
#     if graph[k][i] == 1:
#       dfs(i, dist + 1)
#       graph[k][i] = 2 # 방문처리
#       graph[i][k] = 2
#     elif graph[i][k] == 1: # i가 k의 부모라면
#       dfs(i, dist + 1)
#       graph[i][k] = 2 # 방문처리
#       graph[k][i] = 2
#   return -1

# result = dfs(a, 0)
# if result == -1:
#   print(result)