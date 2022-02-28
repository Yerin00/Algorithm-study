# 시각

## 답안예시1. 
# 3중 for문을 돌아도 괜찮은 문제다. 시간은 전체 경우의 수가 작고 제한시간이 2초이기때문.

# 어떻게 계산하는거지..?
# 전체 경우의 수 = 24 x 60 x 60

n = int(input())

result = 0
for h in range(n+1):
  for m in range(60):
    for s in range(60):
      if "3" in str(h) or "3" in str(m) or "3" in str(s):
        result += 1

print(result)


## 오답노트_____________________________________________

# for h in range(n+1):
#   if "3" in str(h):
#     result += (3600-h)
#     continue
#   for m in range(60):
#     if "3" in str(m):
#       result += (60-m)
#       continue
#     for s in range(60):
#       if "3" in str(s):
#         result += 1

# print(result)


## 내 답안_____________________________________________# 03,13,23: xx : xx(3이 안들어간 경우)
# 3 x (60 x 60 - 1800)

# 분, 초에 3이 들어가는 경우 = xx:__:__
# 0~59중에 3 포함된 경우 03,13,23,43,53(5개), 30~39(10개) = 15개
# 15 x 60 + 60 x 15 = 1800

# .. 아니 근데 이건 코딩문제가 아니고 내가 수학..ㅋㅋㅋㅎ 문제를 푸는거잖아..