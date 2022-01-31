from collections import deque
from typing import Any

class Queue(object):
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, data: Any) -> None:
        self.queue.append(data)

    def dequeue(self) -> Any:
        if self.queue:
            return self.queue.pop(0)

if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.queue)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.queue)
    
    dq = deque()
    dq.append(1)
    dq.append(2)
    dq.append(3)
    dq.append(4)
    print(dq)
    print(dq.popleft())
    print(dq.popleft())
    print(dq.popleft())
    print(dq.popleft())