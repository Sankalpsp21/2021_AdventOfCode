with open('Seven.txt') as f:
    data = f.readlines()
    data = [x.strip().split('|') for x in data]
    data = [[x.split() for x in y] for y in data]


# Identify the letters associated with 1 and 4

# Since every other number has a unique number of shared sides with
# those numbers, use the number of shared letters to deduce the number

def intersect(a, b):
    # 0, 6 and 9 are length 6
    # 2, 3, and 5 are length 5

    return sum(1 for x in a if x in b)  # Counts the number of shared "sides" between 2 numbers


total = 0

for line in data:
    num = ""
    one = ""
    four = ""
    a = line[0]
    b = line[1]

    for x in a + b:
        if len(x) == 2:
            one = x

        elif len(x) == 4:
            four = x

    for value in b:
        if len(value) == 2:
            num += '1'
        elif len(value) == 4:
            num += '4'
        elif len(value) == 3:
            num += '7'
        elif len(value) == 7:
            num += '8'
        elif len(value) == 5:
            if intersect(value, one) == 2:
                num += '3'
            elif intersect(value, four) == 3:
                num += '5'
            else:
                num += '2'

        elif len(value) == 6:
            if intersect(value, one) == 1:
                num += '6'
            elif intersect(value, four) == 4:
                num += '9'
            else:
                num += '0'

    total += int(num)

print(total)
