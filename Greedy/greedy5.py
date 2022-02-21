# 모험가 길드 | 핵심유형 | 난이도 ★
n = int(input())
player = list(map(int, input().split()))


## 답안예시1.
result = 0 # 그룹 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in player:
  count += 1
  if count >= i:
    result += 1 # 그룹수 추가
    count = 0 # 모험가수 초기화

print(result)



## 내 답안_____________________________________________________
# 문제를 잘못 이해함.. 헐.. 마을에 남아도 되는구나(꼭 모든 모험가가 그룹에 포함되어야할 필요X, 문제 명시)
# 뒤에서부터(공포도 큰 순서로) 그룹에 포함시킬 인원 수 만큼 빼기

# result = 0 # 최대 그룹 수
# remain = n
# player.sort()

# i = 0
# while True:
#   if remain < player[n-1-i]:
#     break
#   remain = remain - player[n-1-i]
#   i += player[n-1-i]
#   result += 1

print(result)


