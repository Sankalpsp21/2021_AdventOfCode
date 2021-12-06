with open('Lanternfish.txt', 'r') as f:
    data = f.readline().strip().split(',')
    data = list(map(int, data))
    # the map() function applies the int() function to every value in the list

print(data)

# keeps track of how many fish are in each stage of life
buckets = [0 for _ in range(10)]

for fish_life in data:
    buckets[fish_life] += 1

total_days = 256
for day in range(total_days):
    for idx, count in enumerate(buckets):
        # Enumerate simultaneously gives you indexes and values from a list, Super useful!
        if idx == 0:
            # we use 7 because the enumerate will decrease it to 6 in the current iter.
            buckets[7] += count
            buckets[9] += count
            buckets[idx] = 0
        else:
            buckets[idx - 1] += count
            buckets[idx] = 0

print(sum(buckets))
