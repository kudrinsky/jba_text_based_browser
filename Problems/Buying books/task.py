from collections import deque

actions = int(input())
stack = deque()
output = ''
for _i in range(actions):
    action = input().split(' ', 1)
    if action[0] == 'BUY':
        stack.append(action[1])
    elif action[0] == 'READ':
        output += stack.pop() + '\n'
print(output)
