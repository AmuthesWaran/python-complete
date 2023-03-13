# FIFO - First In - First Out
from collections import deque


queue = deque([])


queue.append(1)
queue.append(2)
queue.append(3)

queue.popleft()
print(queue)
if not queue:
    print("empty")

# for q in queue:
#     if not queue:
#         print("empty")
#     queue.popleft()
