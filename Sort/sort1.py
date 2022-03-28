# 위에서 아래로 | T 기업 코딩 테스트 | 난이도 ★
'''
수열을 내림차순으로 정렬하는 프로그램을 만드시오.
'''

n = int(input())
data = []
for i in range(n):
  data.append(int(input()))

# 파이썬 기본 정렬 라이브러리
data.sort(reverse=True)

for i in range(len(data)):
  print(data[i], end=' ')