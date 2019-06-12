# omniparser/gradebook_parser.py

import os # to activate pandas, always need to import os
import statistics # this module is needed for statistics cmd, via statistics.avg() or statistics.median() etc. etc.

import pandas # needed to use pandas at all!

def calculate_average_grade_from_csv(my_csv_filepath): #This portion is creating your own module
    df = pandas.read_csv(my_csv_filepath) # you are creating a read function for the .csv

    rows = df.to_dict("records")

    grades = [r["final_grade"] for r in rows] #> [86.7, 95.1, 60.3, 99.8, 97.4, 85.5, 97.2, 98.0, 93.9, 92.5], r["final_grade"] 
    # --> read the column downwards loop

    avg_grade = statistics.mean(grades) # Making use of the statistics panda via command --> statistics.mean(grades)

    return avg_grade #90.64 #"OOPS"


if __name__ == "__main__": #now time to execute on the module that you just created
    print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")
    print("if this prints, then this will show up in terminal")

    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2018.csv") 
    #use this path module and directory module to denote which file to focus on.  Note the .csv name

    avg = calculate_average_grade_from_csv(gradebook_filepath)
    print(avg)
    #Finally, your are feeding in the gradebook_filepath into the original UDF/module.  avg should be the 'return' component