with open("file.txt", "r") as f:
    # print(f.readline())
    for line in f.readlines():
        print(line)
