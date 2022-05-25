# 신입사원 | ICPC
'''
신입사원을 채용할 때 서류심사성적과 면접시험성적의 순위 중 적어도 하나가 다른 지원자보다 떨어지지않는 자만 선발한다. 즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다. 뽑을 수 있는 신입사원의 최대인원 수를 구하는 프로그램을 작성하시오.

테스트 케이스의 개수 T
지원자의 숫자 N
N줄에 걸쳐 각 지원자의 서류심사 성적, 면접 성적 순위
※ 성적은 모두 동석차없이 결정된다.

https://www.acmicpc.net/problem/1946


'''
import sys

# 테스트 케이스의 수를 입력받고 그만큼 반복한다.
for _ in range(int(input())):
  n = int(sys.stdin.readline()) # 지원자의 수
  data = []
  count = 1 # 순위가 1위인 지원자는 무조건 뽑기때문에 1로 초기화
  for i in range(n):
    a, b = map(int, sys.stdin.readline().split()) # 서류순위, 면접순위
    data.append([a, b])

  data.sort() # 서류순위로 오름차순 정렬 <- 순위는 숫자가 작을수록 좋음.
  min_value = data[0][1]

  for i in range(1, n):
    if min_value > data[i][1]:
      count += 1
      min_value = data[i][1]

  print(count)
  
 