# 모험가 길드 | 난이도 ★ | 핵심유형
'''
모험가 N명
각 모험가 마다 공포도가 존재하고 공포도가 X인 모험가는 최소 X명 이상으로 구성한
모험가 그룹에 참여해야 여행을 떠날 수 있다.

최대 몇개의 그룹을 만들 수 있는지 출력
'''

n = int(input())
data = list(map(int, input().split()))
data.sort()

group = 0 # 그룹수
count = 0 # 현재 그룹의 모험가 수
for i in data:
  count += 1
  if count >= i:
    result += 1
    count =0

print(group)