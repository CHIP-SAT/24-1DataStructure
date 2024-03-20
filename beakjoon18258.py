import sys
from collections import deque

command_cycle = int(input())
queue = deque([], maxlen=command_cycle)

for i in range(command_cycle):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        queue.append(command[1])
    elif command[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        print(int(not queue))
    elif command[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:
        if queue:

            print(queue[-1])
        else:
            print(-1)
