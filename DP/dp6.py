# 금광 | flipkart 인터뷰 | 난이도 1.5
'''
첫번째 열의 아무 행에서나 출발하여 오른쪽 열 위, 옆, 아래으로 이동합니다.
최종적으로 얻을 수 있는 최대 금값을 출력하시오.

테스트 케이스가 T개 주어집니다.
'''

## 답안예시_________________________________________________
'''
왼쪽에서 온다고 생각하고 코드를 짬. dp가 2차원임.
'''
for tc in range(int(input())):
  n, m = map(int, input().split())
  array = list(map(int, input().split())) # array에 입력받고나서 2차원 배열 dp를 따로 생성해서 사용하기 편하게함

  # 2차원 DP 테이블 초기화
  dp = []
  index = 0
  for i in range(n):
    dp.append(array[index:index+m])
    index += m

  # 다이나믹 프로그래밍 진행
  for j in range(1, m):
    for i in range(n):
      # 왼쪽 위에서 오는 경우
      if i == 0: # 현재 위치가 제일 윗 줄인 경우 왼쪽 위에서 오는 경우 없음
        left_up = 0
      else:
        left_up = dp[i - 1][j - 1]
      # 왼쪽 아래에서 오는 경우
      if i == n - 1: # 마지막 줄이면 왼쪽 아래에서 오는 경우 없음
        left_down = 0
      else:
        left_down = dp[i + 1][j - 1]
      # 왼쪽에서 오는 경우
      left = dp[i][j - 1]
      
      dp[i][j] = dp[i][j] + max(left_up, left_down, left)

  result = 0
  for i in range(n):
    result = max(result, dp[i][m - 1]) # 제일 오른쪽 값들중 최댓값을 출력한다.

  print(result)
  
      
    
## 내 답안___________________________________________________
'''
오른쪽열 중에 제일 큰거 다 갈수 있는게 아니다.
오른쪽 열의 위, 옆, 아래 칸으로만 이동가능함. 그렇기 때문에
★이전의 선택이 이후에 영향을 미침.
'''
t = int(input())

# def dp():
#   n, m = map(int, input().split())
#   array = list(map(int, input().split()))
#   d = [0] * 20

#   # 첫번째 열중에서 가장 큰 값에서 시작한다.
#   d[0] = array[0]
#   for i in range(1, n):
#     d[0] = max(d[0], array[i * m])
    
#   for i in range(1, m): # 가로로 이동하니까 열만큼 반복한다.
#     d[i] = d[i - 1]
#     for j in range(n):
#       d[i] = max(d[i] ,d[i - 1] + array[j * m + i])
      
#   return d[m - 1]

# for _ in range(t):
#   print(dp())

