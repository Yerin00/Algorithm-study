# OX 퀴즈
'''
https://www.acmicpc.net/problem/8958

"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.

"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

첫째줄에는 테스트케이스의 개수가 주어진다.
'''
for _ in range(int(input())):
  data = input()
  score = 0 # 총 점수
  score_now = 0 # 현재 문제의 점수
  for i in data:
    if i == 'X':
      score_now = 0
    else:
      score_now += 1
      score += score_now
      
  print(score)
  
  
