
def main():
    with open("SonarSweep.txt", 'r') as f:
        data = f.readlines()
        data = [int(x.strip()) for x in data]

    count = 0
    prev = -1000000000

    for i in range(1, len(data)-1):

        if data[i-1] + data[i] + data[i+1] > prev:
            count += 1

        prev = data[i-1] + data[i] + data[i+1]

    print(count, "jyg")





if __name__ == "__main__":
    main()