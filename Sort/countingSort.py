# 계수 정렬
'''
범위 좁고 중복값이 많은 경우에 유리한 정렬방법
'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
  count[array[i]] += 1 # 각 데이터에 해당하는 인덱스 값 증가

for i in range(len(count)):
  for j in range(count[i]):
    print(i, end=' ') # 등장 횟수만큼 인덱스 출력