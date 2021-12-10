with open('Syntax.txt') as f:
    data = [list(x.strip()) for x in f.readlines()]


corrupted = []

for line in data:
    priority = []

    for x in line:
        if x in ['[', '{', '(', '<']:
            priority.append(x)

        elif x == ']' and priority[-1] == '[':
            priority.pop()

        elif x == '}' and priority[-1] == '{':
            priority.pop()

        elif x == ')' and priority[-1] == '(':
            priority.pop()

        elif x == '>' and priority[-1] == '<':
            priority.pop()

        else:
            corrupted.append(x)
            break

total = 0

for x in corrupted:
    if x == ')':
        total += 3
    elif x == ']':
        total += 57
    elif x == '}':
        total += 1197
    else:
        total += 25137


print(total)
