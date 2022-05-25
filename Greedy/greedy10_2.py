# 무지의 먹방 라이브 | 난이도 ★ | 2019 카카오 신입 공채
'''
음식이 1번~N번까지 회전판위에 있다.
1번음식부터 1초씩 회전판이 돌아가면서 섭취하게된다.
음식 먹기시작하고 K초뒤에 잠시 방송이 중단되었을때 몇번음식부터 먹으면 되는지 return하는 solution함수를 작성하라.

- food_times 음식먹는데 걸리는 시간의 배열
- K 방송이 중단된 시간
더 섭취해야할 음식이 없다면 -1을 반환합니다.

'''
def solution(food_times, k):
    length = len(food_times)
    if sum(food_times) <= k:
        return -1
    index = 0
    for _ in range(k):
        while food_times[index] == 0:
            index = (index + 1) % length # 다 먹은 음식이면 다음 음식으로 넘어가기
        food_times[index] -= 1
    
    answer = (index + 2) % length # 번호가 1~N이기때문에 1을 마지막에 한번 더해줌, 그리고 마지막으로 먹은 것의 다음 걸 먹기때문에 1을 또 더해줘야함
    return answer

food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))

'''
위 코드로 일부는 정답이지만 몇몇 문제는 실패로 뜨고 시간초과가 난다.
'''
