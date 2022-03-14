# 기둥과 보 설치 | 2020 카카오 신입 공채 | 난이도★1.5
'''
- 기둥 : 바닥 or 보의 한쪽 끝부분 위 or 또 다른 기둥 위
- 보: 한쪽 끝부분 기둥 위 or 양쪽 끝부분이 다른 보와 동시에 연결

[x좌표, y좌표, 구조물 종류, 설치/삭제]
- 0: 기둥/ 1: 보
- 0: 삭제/ 1: 설치

결과물을 return함. 규칙에 만족하지않는 명령은 실행하지않는다.
'''

# 조건에 만족하는 지 확인
def check():
  # 기둥
  if type == 0:
    # 바닥 or 왼쪽에 보 or 오른쪽에 보 or 기둥 위
    if y == 0 or wall[x-1][y] == 1 or wall[x][y] == 1 or wall[x][y-1] = 0:
      return True
    else:
      return False
  # 보
  else:
    if :
      return True
    else:
      return False

def add(x, y, type):
  # 기둥이면
  if type == 0:
    wall[x][y] = 0 # 기둥 추가
    return [x, y, wall[x][y]]    
  # 보면
  else:
    wall[x][y] = 1 # 보 추가
    return [x, y, wall[x][y]]
    
    
def remove(x, y, type):


def solution(n, build_frame):
  # N x N 2차원 리스트 -> 0 기둥/1 보/2 아무것도 없음
  wall = [[2]* n for _ in range(n)]
  # 명령을 하나씩 실행
  for build in build_frame:
    x, y = build[0], build[1] # x, y좌표
    type = build[2] # 기둥 or 보
    work = build[3] # 삭제 or 설치
    # 삭제하기
    if work == 0:

    # 설치하기
    elif work == 1:
      # 일단 설치한 뒤 성공이면 두고
      add(x, y, type)
      if check() == True: # 추가성공
      # 조건 불충족이면 다시 삭제
      else:
        remove(x, y, type)

  
  answer = [[]]
  # x,y,type 순으로 오름차순 정렬
  answer.sort()  
  return answer


n = 5
build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]

solution(n, build_frame)