print("-----------WELCOME-----------\nGet access to data-statistics about measles vaccination around the world")

#try block for graceful check of the available measles file
try:
    input_file = open("measles.txt")
except:
    pass

output_file = input("Enter file name: ")

year = input("Enter year: ")
# function that executes the extraction of the users criteria
def extract_line(file):
    with open("measles.txt", "r") as file_name:
    # file measles.txt is to be read only
         for line in file_name:
            try:
                # if blocks to check for the year input
             index = line.split()[-1].strip() # splits the year of the line and strips any spaces attached
             if year.lower() == "all" or year == "":
                 file.write(line)
             # check for correspondence of the users input and each line in the file
             # for each line: "Afghanistan                                        WB_LI    8 Eastern Mediterranean     1982"
             # country-50 xters, income rate - 6 xters, %-2 xters, location-25 xters, and year-4 xters
             elif year == index[0] or year == index[0:2] or year == index[0:3] or year == index[0:4]:
                 file.write(line)
            except year is False:
                print("wow!!, the year required is actually not available")

# A try block as a provision when the user enters a file name that is either present or absent
try:
    with open(output_file , "w+") as file_handle:  #to delete all lines in present files and edit details required
        extract_line(file_handle)
except:
    with open(output_file,"x") as file: # to create absent file
        extract_line(file_handle)
