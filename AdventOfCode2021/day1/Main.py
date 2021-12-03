
def main():
    with open("SonarSweep.txt", 'r') as f:
        data = f.readlines()
        data = [int(x.strip()) for x in data]

    count = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            count += 1

    print(count)





if __name__ == "__main__":
    main()