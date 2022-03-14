# 문자열 재정렬 | Facebook 인터뷰 | 난이도★
## 내 답안
n = input()
str = []
sum = 0

for i in range(len(n)):
  # 대문자 알파벳이면 리스트에 추가
  if ord("A") <= ord(n[i]):
    str.append(n[i])
  # 숫자면 sum에 더하기
  else:
    sum += int(n[i])

str.sort()
for i in range(len(str)):
  print(str[i],end='') # 문자열은 따로 출력하되, end를 추가해줘야함
print(sum)

## 답안예시1.________________________________________________
data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
  if x.isalpha(): # ★isalpha()를 쓰면 간단하게 체크할 수 있다.
    result.append(x)
  else:
    value += int(x)

result.sort()

# 숫자를 따로 출력하지않고 문자열끝에 추가해서 같이 출력
if value != 0:
  result.append(str(value))

# ★하나씩 출력안해도 되네..
print(''.join(result))