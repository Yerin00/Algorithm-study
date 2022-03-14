# 재귀함수(recursion function) 자기자신을 다시 호출하는 함수

# 자기자신 무한 호출
# def recursive_function():
#   print('재귀 함수를 호출합니다.')
#   recursive_function()

# recursive_function()

# 종료조건
# def recursive_function(i):
#   # 100번째 출력에 종료
#   if i == 100:
#     return
#   print(i, '번째 재귀 함수에서',i+1,'번째 재귀 함수를 호출합니다.')
#   recursive_function(i+1)
#   print(i, '번째 재귀 함수를 종료합니다.')

# recursive_function(1)


# 두가지 방식으로 구현한 팩토리얼
def factorial_iterative(n):
  result = 1
  # 1부터 차례대로 곱하기
  for i in range(1,n+1):
    result *= i
  return result

# 재귀적으로 구현
def factorial_recursive2(n):
  result = 1
  if n == 0:
    return
  factorial_recursive2(n-1)
  return result *= n

def factorial_recursive(n):
  if n<=1:
    return 1
  return n * factorial_recursive(n-1)

print('반복:', factorial_iterative(5))
print('재귀:', factorial_recursive(5))
print('재귀2:', factorial_recursive2(5))