# Let's learn how to read a .json file from within a data file

# Remember to make sure the terminal is tethered to the file where the .py file is located

    #  run this script ----->****** python gradebook_parser_json.py ******
    #  Testing ----->****** pytest test/gradebook_parser_json.py ******

    

# if we're using os to find filepath instead of hard coding, then make sure to import needed modules

# step 1 for activating json reading

import os
import json
import pandas
import statistics



# step 2, define the function to move forward with json script

def calculate_avg_json_grades(x):
    with open(x, "r") as i:
        file_stuffing = i.read()
    
    gradebook = json.loads(file_stuffing)

    students = gradebook["students"]
    grades = [s ["finalGrade"] for s in students]
    avg_grade = statistics.mean(grades)
    return avg_grade

# step 3, make sure that you set up the filepath coding so that the terminal on mac will run this script

if __name__ == "__main__":
    print("This is the house of json")
    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.json")
    print(gradebook_filepath)
    avg = calculate_avg_json_grades(gradebook_filepath)
    print(avg)








# # json_instructions_recap =

# '''
# import os
# import json
# import pandas
# import statistics

# def calculate_avg_json_grades(x):
#     with open(x, "r") as i:

#         file_contents = i.read()

#     gradebook = json.loads(file_contents)     


#     students = gradebook["students"]
#     grades = [s["finalGrade"] for s in students]
#     avg_grade = statistics.mean(grades)
#     return avg_grade

# if __name__ == "__main__":
#     print("PARSING SOME JSON GRADEBOOK FILES HERE...")
#     gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2018.json")
#     print(gradebook_filepath) #>  c:\users\mike\documents\github\omniparser-starter-py\omniparser\gradebook_parser.py
#     print(os.path.isfile(gradebook_filepath)) #> True
#     avg_grade = calculate_avg_json_grades(gradebook_filepath)
#     print("{0:.2f}".format(avg_grade))

# ''' 