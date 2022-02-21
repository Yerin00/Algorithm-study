# 문자열 뒤집기 | 핵심유형 | 난이도★

## 내 답안, 소요시간: 10분__________________________
data = input()
count = [0, 0]

cur = int(data[0])
count[cur] += 1

for i in range(1, len(data)):
    num = int(data[i])
    if cur != num:
        count[num] += 1
        cur = num

result = min(count[0], count[1])
print(result)

## 답안예시1.________________________________________

# data = input()
# count0 = 0
# count1 = 0

# if data[0] == '1':
#     count0 += 1  #..?왜 count0에 더하지
# else:
#     count1 += 1

# for i in range(len(data) - 1):
#     if data[i] != data[i + 1]:
#         if data[i + 1] == '1':
#             count0 += 1
#         else:
#             count1 += 1

# print(min(count0, count1))
