try :
    new_file=input("Enter file name: ")
    total = 0
    count = 0
    with open(new_file,"r") as file:
    # for loop used to read through all lines in the file
        for line in file:
            # check for every line that starts wit the desired prefix
            if line.startswith("X-DSPAM-Confidence:"):
                count = count + 1
                var =line[line.find("0"):] #for the first number in the line "X-SPAM-Confidence:"
                float_value = float(var) # is coverted to float
                total = total + float_value

    average_spam = total/count
    print('Average SPAM ; ', average_spam)

except:
    print("file not found ")



