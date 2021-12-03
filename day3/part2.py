with open("BinaryDiagnostic.txt", 'r') as f:
    data = f.readlines()
    data = [x.strip() for x in data]
    data2 = [x.strip() for x in data]

for i in range(len(data[0])): #This chunk finds the Oxygen number
    zero = 0
    one = 0
    valToMatch = 0
    linesToRemove = []

    for line in range(len(data)):
        if data[line][i] == '0':
            zero += 1
        else:
            one += 1

    if zero > one:
        valToMatch = 0
    else:
        valToMatch = 1

    for line in range(len(data)):
        if int(data[line][i]) != valToMatch:
            linesToRemove.append(data[line])

    for line in linesToRemove:
        data.remove(line)

for i in range(len(data2[0])): # This chunk finds the CO2 number
    if len(data2) == 1:
        break

    zero = 0
    one = 0
    valToMatch = 0
    linesToRemove = []

    for line in range(len(data2)):
        if data2[line][i] == '0':
            zero += 1
        else:
            one += 1

    if zero <= one:
        valToMatch = 0
    else:
        valToMatch = 1

    for line in range(len(data2)):
        if int(data2[line][i]) != valToMatch:
            linesToRemove.append(data2[line])

    for line in linesToRemove:
        data2.remove(line)

ox = data[0]
co = data2[0]
ox2 = int(ox, 2)
co2 = int(co, 2)

print("Oxygen: ", ox, ox2)
print("CO2: ", co, co2)

