# 연산자 끼워넣기 | 삼성전자 SW 역량테스트 | 난이도 ★★
'''
주어진 수들에 연산자의 위치에 따른 결과값중 최대, 최소를 출력하라
'''

## 답안예시____________________________________________
n = int(input())
numbers = list(map(int, input().split())) # N개의 수
add, sub, mul, div = list(map(int, input().split())) # 각 연산자의 수 +, -, x, //

# 1e9 == 1,000,000,000
min_value = 1e9
max_value = -1e9

def dfs(i, now):
  global min_value, max_value, add, sub, mul, div  
  # i는 지금 몇번째 연산자인지 나타냄, 처음에 1로 시작함
  if i == n:
    # ★주어진 n-1개의 연산자 모두 사용했으면 비교 후 값 넣기
    min_value = min(min_value, now)
    max_value = max(max_value, now)
  else:
    # ★now에 계산한 값을 넣지않고 그냥 재귀 함수의 매개변수로 넘겨줌으로써 재귀함수에서 나온 뒤 계산했던 값을 다시 되돌릴필요 없다.
    if add > 0:
      add -= 1
      dfs(i+1, now + numbers[i])
      add += 1
    if sub > 0:
      sub -= 1
      dfs(i+1, now - numbers[i])
      sub += 1
    if mul > 0:
      mul -= 1
      dfs(i+1, now * numbers[i])
      mul += 1
    if div > 0:
      div -= 1
      dfs(i+1, int(now / numbers[i])) # 나눌때는 나머지를 제거
      div += 1
    
dfs(1, numbers[0])

print("max:",max_value, "min:", min_value)
