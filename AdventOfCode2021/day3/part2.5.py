with open("BinaryDiagnostic.txt", 'r') as f:
    data2 = f.readlines()
    data2 = [x.strip() for x in data2]

for i in range(len(data2[0])):
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

print(data2)
co = data2[0]

co = int(co, 2)
print(co)
