# 문자열 압축 | 2020 카카오 신입 공채 | 난이도 ★1.5
# ababcdcd/ababcdcd ->2ababcdcd

def solution(s):
    answer = len(s) # 최악의 경우

    # 1~len(s)/2 까지 완전탐색
    for step in range(1, len(s) // 2 + 1):
      compressed = ""
      prev = s[0:step] # ★슬라이싱
      count = 1

      # 단위 크기만큼 증가시키며 이전 문자열과 비교
      for j in range(step, len(s), step):
        # 이전과 동일하면 압축횟수(count) 증가
        if prev == s[j:j+step]:
          count += 1
        # 다른 문자열 나옴
        else:
          # count에 str() 처리해서 문자열에 포함시키는게 정석. count가 두자릿수 이상인 경우에 숫자도 두자리로 계산되어야하기때문에 12ab면 1,2,a,b 로 문자열의 길이가 4이다.
          compressed += str(count) + prev if count >= 2 else prev # 1이면 생략 가능
          # 초기화
          prev = s[j:j+step]
          count = 1
      # 남아있는 문자열 처리
      compressed += str(count) + prev if count >= 2 else prev
      # 만들어지는 압축 문자열이 가장 짧은 것이 정답
      answer = min(answer, len(compressed))

    return answer

data = "aaaaaaaaaaaabcd"
print(solution(data))