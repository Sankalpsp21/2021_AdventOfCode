with open("Dive.txt", 'r') as f:
    data = f.readlines()
    data = [x.split() for x in data]

    depth = 0
    forward = 0
    aim = 0

    for i in data:
        if(i[0] == "forward"):
            forward += int(i[1])
            depth += aim*int(i[1])

        elif(i[0] == "down"):
            aim += int(i[1])

        elif (i[0] == "up"):
            aim -= int(i[1])

    print(depth*forward)