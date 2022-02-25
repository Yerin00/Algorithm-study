# 만들 수 없는 금액
n = int(input())
data = list(map(int, input().split()))

## 답안예시1. 
# 앗 쉬 이해했다.
#  [1, 5, 9] : x
# 1 2(2<5 => break), 2를 만들수 있는지 확인할 차례인데 2보다 큰 녀석이 나왔으니..2는 만들수 없다.

data.sort()
target = 1
for x in data:
  # 만들 수 없는 금액 찾았을 때 반복 종료
  if target < x:
    break
  target += x

print(target)
    