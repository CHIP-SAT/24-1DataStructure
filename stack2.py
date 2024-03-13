import sys

n = int(input(""))
stack = []

for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "1":
        stack.append(cmd[1])

    if cmd[0] == "2":
        if not stack:
            print(-1)
        else:
            print(stack.pop())

    if cmd[0] == "3":
        print(len(stack))

    if cmd[0] == "4":
        if not stack:
            print(1)
        else:
            print(0)
            
    if cmd[0] == "5":
        if not stack:
            print(-1)
        else:
            print(stack[-1])


