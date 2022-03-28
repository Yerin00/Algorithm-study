# 안테나 | 2019 SW 마에스트로 입학 테스트 | 난이도 ★
'''
안테나와 모든 집의 거리 합이 최소가 되도록 안테나 하나를 설치하시오.
안테나는 집이 있는 곳에만 설치할 수 있습니다.
'''

# 집의 수
n = int(input())
data = list(map(int, input().split()))


# 답안예시________________________________________
'''
정렬한 뒤 중간값만 출력하면됨. 이게 무조건 성립하는구나.. 신기하다
'''

data.sort()
print(data[(n-1) // 2])


# 내 답안________________________정렬문제인지 모르고 푼다면 이렇게 풀듯

# min_index = 0
# min = 1e9
# data.sort()

# for i in data:
#   sum = 0
#   for j in data:
#     sum += abs(j - i)
#   if sum < min:
#     min = sum
#     min_index = i

# print(min_index)