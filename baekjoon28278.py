import sys

stack = []
command_cycle = int(input())
for i in range(command_cycle):
    command = sys.stdin.readline().split(" ")
    command[-1] = command[-1].replace("\n", "")
    if command[0] == "1":
        stack.append(command[1])
    elif command[0] == "2":
        if stack:
            print(stack.pop(-1))
        else:
            print(-1)
    elif command[0] == "3":
        print(len(stack))
    elif command[0] == "4":
        print(int(not stack))
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)
