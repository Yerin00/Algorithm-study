# 무지의 먹방 라이브 | 2019 카카오 신입 공채 | 난이도★
# 제공 코드
# def solution(food_times, k):
#     answer = 0
#     return answer
'''
왜 그리디로 푸는지 이해가 안됐었는데 예시를 보니 알겠다.
[8, 6, 4], K = 15 일때
회전판이 돌면서 모든 음식을 1초동안 먹음. 일단 한번에 많이 뻬야 O(K) 보다는 빠르게 처리할 수 있다.

15 - (먹는데 걸리는 시간이 제일 짧은 시간) x (len(food_times))를 하면 일단
한 음식이 빌때까지는 같은 동작(세개의 음식에서 1씩 반복적으로 빼는 것)을 하기때문에 한번에 뺄수있게되며 이는 시간을 많이 절약할 수 있게된다.
이때까지 문제가 이해가 안됐던 점은 15 - 4 x 3을 하는데 이 3이 뜻하는게 무엇인지, 왜 이걸 빼는지 잘 몰랐기때문이었다.

# sum_value + (현재 음식을 다 먹는 시간 = 현재의 음식시간 - 이전 음식시간) * 현재 음식 개수와 k 비교
이 계산이 이해가 잘 안됐었는데 예시를 보고나서 이해가됐다.
1단계로 15 - 4x3 = 3초가 남았다.
2단계로 이제 6초가 걸리는 2번 음식을 먼저 비울 것인데 앞서 1단계를 거치면서
1씩 4번 빼기 연산을 했기때문에 실제로 2번 음식을 다 먹는데에 남은 시간은 6-4 = 2초이다.

'''
## 답안예시1.
import heapq

def solution(food_times, k):
  if sum(food_times) <= k:
    return -1

  q = []
  for i in range(len(food_times)):
    heapq.heappush(q, (food_times[i], i + 1))
  sum_value = 0 # 먹기위해 사용한 시간
  previous = 0 # 직전에 다 먹은 음식시간

  length = len(food_times)

  # sum_value + (현재 남은 음식을 다 먹는 시간 = 현재의 음식시간 - 이전 음식시간) * 현재 음식 개수와 k 비교
  while sum_value + ((q[0][0] - previous) * length) <= k:
    now = heapq.heappop(q)[0]
    sum_value += (now - previous) * length
    length -= 1 # 다먹은 음식 제외
    previous = now # 이전 음식시간 재설정

  # 남은 음식 중에서 몇번째 음식인지 확인하여 출력
  result = sorted(q, key = lambda x: x[1]) # 음식번호 기준으로 정렬
  return result[(k - sum_value) % length][1]



