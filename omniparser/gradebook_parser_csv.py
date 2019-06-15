# Let's learn how to read a .csv file from within a data file

# Remember to make sure the terminal is tethered to the file where the .py file is located

    #  run this script ----->****** python gradebook_parser_csv.py ******

# if we're using os to find filepath instead of hard coding, then make sure to import eeded modules


# Step 1: import the correct functions

import os
import statistics
import pandas
import json

# Step 2: set up a UDF to ensure that you can use pandas to process csv file form data file

def calculate_avg_from_csv (x):
    dataframe = pandas.read_csv(x)
    avg_grade = dataframe["final_grade"].mean()
    return avg_grade


# Step 3: we need to ensure that associated terminal, github on windows, terminal on mac will run the .csv file

if __name__ == "__main__":
    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.csv")
    print(gradebook_filepath)
    avg = calculate_avg_from_csv(gradebook_filepath)
    print(avg)




# if __name__ == "__main__": # Required script to run the JSON or CSV from terminal
#     print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")
#     gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.csv")
#     #gradebook_filepath = "C:/Users/Mike/Documents/GitHub/omniparser-starter-py/data/gradebook_2019.csv"
#     #gradebook_filepath = "data/gradebook_2019.csv"
#     print(gradebook_filepath)
#     avg = calculate_average_grade_from_csv(gradebook_filepath)
#     print(avg)
















instructions_recap = [

'''
import os # needed for os functions
import pandas # needed for pandas based crunching
import json # needed to process json (This is for later)
import statistics # needed to process .statistics based functions ex. .mean(), .median()




# Let's create function to parse through the .csv

def calculate_avg_csv_grades(x):
    dataframe = pandas.read_csv(x)

    # avg_grade = df["final_grade"].mean()
    avg_grade = dataframe["final_grade"].mean()

    return avg_grade #90.64 #"OOPS"


# Now that we created a UDF to read the .csv, now let's ensure that we print out the results using UDF components

if __name__== "__main__": # <---- this 'if' statement is required to process file via terminal
    print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")
    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..","data","gradebook_2018.csv")
    # the prior command is about joining files where file for where the data is located (grade.csv file)
    print(gradebook_filepath) # <--- this is where the file for your gradebook, notably the 2019.csv is located
    avg_grade = calculate_avg_csv_grades(gradebook_filepath)
    print("{0:.2f}".format(avg_grade))



# if __name__ == "__main__": # Required script to run the JSON or CSV from terminal
#     print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")
#     gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.csv")
#     #gradebook_filepath = "C:/Users/Mike/Documents/GitHub/omniparser-starter-py/data/gradebook_2019.csv"
#     #gradebook_filepath = "data/gradebook_2019.csv"
#     print(gradebook_filepath)
#     avg = calculate_average_grade_from_csv(gradebook_filepath)
#     print(avg)

''' ]