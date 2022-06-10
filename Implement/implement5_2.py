# 럭키 스트레이트 | 핵심유형 | 난이도 1 
'''
게임 캐릭터의 필살기인 '럭키 스트레이트' 기술은 특정 조건을 만족할 때만 사용가능하다.
- 조건: 캐릭터의 점수를 N이라고할 때, 점수 N을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더하면 동일한 상황

현재 점수가 주어질 때 사용가능한지 여부를 사용할수 있으면 LUCKY, 사용할 수 없으면 READY로 출력하라.
(자릿수는 항상 짝수)
'''
n = list(map(int, input()))
center = len(n) // 2
left = sum(n[:center])
right = sum(n[center:])
if left == right:
  print("LUCKY")
else:
  print("READY")