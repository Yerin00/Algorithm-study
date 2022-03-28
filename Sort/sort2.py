# 성적이 낮은 순서로 학생 출력하기 | D 기업 프로그래밍 콘테스트 예선 | 난이도 ★
n = int(input())
data = []
for i in range(n):
  name, score = input().split()
  data.append((name, int(score))) # 점수는 int로 변환한 후 저장

'''
★sorted(), key, 람다식 사용
https://kingofbackend.tistory.com/98
'''

data = sorted(data, key= lambda student: student[1])

for i in data:
  print(i[0], end=' ')