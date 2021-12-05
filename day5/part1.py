with open('Hydrothermal.txt') as f:
    data = [x.strip() for x in f]

lines = [x.split(" -> ") for x in data]
lines = [[x.split(',') for x in y] for y in lines]
lines = [[[int(x) for x in y] for y in z] for z in lines]

print(lines)

# Creating a 1000x1000 2D Array full of 0s
map = []

for i in range(1000):
    row = []
    for j in range(1000):
        row.append(0)

    map.append(row)


def plot(line, map):
    x1 = line[0][0]
    y1 = line[0][1]
    x2 = line[1][0]
    y2 = line[1][1]

    if x1 == x2: #Checking to see if the line is vertical
        if y1 < y2:
            for i in range(y1, y2 + 1):
                map[i][x1] += 1
        elif y2 < y1:
            for i in range(y2, y1 + 1):
                map[i][x1] += 1

    if y1 == y2: #Checking to see if the line is horizontal
        if x1 < x2:
            for i in range(x1, x2 + 1):
                map[y1][i] += 1
        elif y2 > y1:
            for i in range(y2, y1 + 1):
                map[y1][i] += 1


for line in lines:
    plot(line, map)

danger = 0

for i in range(1000):
    for j in range(1000):
        if map[i][j] > 1:
            danger += 1

print(danger)