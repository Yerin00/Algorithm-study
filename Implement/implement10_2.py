# 기둥과 보 설치 | 2020 카카오 신입 공채 | 난이도★1.5
'''
https://programmers.co.kr/learn/courses/30/lessons/60061

- 기둥 : 바닥 or 보의 한쪽 끝부분 위 or 또 다른 기둥 위
- 보: 한쪽 끝부분 기둥 위 or 양쪽 끝부분이 다른 보와 동시에 연결

[x좌표, y좌표, 구조물 종류, 설치/삭제]
- 0: 기둥/ 1: 보
- 0: 삭제/ 1: 설치

결과물을 return함. 규칙에 만족하지않는 명령은 실행하지않는다.
'''
# 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
def possible(answer):
  for x, y, stuff in answer:
    if stuff == 0: # '기둥'이면
      # 바닥 위 / 보의 한쪽 끝부분 위 / 다른 기둥 위 라면 정상
      if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
        continue
      return False # 아니라면 False 반환
    elif stuff == 1: # '보'면
      # 한쪽 끝부분 기둥 위 / 양쪽 끝부분이 다른 보와 동시에 연결
      if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
        continue
      return False # 아니라면 False 반환
    return True
      

# solution 함수 구현
def solution(n, build_frame):
  answer = []
  for frame in build_frame:
    x, y, stuff, operate = frame
    if operate == 0: # 삭제하는 경우
      answer.remove([x, y, stuff]) # 일단 삭제
      if not possible(answer): # 가능한 구조물이 아니면
        answer.append([x, y, stuff]) # 다시 설치
    if operate == 1: # 설치하는 경우
      answer.append([x, y, stuff]) # 일단 설치
      if not possible(answer): # 가능한 구조물이 아니면
        answer.remove([x, y, stuff]) # 제거
  return sorted(answer)
  