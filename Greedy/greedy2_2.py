# 큰수의 법칙 | 2019 국가 교육기관 코딩 테스트 | 난이도 ★
'''
주어진 수를 M번 더하여 가장 큰 수를 만드는 법칙
배열의 크기 N, 숫자가 더해지는 횟수 M, 연속해서 더해질 수 있는 횟수 K

만들 수 있는 가장 큰 수를 출력하라
'''
# 내 답안

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
result = 0

data.sort(reverse = True)
while m > 0: # 굳이 조건 안주고 True: 로 해도됨
  # 제일 큰 값을 연속해서 K번 더해주기
  for i in range(k):
    if m == 0:
      break
    result += data[0]
    m -= 1
  # 두번째로 큰 값 더해주기
  if m == 0:
    break
  result += data[1]
  m -= 1
    
print(result)