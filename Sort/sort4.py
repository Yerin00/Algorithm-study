# 국영수 | 핵심유형 | 난이도 ★

'''
1. 국어 내림차순
2. 영어 오름차순
3. 수학 내림차순
4. 이름 알파벳 오름차순
'''

#n = int(input())
#data = []
data = [
  ('Junkyu', 50, 60, 100),
  ('Sangkeun', 80, 60, 50),
  ('Sunyoung', 80, 70, 100)
]

# for i in range(n):
#   # 다 str으로 받기
#   data.append(input().split())

  
# 국어, 영어, 수학, 이름: str에는 -가 안먹는듯?
data = sorted(data, key = lambda student: (-int(student[1]), int(student[2]), -int(student[3]), student[0]))

for student in data:
  print(student[0])