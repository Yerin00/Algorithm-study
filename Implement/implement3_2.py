# 왕실의 나이트 | 실전문제 | 난이도
'''
8X8 좌표평면, 나이트는 L자 형태로만 이동할 수 있다.
1. 수평으로 두칸 이동한 뒤 수직으로 한 칸 이동하기
2. 수직으로 두칸 이동한 뒤 수평으로 한 칸 이동하기

나이트가 이동할 수 있는 경우의 수를 출력하라.
행은 1~8
열은 a~h 로 표현한다.

<입출력>
a1 -> 2
'''

# ord()를 알아두자
data = input()
x = int(data[1]) # 행
y = int(ord(data[0])) - int(ord('a')) + 1 # 열


dx = [-1, 1, -1, 1]
dy = [1, 1, -1, -1]

result = 0 # 경우의 수
for i in range(4):
  next_x = x + 2 * dx[i]
  next_y = y + dy[i]
  if next_x <= 8 and 1<= next_x and next_y <= 8 and 1 <= next_y:
    result += 1
  next_x = x + dx[i]
  next_y = y + 2 * dy[i]
  if next_x <= 8 and 1<= next_x and next_y <= 8 and 1 <= next_y:
    result += 1

print(result)
    
    
  

