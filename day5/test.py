with open('test.txt') as f:
    data = [x.strip() for x in f]

lines = [x.split(" -> ") for x in data]
lines = [[x.split(',') for x in y] for y in lines]
lines = [[[int(x) for x in y] for y in z] for z in lines]

print(lines)

# Creating a 1000x1000 2D Array full of 0s
map = []

for i in range(10):
    row = []
    for j in range(10):
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

    elif y1 == y2: #Checking to see if the line is horizontal
        if x1 < x2:
            for i in range(x1, x2 + 1):
                map[y1][i] += 1
        elif x2 < x1:
            for i in range(x2, x1 + 1):
                map[y1][i] += 1
    else:
        counter = 0

        if x1 < x2 and y1 < y2:
            for i in range(y1, y2 + 1):
                map[i][x1 + counter] += 1
                counter += 1

        elif x2 < x1 and y1 < y2:
            for i in range(y1, y2 + 1):
                map[i][x1 - counter] += 1
                counter += 1

        elif x1 < x2 and y2 < y1:
            for i in range(x1, x2 + 1):
                map[y1 - counter][i] += 1
                counter += 1
        else:
            for i in range(x2, x1 + 1):
                map[y2 + counter][i] += 1
                counter += 1


for line in lines:
    plot(line, map)

danger = 0

for i in range(10):
    for j in range(10):
        if map[i][j] > 1:
            danger += 1

for row in map:
    print(row)


print(danger)