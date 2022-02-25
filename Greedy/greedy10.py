# 무지의 먹방 라이브 | 2019 카카오 신입 공채 | 난이도★
# 제공 코드
# def solution(food_times, k):
#     answer = 0
#     return answer

## 답안예시1.
# 음식을 많이 끝내는게 좋다고 조건에 표시된 것도 아닌데 왜 적은거 순으로
# 먹는 건지 잘 이해가 안된다. 그냥 1번부터 순서대로 먹는게 아니었나..




## 오답노트________________________________
def solution(food_times, k):
    answer = 0
    while k < 0:
      for i in range(len(food_times)):
        if food_times[i] != 0:
          food_times[i] -= 1
          k -= 1
          answer = i + 1
      
    return answer

