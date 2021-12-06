with open('Lanternfish.txt') as f:
    data = [x.strip() for x in f]
    data = data[0].split(',')
    data = [int(x) for x in data]

print(data)

for i in range(256):

    fishToAdd = []

    for fish in range(len(data)):
        if data[fish] > 0:
            data[fish] -= 1

        elif data[fish] == 0:
            data[fish] = 6
            fishToAdd.append(8)

    for fish in fishToAdd:
        data.append(fish)


print(len(data))

