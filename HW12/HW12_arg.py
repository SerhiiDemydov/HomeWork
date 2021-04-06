"""In the homework directory you can find the directory arg_parser_homework where you can find 2020_june_mini.csv file.

1. Create a script with arguments:

exp; required: false; default: min(exp)
current_job_exp; required: false; default: max(current_job_exp)
sex; required: false
city; required: false
position; required: false
age; required: false
path_to_source_files; required: true;
destination_path; required: false; default: .
destination_filename; required: false; default: f"2020_june_mini.csv".
The script should read the .csv file and get the information based on your input and generate a new .csv
file with that info

Example of input:
-exp 3 -sex female -position DevOps -city Kyiv --path_to_source_files . ...
"""

import argparse
import csv

# Task 1
parser = argparse.ArgumentParser(description="Homework 12")
parser.add_argument('-cp', '--choice_program', required=True, choices=['1', '2'], help="Choice program 1: Task1 ; 2: Task2")
parser.add_argument('-e', '--exp', required=False, default="min(exp)", help="Experience")
parser.add_argument('-c', '--current_job_exp', required=False, default="max(current_job_exp)", help="Currently job experience")
parser.add_argument('-s', '--sex', required=False, help="Sex")
parser.add_argument('-ct', '--city', required=False, help="City")
parser.add_argument('-p', '--position', required=False, help="Position")
parser.add_argument('-a', '--age', required=False, help='Age')
parser.add_argument('-psf', '--path_to_source_files', required=False, help="Path to source files ")
parser.add_argument('-dp', '--destination_path', required=False, default='', help="Destination path")
parser.add_argument('-df', '--destination_filename', required=False, default="2020_june_mini2.csv",
                    help="Destination filename")

# Task 2
parser.add_argument('-ss', '--start_salary', required=False, help="Starting point of salary")
parser.add_argument('-es', '--end_salary', required=False, help="The max point of salary")
parser.add_argument('-l', '--language', required=False, help="Programming language")

args = parser.parse_args()

# Task 1
choice_program = args.choice_program
exp = args.exp
current_job_exp = args.current_job_exp
sex = args.sex
city = args.city
position = args.position
age = args.age
path_to_source_files = args.path_to_source_files
destination_path = args.destination_path
destination_filename = args.destination_filename

"""2. Create a script with arguments:

source_file_path; required: true; 
start_salary; required: false; help: starting point of salary;
end_salary; required: false; help: the max point of salary;
position; required: false; help: position role
age; required: false; help: Age of person
language; required: false; help; Programming language

Based on this info generate a new report of average salary.
"""

# Task 2
start_salary = args.start_salary
end_salary = args.end_salary
language = args.language

# Task 1
exp_list = []
current_job_exp_list = []
if int(choice_program) == 1:
    with open(path_to_source_files, 'r', newline='') as file:
        read = csv.DictReader(file)
        head = read.fieldnames

        if exp == "min(exp)" or current_job_exp == "max(current_job_exp)":
            for dict_info in read:
                if exp == "min(exp)":
                    exp_list.append(float(dict_info['exp']))
                if current_job_exp == "max(current_job_exp)":
                    current_job_exp_list.append(float(dict_info['current_job_exp']))
            if exp == "min(exp)":
                exp = min(exp_list)
                print(f'Experience = {current_job_exp}')
            if current_job_exp == "max(current_job_exp)":
                current_job_exp = max(current_job_exp_list)
                print(f'Currently job experience = {current_job_exp} ')

        with open(destination_path + destination_filename, 'w', newline="") as f:
            writer = csv.DictWriter(f, fieldnames=head)
            writer.writeheader()
            for dict_info in read:
                if float(dict_info['exp']) != float(exp):
                    continue
                if current_job_exp is not None and float(dict_info['current_job_exp']) != float(current_job_exp):
                    continue
                if sex is not None and dict_info['Пол'] != sex:
                    continue
                if city is not None and dict_info['Город'] != city:
                    continue
                if position is not None and dict_info['Должность'] != position:
                    continue
                if age is not None and dict_info['Возраст'] != age:
                    continue
                writer.writerow(dict_info)



# Task 2

salary = 0
quon = 0

if int(choice_program) == 2:
    with open(path_to_source_files, 'r', newline='') as file:
        read = csv.DictReader(file)
        for row in read:
            if start_salary is not None and float(row["Зарплата.в.месяц"]) < float(start_salary):
                continue
            if end_salary is not None and float(row["Зарплата.в.месяц"]) > float(end_salary):
                continue
            if language is not None and row["Язык.программирования"] != language:
                continue
            if position is not None and row['Должность'] != position:
                continue
            if age is not None and row['Возраст'] != age:
                continue
            salary += float(row["Зарплата.в.месяц"])
            quon += 1
    aver_salary = salary / quon
    print(f'Average salary = {round(aver_salary, 2)}')
