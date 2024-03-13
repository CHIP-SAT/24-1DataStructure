import sys

stack = []
commands = list(map(lambda a: a.replace("\n", "").split(" "), sys.stdin.readlines()))
for i in range(1, len(commands)):
    commands[i]
    if commands[i][0] == "1":
        stack.append(commands[i][1])
    elif commands[i][0] == "2":
        if stack:
            print(stack.pop(-1))
        else:
            print(-1)
    elif commands[i][0] == "3":
        print(len(stack))
    elif commands[i][0] == "4":
        print(int(not stack))
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)
