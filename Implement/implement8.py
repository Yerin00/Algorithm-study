# 자물쇠와 열쇠 | 2020 카카오 신입 공채 | 난이도★1.5


# 시계방향 90도 회전★
def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]  # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result


# def rotate_a_matrix_by_90_degree(a):
#   for i in range(len(key)):
#     # [::-1] 처음부터 끝까지 역순으로
#     # zip([],[],[])와 같다. 여러개의 인자가 전달된 것. zip()은 여러 인자에서 값을 하나씩 가져와 짝을 지어 pairs를 만들어준다.
#     rotate = [k[::-1] for k in zip(*key)]
#     print(rotate)


# 자물쇠의 중간이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):  # 중간 범위
        for j in range(lock_length, lock_length * 2):  # 중간 범위
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
  n = len(lock)
  m = len(key)

  # 자물쇠의 크기를 기존의 3배로 변환
  new_lock = [[0]*(n*3) for _ in range(n*3)]
  # 새로운 자물쇠의 중앙에 기존 자물쇠 넣기
  for i in range(n):
    for j in range(n):
      new_lock[i+n][j+n] = lock[i][j]

  # 4가지 방향 확인
  for rotation in range(4):
    key = rotate_a_matrix_by_90_degree(key) # 열쇠 회전
    for x in range(n*2):
      for y in range(n*2):
        # 자물쇠 끼워넣기
        for i in range(m):
          for j in range(m):
            new_lock[x+i][y+j] += key[i][j]
        # 맞는지 확인
        if check(new_lock) == True:
          return True
        # 안맞으면 자물쇠에서 열쇠빼기
        for i in range(m):
          for j in range(m):
            new_lock[x+i][y+j] -= key[i][j]

  return False
