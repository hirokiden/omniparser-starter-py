# omniparser/gradebook_parser.py
# python gradebook_parser.py

import json
import os
import statistics

import pandas

def calculate_average_grade_from_csv(my_csv_filepath): # All CSV STUFF
    df = pandas.read_csv(my_csv_filepath)

    #breakpoint()
    # avg_grade = df["final_grade"].mean()

    #rows = df.to_dict("records")
    #grades = [r["final_grade"] for r in rows] #> [86.7, 95.1, 60.3, 99.8, 97.4, 85.5, 97.2, 98.0, 93.9, 92.5]
    #avg_grade = statistics.mean(grades)

    #grades =  df["final_grade"].to_list()
    #avg_grade = statistics.mean(grades)

    avg_grade = df["final_grade"].mean()

    return avg_grade #90.64 #"OOPS"

def calculate_average_grade_from_json(x): # ALL JSON STUFF...
    with open(x, "r") as f:
        #print(type(f)) #> Text IO
        file_contents = f.read()
        #print(type(file_contents)) #> str

    gradebook = json.loads(file_contents)
    #print(type(gradebook))
    #print(gradebook)

    #breakpoint()
    students = gradebook["students"]
    grades = [s["finalGrade"] for s in students]
    avg_grade = statistics.mean(grades)
    return avg_grade


if __name__ == "__main__": # Required script to run the JSON or CSV from terminal
    print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")
    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.csv")
    #gradebook_filepath = "C:/Users/Mike/Documents/GitHub/omniparser-starter-py/data/gradebook_2019.csv"
    #gradebook_filepath = "data/gradebook_2019.csv"
    print(gradebook_filepath)
    avg = calculate_average_grade_from_csv(gradebook_filepath)
    print(avg)

    print("PARSING SOME JSON GRADEBOOK FILES HERE...")
    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2018.json")
    print(gradebook_filepath) #>  c:\users\mike\documents\github\omniparser-starter-py\omniparser\gradebook_parser.py
    print(os.path.isfile(gradebook_filepath)) #> True
    avg = calculate_average_grade_from_json(gradebook_filepath)
    print(avg)
