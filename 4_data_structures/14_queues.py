from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)  # deque([1, 2, 3])

# Remove first item
first = queue.popleft()
print(first)  # 1

if not queue:
    print("Queue is empty")
