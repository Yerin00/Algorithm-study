# 괄호 변환 | 난이도 ★ | 2020 카카오 신입 공채 1차
'''
재귀, DFS로 풀면 될 것 같음. 마지막에 다 완료한 뒤에 처음에 나눴던 u를 앞에 붙여서 반환한다.
즉 멀리있는 것부터 탐색하고 처음으로 돌아와서 끝나는 DFS에 적절한 문제
1. u, v로 문자열을 나눔(u는 더이상 균형잡힌 문자열로 나뉘지않는다.)
'''
## 내 답안___________________________________________________________________
# 더이상 쪼개지지않는 균형잡힌 문자열 분리: (, ) 개수 동일
def valance(p):
  sum = 0
  for i in range(len(p)):
    if p[i] == '(':
      sum += 1
    elif p[i] == ')':
      sum -= 1
    if sum == 0: # 괄호를 열기도 전에 닫은게 더 많다면 올바르지x
      return i

        
    
# 올바른 문자열 : 개수 동일, 짝도 맞음
def proper(p):
  sum = 0
  for i in range(len(p)):
    if p[i] == '(':
      sum += 1
    elif p[i] == ')':
      sum -= 1
    if sum < 0: # 괄호를 열기도 전에 닫은게 더 많다면 올바르지x
      return False
  # 반복문을 모두 돌고 나온 뒤 (,) 개수 동일한지 확인
  if sum == 0:
    return True
  
# 균형잡힌 괄호 문자열을 올바른 괄호 문자열로 변환하는 함수
def solution(p):
    answer = p
    # 입력이 빈문자열이면 반환
    if p == "":
      return answer
    # u, v로 나눔
    index = valance(p)
    u = p[:index + 1] # 0 ~ index
    v = p[index + 1:] # index + 1 ~ end
    
    # u가 올바른 괄호 문자열이면, v에 대해 재귀적 수행
    if proper(u) == True:
      new_p = solution(v)
      return u + new_p
    # u가 올바른 괄호 문자열이 아니면
    else: # 이어 붙이기= ( +  v에 대한 재귀수행 결과 + ) + u처리
      # u 앞뒤 문자 제거후 괄호 방향 뒤집기
      for i in range(len(u)):
        if u[i] == '(':
          u[i] = ')'
        elif u[i] == ')':
          u[i] = '('
      answer = '(' + solution(v) + ')' + u
      return answer

data = "()))((()" # result : ()(())()
print(solution(data))


## 답안예시________________________________________________________
# 더이상 쪼개지지않는 균형잡힌 문자열 분리: (, ) 개수 동일
def balanced_index(p):
  count = 0 # 왼쪽 괄호의 개수
  for i in range(len(p)):
    if p[i] == '(':
      count += 1
    else:
      count -= 1
    if count == 0: # 괄호를 열기도 전에 닫은게 더 많다면 올바르지x
      return i

        
# 올바른 문자열 : 개수 동일, 짝도 맞음
def check_proper(p):
  count = 0
  for i in p:
    if i == '(':
      count += 1
    else:
      if count == 0: # 쌍이 맞지않는 경우
        return False
      count -= 1
  return True
    
  
# 균형잡힌 괄호 문자열을 올바른 괄호 문자열로 변환하는 함수
def solution(p):
    answer = ''
    # 입력이 빈문자열이면 반환
    if p == '':
      return answer
    # u, v로 나눔
    index = balanced_index(p)
    u = p[:index + 1] # 0 ~ index
    v = p[index + 1:] # index + 1 ~ end
    
    # u가 올바른 괄호 문자열이면, v에 대해 재귀적 수행
    if check_proper(u) == True:
      answer =  u + solution(v)
    # u가 올바른 괄호 문자열이 아니면
    else: # 이어 붙이기= ( +  v에 대한 재귀수행 결과 + ) + u처리
      answer = '('
      answer += solution(v)
      answer += ')'
      # u 앞뒤 문자 제거후 괄호 방향 뒤집기
      u = list(u[1:-1])
      for i in range(len(u)):
        if u[i] == '(':
          u[i] = ')'
        else:
          u[i] = '('
      answer += "".join(u)
    return answer # 마지막에 return, return위치가 족므 헷갈린다..

data = "()))((()" # result : ()(())()
print(solution(data))