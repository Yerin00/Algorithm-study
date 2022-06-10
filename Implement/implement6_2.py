# 문자열 재정렬 | Facebook 인터뷰
'''
알파벳 대문자와 숫자(0~9)로만 이루어진 문자열이 있다.
이때 모든 알파벳을 오름차순으로 정렬하여 출력한 뒤 그 뒤에 모든 숫자를 더한 값을 이어서 출력한다.
'''
s = input()
result = []
sum = 0
for i in range(len(s)):
  if ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z'):
    result.append(s[i])
  else:
    sum += int(s[i])

result.sort()
result.append(str(sum))

print(''.join(result))