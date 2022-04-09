fhandle = open("../../../../romeo.txt")
clean_data = []
for line in fhandle:
    line = line.split()
    for i in line:
        if i not in clean_data:
            clean_data.append(i)
clean_data.sort()
print(clean_data)