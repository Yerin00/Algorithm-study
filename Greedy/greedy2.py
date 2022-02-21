# 큰 수의 법칙

# n(2 <= N <= 1000), m(1<= M <=10000), k(1<= K <=10000)
# N개의 숫자들 중 M개를 뽑아 더해 가장 큰수를 구하는데, 같은 인덱스의 수는 K번 연속해서 더할 수 있다.
# 단, K는 M보다 작거나 같다.

# 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
sum = 0

data.sort() # sort(reverse=True)

## 답안 예시1. 무식하게 찾기________________________________________
while True:
    for i in range(k):
        if (m == 0):
            break
        sum += data[n - 1]
        m -= 1
    if m == 0:
        break
    sum += data[n - 2]
    m -= 1

print(sum)

## 답안 예시2. 패턴 찾기 [hint: (k+1)개씩 반복됨]___________________
# 가장 큰 수가 더해지는 횟수
# count1 = (m // (k+1)) * k
# count1 += m % (k+1)
# # 두번째로 큰 수가 더해지는 횟수
# count2 = m // (k+1)
# # 큰수의 합
# sum = data[n-1] * count1 + data[n-2] * count2
# print(sum)

## 오답노트__________________________________________________
# sum=0
# index = 0
# count = m
# data.sort()

# while count != 0:
#     if count - k >= 0:
#         sum += data[index] * k
#         count -= k
#         index= abs(index-1)
#     else:
#         sum += data[0] * count
#         count -= count

# print("큰 수의 합: ",sum)
