string = input()
stack = []

if string.index(')') < string.index('(') or string.count('(') != string.count(')'):
    print('ERROR')
else:
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')' and len(stack) > 0:
            stack.pop()

    print('OK' if len(stack) == 0 else 'ERROR')
