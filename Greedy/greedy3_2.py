# 숫자 카드 게임 | 2019 국가 교육기관 코딩 테스트 | 난이도 ★
'''
여러 개의 숫자 카드중 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
- N X M 행렬
- 행을 선택한 후 그 행에 있는 카드 중 가장 낮은 카드를 뽑는다.
'''
n, m = map(int, input().split())

result = 0
for i in range(n):
  data = list(map(int, input().split()))
  min_value = min(data)
  if result < min_value:
    result = min_value

print(result)