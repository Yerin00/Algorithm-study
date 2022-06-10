# 문자열 압축 | 난이도 2 | 2020 카카오 신입 공채
'''
같은 값이 연속해서 나타나는 것 -> 문자의 개수와 반복되는 값으로 표현
예) aabbaccc -> 2a2ba3c
하지만 반복되는 문자가 적은 경우 압축이 거의 안됨. 이러한 단점을 해결하기위해 문자열을 1개이상의 단위로 잘라서 압축하는 방법을 찾으려고한다.
예) ababcdcdababcdcd의 경우
1. 2개씩 잘라서 압축 -> 2ab2cd2ab2cd
2. 8개씩 잘라서 압축 -> 2ababcdcd(제일 짧음)

1개 이상의 단위로 문자열을 잘라 압축하여 표현한 문자열중
가장 짧은 것의 길이를 return하는 함수 solution을 완성하라.

- s (1 <= s <= 1000)
- 알파벳 소문자로만 이루어짐
'''
def solution(s):
  answer = len(s)

  for step in range(1, len(s) // 2 + 1):
    compressed = ""
    count = 1

    for j in range(step, len(s), step):
      if prev == s[j:j+step]:
        count += 1
      else:
        compressed += str(count) + prev if count >= 2 else prev
        prev = s[j:j+step]
        count = 1
      compressed += str(count) + prev if count >= 2 else prev
      answer = min(anser, len(compressed))
  return answer

# 아... 1개짜리로 자르는것밖에 생각을 못했네.._________________
# s = input()
# result = 0
# min_value = 1e9
# for i in range(1, len(s)):
#   count = 1 # 중복되는 수
#   for j in range(len(s) - 1): # 처음부터 확인
#     if s[j] == s[j+1]: # 같으면 count 1증가
#       count += 1
#     else: # 다르면 result에 값 넣어주기
#       result += 1 # 문자 -> result 1 증가
#       if count == 1: # count가 1이면 생략
#         pass
#       elif count >= 10: # count가 두자릿수면 result 2 증가
#         result += 2
#       elif count >= 100:
#         result += 3
#       elif count >= 1000:
#         result += 4
#       else:
#         result += 1
#       count = 1 # count 초기화
  
#   min_value = min(min_value, result) # result중에서 제일 작은 값 저장

# print(min_value)

    
        
