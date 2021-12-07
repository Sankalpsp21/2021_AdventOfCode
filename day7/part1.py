with open('Whale.txt') as f:
    data = f.readline().strip().split(',')
    data = list(map(int, data))

data.sort()
mid = data[int(len(data) / 2)] #Getting the median horizontal position

fuel = 0

for crab in data:
    fuel += abs(crab - mid)

print(fuel)