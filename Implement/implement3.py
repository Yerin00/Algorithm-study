# 왕실의 나이트 | 실전문제 | 난이도★
## 내 답안
pos = list(input())
x = ord(pos[0]) - 96 # ord("a") -> 97 아스키 코드 숫자로 바꿔주는 함수
y = int(pos[1])
print(x, y)

result = 0
tempx, tempy = 1, 2 # 더해줄 숫자
x_, y_ = x, y # 비교용 x, y

for i in range(2):
  # ++
  x_ = x + tempx
  y_ = y + tempy
  if 1 <= x_ and x_ <= 8 and 1 <= y_ and y_ <= 8:
    result += 1 # 경우의수 1 증가
    print("++result", result)
    
  # +-
  x_ = x + tempx
  y_ = y - tempy
  if 1 <= x_ and x_ <= 8 and 1 <= y_ and y_ <= 8:
    result += 1 # 경우의수 1 증가
    print("+-result", result)
    
  # -+
  x_ = x - tempx
  y_ = y + tempy
  if 1 <= x_ and x_ <= 8 and 1 <= y_ and y_ <= 8:
    result += 1 # 경우의수 1 증가
    print("-+result", result)
    
  # --
  x_ = x - tempx
  y_ = y - tempy
  if 1 <= x_ and x_ <= 8 and 1 <= y_ and y_ <= 8:
    result += 1 # 경우의수 1 증가
    print("--result", result)
    
  tempx, tempy = 2, 1 # x, y값 바꾸기

  
print(result)

