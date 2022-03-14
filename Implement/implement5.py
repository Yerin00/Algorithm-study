# 럭키 스트레이트 | 핵심유형(백준) | 난이도★
## 내 답안
# 반복문보다는 슬라이싱과 sum이 더 빠르다
n = list(map(int, input()))

# 전체 길이의 왼쪽 오른쪽 각자릿수의 합비교

left = n[:len(n)//2]
right = n[len(n)//2:]

lsum = sum(left)
rsum = sum(right)

if lsum == rsum:
  print("LUCKY")
else:
  print("READY")

# 답안예시1._________________________________________________
# n = input()
# length = len(n)
# summary = 0

# for i in range(length // 2):
#   summary += int(n[i])

# for i in range(length // 2, length):
#   summary -= int(n[i])

# if summary == 0:
#   print("LUCKY")
# else:
#   print("READY")