# 멀티탭 스케줄링
'''
[예시]
예를 들어 3 구(구멍이 세 개 달린) 멀티탭을 쓸 때, 전기용품의 사용 순서가 아래와 같이 주어진다면, 

1키보드
2헤어드라이기
3핸드폰 충전기
4디지털 카메라 충전기
5키보드
6헤어드라이기

키보드, 헤어드라이기, 핸드폰 충전기의 플러그를 순서대로 멀티탭에 꽂은 다음 디지털 카메라 충전기 플러그를 꽂기 전에 핸드폰충전기 플러그를 빼는 것이 최적일 것이므로 플러그는 한 번만 빼면 된다. 
멀티탭 구멍의 개수 N(<=100)과 전기용품의 총 사용횟수 K(<=100)가 정수로 주어진다.
전기용품의 이름이 K이하의 자연수로 사용 순서대로 주어진다.
하나씩 플러그를 빼는 최소의 횟수를 출력하시오.
'''

n, k = map(int, input().split())
data = list(map(int, input().split()))

# 멀티탭
multitap = [] # 초기화

result = 0 # 멀티탭에서 뺀 횟수

for i in range(len(data)):
  # 멀티탭에 이미 꽂혀있으면 다음 반복문으로 이동
  if data[i] in multitap:
    continue
  # 멀티탭 비어있으면 무조건 꽂는다.
  if len(multitap) < 2:
   multitap.append(data[i])
  else:
    for j in range(i + 1, len(data)):
      if data[j] == multitap[0]:
        multitap[1] = data[i] # 새로운 값 넣기
        result += 1
        break
      elif data[j] == multitap[1]:
        multitap[0] = data[i] # 새로운 값 넣기
        result += 1
        break
      if multitap[0] != data[i] and multitap[1] != data[i]:
        multitap[0] = data[i]
        result += 1
  
print(result)

#______________________________________________________________
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

multitap = list(map(int, input().split()))

plugs = []
count = 0

for i in range(K):
  # 있으면 건너 뛴다.
  if multitap[i] in plugs:
    continue
  
  # 플러그가 1개라도 비어 있으면 집어넣는다.
  if len(plugs) < N:
    plugs.append(multitap[i])
    continue
  
  multitap_idxs = [] # 다음 멀티탭의 값을 저장.
  hasplug = True

  for j in range(N):
  	# 멀티탭 안에 플러그 값이 있다면
    if plugs[j] in multitap[i:]:
      # 멀티탭 인덱스 위치 값 가져오기.
      multitap_idx = multitap[i:].index(plugs[j])
    else:
      multitap_idx = 101
      hasplug = False

    # 인덱스에 값을 넣어준다.
    multitap_idxs.append(multitap_idx)
    
    # 없다면 종료
    if not hasplug:
      break
  
  # 플러그를 뽑는다.
  plug_out = multitap_idxs.index(max(multitap_idxs))
  del plugs[plug_out] # 플러그에서 제거
  plugs.append(multitap[i]) # 플러그에 멀티탭 값 삽입
  count += 1 # 뽑았으므로 1 증가

print(count)