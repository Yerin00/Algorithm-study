# 문자열 뒤집기 | 난이도 ★ | 핵심유형
'''
0과1로만 이루어진 문자열 S,
연속된 하나 이상의 숫자를 잡고 모두 뒤집어서 모든 숫자를 같게 만들려고합니다.
이때 다솜이가 해야하는 행동의 최소 횟수를 출력하세요.
'''
data = input()
# 0과 1로 이루어진 그룹의 개수

count = [0, 0]
previous = int(data[0]) # 이전 값
count[previous] = 1
for i in range(1, len(data)):
  if int(data[i]) != previous:
    previous = int(data[i])
    count[previous] += 1

result = min(count[0], count[1])
print(result)
  
  