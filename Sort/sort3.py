# 두 배열의 원소 교체 | 국제 알고리즘 대회 | 난이도 ★
'''
A, B 두 배열의 값을 바꿔치기해서 A의 합이 최대가 되도록 하라
'''
n, k = map(int, input().split())
a, b = [], []

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else:
    break

print(sum(a))

  