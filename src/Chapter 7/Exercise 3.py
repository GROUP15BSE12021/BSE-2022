file_name = input("Enter file name: ")
count = 0
# checking for file existance for graceful execution
try :
    with open(file_name,"r") as file_handle:
        for line in file_handle:
            if line.startswith("Subject"):
                count = count + 1 # to count each line that starts with "subject"
    print("There were ",count, "subject lines in the ", file_name)
except:
    # python egg.py
    if file_name.lower() == "na na boo boo" :
        print("NA NA BOO BOO TO YOU - You have been punk'd")
    else:           # when the file entered is absolutely not available
        print("file doesnt exist/not found")