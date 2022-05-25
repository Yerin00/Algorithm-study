# 곱하기 혹은 더하기 | 난이도 ★ | Facebook 인터뷰
'''
각자리가 0~9로 이루어진 문자열 S,
왼쪽부터 오른쪽까지 하나씩 모든 숫자를 확인하며 x혹은+연산자를 넣어
결과적으로 만들수있는 가장 큰 수를 구하시오.
단 모든 연산은 x, + 상관없이 왼쪽부터 이루어집니다.
'''
s = input() # 문자열 입력받기
result = int(s[0])
for i in range(1, len(s)):
  num = int(s[i])
  if num <= 1 or result <= 1:
    result += num
  else:
    result *= num
