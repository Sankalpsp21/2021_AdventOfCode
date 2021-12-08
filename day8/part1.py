with open('Seven.txt') as f:
    data = f.readlines()
    data = [x.strip().split('|') for x in data]
    data = [[x.split() for x in y]for y in data]

print(data)

sum = 0

for line in data:
    for value in line[1]:
        if len(value) == 2 or len(value) == 4 or len(value) == 3 or len(value) == 7:
            sum += 1

print(sum)