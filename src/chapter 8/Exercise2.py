with open("file.txt") as fhand:
    count = 0
    for line in fhand:
        words = line.split()
        # print("Debug", words)
        if len(words) < 3 : continue
        if words[0] != "From"  : continue
        print(words[2])