# 큐(queue) 선입선출(FIFO)
from collections import deque

# 큐 생성
queue = deque()

# 삽입
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)

# 삭제
queue.popleft()

print(queue) # 들어온 순서대로 출력
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 순서대로 출력