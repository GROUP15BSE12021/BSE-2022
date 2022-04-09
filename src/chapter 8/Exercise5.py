file_name = input("Enter a file name : ")
with open(file_name) as fhand:
    count = 0
    for line in fhand:
        if line.startswith("From") and not line.startswith("From:"):
            line = line.split()
            print(line[1])
            count += 1
print(f"There were {count} lines in the file with From as the first word")