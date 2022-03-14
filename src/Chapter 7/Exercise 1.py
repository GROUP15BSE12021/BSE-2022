with open("mbox-short.txt","r") as new_file:
    for line in new_file:
        line=line.upper()
        print(line)
