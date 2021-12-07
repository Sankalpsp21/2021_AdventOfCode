with open('Whale.txt') as f:
    data = f.readline().strip().split(',')
    data = list(map(int, data))

data.sort()
total = sum(data)
avg = int(total / len(data))  # Getting the average horizontal position

fuel = 0

for crab in data:
    distance = abs(crab - avg)
    i = 1
    for x in range(distance):
        fuel += i
        i += 1

print(fuel)
