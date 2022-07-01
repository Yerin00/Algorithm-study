# 외벽점검 | 2020 카카오 신입공채 1차 | 난이도★★★
'''
레스토랑의 구조는 동그란 모양이고 외벽의 총 둘레는 n미터이다.
외벽의 몇몇 지점은 취약지점들이 있다.
주기적으로 친구들을 보내 점검을 하기로 했으며 점검시간을 1시간으로 제한했다.
친구들이 한시간동안 이동할 수 있는 거리는 제각각이며 최소한의 친구를 투입해
점검을 완료하고자 한다.
레스토랑의 정북 방향을 0으로 나타내며 취약지점의 위치는 정북 방향으로부터 시계방향으로 떨어진 거리로 나타낸다.
친구들은 출발지점부터 시계 혹은 반시계 방향으로 외벽을 따라서만 이동한다.

외벽의 길이 n, 취약지점의 위치 배열 weak, 각 친구가 1시간동안 이동할 수 있는 거리 배열 dist가 주어질때
점검을 위해 보내야하는 친구의 수 최솟값을 return 하도록 solution함술르 완성하라.

친구를 모두 투입해도 전부 점검할 수 없는 경우에는 -1을 return하라.
'''
from itertools import permutations

def solution(n, weak, dist):
  length = len(weak)
  for i in range(length):
    weak.append(weak[i] + n) # 길이를 2배로 늘려준다.
  answer = len(dist) + 1 # 투입할 친구의 최솟값을 찾아야함

  # weak[0 ~ length - 1]까지를 각각 시작점으로 설정
  for start in range(length):
    # 친구를 나열하는 모든 경우의 수에 대하여 확인
    for friends in list(permutations(dist, len(dist))):
      count = 1 # 투입할 친구의 수
      # 해당 친구가 점검할 수 있는 마지막 위치
      position = weak[start] + friends[count - 1]
      # 시작점부터 모든 취약 지점을 확인
      for index in range(start, start + length): 
        # 점검할 수 있는 위치를 벗어나는 경우
        if position < weak[index]:
          count += 1 # 새로운 친구 투입
          if count > len(dist): # 더 투입이 불가능 하다면
            break
          position = weak[index] + friends[count - 1]
      answer = min(answer, count) # 최솟값 계산
      
  if answer > len(dist):
    return -1
  
  return answer