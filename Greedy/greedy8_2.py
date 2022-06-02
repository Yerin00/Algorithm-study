# 만들 수 없는 금액 | 난이도 ★ | K 대회 기출
'''
동전 N개를 가지고 만들수 없는 양의 정수 금액 중 최솟값을 구하시오.
N = 5, 3,2,1,1,9원이라고 가정하면 최솟값은 8원입니다.
'''
n = int(input())
data = list(map(int, input().split()))
data.sort() # 오름차순 정렬

target = 1
for x in data:
  if target < x:
    break
  target += x

print(target)