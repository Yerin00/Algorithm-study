# 볼링공 고르기 | 2019 SW 마에스트로 입학 테스트 | 난이도★
'''
A, B 두사람이 볼링을 치는데 두 사림이 서로 다른 무게의 볼링공을 고르려고 한다. 볼링공은 총 N개가 있으며 공의 번호는 1번부터 부여된다.
같은 무게의 공이 여러개 있을 수 있지만 서로 다른 공으로 간주한다.
볼링공의 무게는 1~M까지의 자연수
이때 두 사람이 고를 수 있는 볼링공 번호 조합의 경우의 수를 출력하라.

* 조합이므로 (1, 2)와 (2, 1)은 같은 경우로 간주한다.
'''
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 볼링공 무게별 개수
count = [0] * (n + 1)
for i in data: # 1~
  count[i] += 1

result = 0
for i in range(len(count) - 1): # 공의 번호는 1번부터이므로 0번을 제외
  result += count[i] * sum(count[i + 1:]) # 자기번호 이후의 공과 경

print(result)