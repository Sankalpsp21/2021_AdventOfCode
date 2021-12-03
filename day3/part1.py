with open("BinaryDiagnostic.txt", 'r') as f:
    data = f.readlines()
    data = [x.strip() for x in data]

    print(data)

gamma = ""
epsilon = ""
for i in range(len(data[0])):
    zero = 0
    one = 0
    for line in data:
        if line[i] == '0':
            zero += 1
        else:
            one += 1

    if one > zero:
        gamma += '1'
    else:
        gamma += '0'

for j in gamma:
    if j == '1':
        epsilon += '0'
    else:
        epsilon += '1'

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma)
print(epsilon)
print(gamma*epsilon)


