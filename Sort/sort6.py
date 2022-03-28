# 실패율 | 2019 카카오 신입 공채 1차 | 난이도 ★
'''
입력
N :스테이지 수
stages: 사용자가 멈춰있는 스테이지
N+1인 경우 -> 끝까지 클리어

실패율 높은 스테이지부터 내림차순으로 리턴
'''
## 답안예시_____________________________________________
def solution(N, stages):
  answer = []
  length = len(stages)

  # 스테이지 번호를 1부터 증가시키며
  for i in range(1, N + 1):
    # 해당 스테이지에 머물러 있는 사람의 수 계산
    count = stages.count(i) # count()★

    # 실패율 계산
    if length == 0:
      fail = 0
    else:
      fail = count / length

    # 리스트에 (스테이지 번호, 실패율) 삽입
    answer.append((i, fail))
    length -= count
  # 실패율 기준으로 내림차순 정렬
  answer = sorted(answer, key=lambda t:t[1], reverse=True)

  # 정렬된 스테이지 번호 출력
  answer = [i[0] for i in answer]
  return answer
    

## 내 답안_______________________________________________
# def solution(N, stages):
#     # 실패율 내림차순으로 번호를 나열함
#     answer = []
#     challenger = [0] * (N + 2)
#     fail = [0] * (N + 2) # 범위 0 ~ N+1 => 1~N단계, N+1은 올클리어
#     fail_rate = []
  
#     # 도전 실패 후 머물러 있는 플레이어 수 
#     for i in stages:
#       fail[i] += 1

#     # 각 레벨마다 도전한 플레이어 수 구하기
#     ## 방법 1. 완전 탐색- 레벨 1부터 N까지 다 돌면서 확인함
#     for level in range(1, N + 1):
#       for i in stages:
#         if i >= level:
#           challenger[level] += 1        
#     # 실패율
#     for level in range(1, N + 1):
#       if challenger[level] == 0:
#         fail_rate[level] = 0
#         continue
#       fail_rate[level] = ((fail[level] / challenger[level]), level) # index out of range??
    
#     fail_rate = sorted(fail_rate, key= lambda x: x[0], reverse=True)
#     for i in fail_rate:
#       answer.append(i[1])
      
#     return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N, stages))



# 그냥 참고_______________________________________________________
## 내가 생각했던 플레이어수 구하는 다른 방법.. 근데 더 복잡해짐
    ## 방법 2. 내림차순으로 정렬한 뒤 값이 바뀔 때 인덱스 = 도전자의 수
    # stages.sort(reverse=True)
    # for i in range(len(stages)-1):
    #   a = stages[i]
    #   b = stages[i+1]
    #   if i != len(stages) - 2: # 마지막 루프가 아닐때
    #     if a > b: # 값이 달라지면 그때 i+1이 a 레벨의 도전자 수가 된다.
    #       challenger[stages[i]] = i + 1
    #   else: # 마지막 루프일 때, 마지막값 처리를 해줘야함
    #     if a > b: # 값이 달라지면
    #       challenger[stages[i]] = i + 1
    #       challenger[stages[i+1]] = i + 2
    #     elif a == b: # 값이 안 달라지면
    #       challenger[stages[i]] = i + 2

## 나민언니 코드__________________________________________________
# def solution(N, stages):
#     answer = []
#     #거꾸로 정렬
#     stages=sorted(stages,reverse=True)
#     #print(stages)
#     #초기화
#     fail_rate_list=[]
#     #단 모두 성공한? 값이 N+1인 것도 포함하기 위해 크기 N+2로
#     fail=[0 for _ in range(N+2)]
#     do=[0 for _ in range(N+2)]

    
#     for index,value in enumerate(stages):
#         #해당 스테이지에서 실패=> 실패+1
#         fail[value]+=1
#         #해당 스테이지의 index+1까지 도전한 사람
#         do[value]=index+1
#         """ex) [6,5,4,3,3,2,2,2,1]에서 3까지 도전한 사람은 5명
#                 ->3인 마지막 index+1=4+1
#         """
#     #실패율 계산하고 (index,실패율)리스트에 추가
#     for j in range(1,N+1):
#         #단 0으로 나누는 것은 오류이므로 확인하기!
#         if do[j]!=0:
#             fail_rate_list.append((j,fail[j]/do[j]))
#         else:
#             fail_rate_list.append((j,0))
#     #print(fail_rate_list)
#     #실패율로 거꾸로 정렬
#     fail_rate_list.sort(key= lambda x:x[1],reverse=True)
#     #정렬된 리스트를 순서대로 인덱스를 넣기
#     for i in fail_rate_list:
#         answer.append(i[0])
#     return answer

# """
# #solution
#     length=len(stages)
#     for i in range(1,N+1):
#         count=stages.count(i)
#         if length==0:
#             fail=0
#         else:
#             fail=count/length
#         answer.append((i,fail))
#         length-=count
        
#     return answer
# """