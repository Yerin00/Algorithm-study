# 상하좌우
## 내 답안
n = int(input())
move = input().split()
move_type = ['L', 'R', 'U', 'D'] #y-1, y+1, x-1, x+1
x, y = 1, 1
tempx, tempy = 1, 1

for m in move:
  # 일단 변경한 뒤에
  if m == 'L': tempy -= 1
  elif m == 'R': tempy += 1
  elif m == 'U': tempx -= 1
  elif m == 'D': tempx += 1

  if tempx < 1 or tempy < 1 or tempx > n or tempy > n:
    tempx, tempy = x, y # 조건 만족x -> 롤백
  x, y = tempx, tempy # x, y에 적용

print(x, y)