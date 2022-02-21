# 곱하기 혹은 더하기 | Facebook 인터뷰 | 난이도★
## 내 답안. 오...거의 똑같다..
data = list(input()) # list() 없어도 문자열은 자동으로 한 자씩 들어가는 구나
result=0

for i in data:
  num = int(i)
  if result <= 1 or num <= 1:
    result += num
  else:
    result *= num

print("result:",result)

## 답안예시1.
# data = input()
# result=int(data[0])

# for i in range(1, len(data)):
#   num = int(data[i])
#   if result <= 1 or num <= 1:
#     result += num
#   else:
#     result *= num

# print("result:",result)
