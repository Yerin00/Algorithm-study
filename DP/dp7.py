# 정수 삼각형 | IOI 1994년도 | 난이도 1.5
'''
삼각형 꼭대기에서 아래로 내려가며 하나씩 선택해 더할때 최댓값을 구하시오.
대각선 왼쪽 아래 혹은 오른쪽 아래만 가능.

★금광문제와 비슷하게 풀면 된다.
'''

n = int(input()) # 삼각형의 크기 n
dp = []
for _ in range(n):
  dp.append(list(map(int,input().split())))

temp1, temp2 = 0, 0 # 초기화 안해주면 정의 안되어있다고함
for i in range(1, n): # 두번째 줄부터 시작
  for j in range(i + 1):
    # 왼쪽 끝값이 아니면
    if j != 0:
      # 대각선 왼쪽 위에서 오는 경우
      temp1 = max(dp[i][j], dp[i][j] + dp[i-1][j-1])
    # j가 오른쪽 끝값이 아니면
    if j != i:
      # 대각선 오른쪽 위에서 오는 경우
      temp2 = max(dp[i][j], dp[i][j] + dp[i-1][j])
      
      '''
      if문 두개 다 도는 경우에는 이미 위의 if문에서 dp값이 증가됐는데 증가된 dp값에 또 더해서 값이 이상해지는구나.. 점화식에서 dp[i][j]를 사용하는 경우에는 주의하자!
      '''
    dp[i][j] = max(temp1, temp2) # dp값이 변하는 것을 막기위해 임시변수 temp1,2에 저장한 뒤 값을 비교해서 큰 값을 dp에 최종적으로 적용시켰다.

print(max(dp[n-1]))
'''
치명적인 실수로 틀리긴 했지만 알고리즘 자체는 거의 맞았다! 휴 오래고민한 보람이 있다.
'''

## 답안예시_____________________________________________________________

n = int(input()) # 삼각형의 크기 n
dp = []
for _ in range(n):
  dp.append(list(map(int,input().split())))

for i in range(1, n):
  for j in range(i + 1):
    # 왼쪽 위에서 내려오는 경우
    if j == 0:
      up_left = 0
    else:
      up_left = dp[i - 1][j - 1]
    # 바로 위에서 내려오는 경우
    if j == i:
      up = 0
    else:
      up = dp[i - 1][j]

    dp[i][j] = dp[i][j] + max(up_left, up)

print(max(dp[n - 1]))