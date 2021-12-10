with open('Syntax.txt') as f:
    data = [list(x.strip()) for x in f.readlines()]

corrupted = []
corruptedLines = []

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
            corruptedLines.append(line)
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

for line in corruptedLines:
    data.remove(line)

print("Part 1:", total)


# Part 2

def calcScore(extension):
    score = 0

    for l in extension:
        score *= 5

        if l == '(':
            score += 1
        elif l == '[':
            score += 2
        elif l == '{':
            score += 3
        else:
            score += 4

    return score


scores = []
for line in data:
    priority = []
    extension = ""

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

    if len(priority) > 0:
        for i in reversed(priority):
            extension += i

    score = calcScore(extension)
    scores.append(score)

scores.sort()
mid = scores[int(len(scores)/2)]
print("Part 2:", mid)