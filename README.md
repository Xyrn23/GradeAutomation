# Grade Automation Tool 
**By: Jers**

ON SITE (50%)|1st week | 2nd week | 3rd week | 4th week | 5th week
--- | :---: | :---: | :---: | :---: | :---: 
Attendance [10%]| 100 | 100 | 100 | 100 | 100 
AAE [35%]| 100 | 100 | 100 | 100 | 100 | 100
Evalution [30%] | 100 | 100 | 100 | 100 | 100
Project [25%]| 100 | 100 | 100 | 100 | 100 
**LMS (30%)** | 100 | 100 | 100 | 100 | 100
**Major Exam (20%)** | 50/50 |



$$ \frac {firstGr + secondGr + thirdGr+ fourthGr + fifthGr}{5} (percentOfCriteria)$$

Quarters | Grades 
--- | :---:
Prelim(30%) | 30
Midterm(30%) | 30
Finals(40%) |40
**FinalGrade** | 100

```python
from colorama import Fore

def logo():
    print(Fore.GREEN + """ 
 __    ___    __    ___   ____                                
/ /`_ | |_)  / /\  | | \ | |_                                 
\_\_/ |_| \ /_/--\ |_|_/ |_|__                                
 __     __    _     __    _     _      __   _____  ___   ___  
/ /`   / /\  | |   / /`  | | | | |    / /\   | |  / / \ | |_) 
\_\_, /_/--\ |_|__ \_\_, \_\_/ |_|__ /_/--\  |_|  \_\_/ |_| \\
[You just need to enter your grade(0-100) and let the tool do the work]
""")
    
def get_input(prompt):
    while True:
        try:
            value = float(input(f"\033[32m{prompt}\033[0m"))
            if 0 <= value <= 100:
                return value
            else:
                print("\033[31mInvalid input. Please enter a valid grade between 0 and 100.\033[0m")
        except ValueError:
            print("\033[31mInvalid input. Please enter a valid numeric value.\033[0m")

def get_quarter_weight(quarter):
    if quarter == "prelim":
        return 0.30
    elif quarter == "midterm":
        return 0.30
    elif quarter == "finals":
        return 0.40
    else:
        print("Invalid quarter choice. Using default weight of 0.30 for Prelim.")
        return 0.30

def calculate_grade(criteria, num_weeks, weight):
    print(f"\033[33m\033[1m>> {criteria} <<\033[0m")
    grades = [get_input(f"Enter your grade for {criteria} Week {i + 1}~~>") for i in range(num_weeks)]
    total_grade = sum(grades)
    average_grade = (total_grade / num_weeks) * weight
    print(f"\033[33mYour grade in {criteria} is \033[31m{average_grade:.2f}%\033[33m.\033[0m\n")
    return average_grade

def main():
    logo()

    attendance_grade = calculate_grade("ATTENDANCE", 5, 0.10)
    aae_grade = calculate_grade("AAE", 5, 0.35)
    eval_grade = calculate_grade("EVALUATION", 5, 0.30)
    project_grade = calculate_grade("PROJECT", 5, 0.25)

    final_onsite_grade = (attendance_grade + aae_grade + eval_grade + project_grade) * 0.50
    print(f"\033[32mYour final OnSite grade is: \033[31m{final_onsite_grade:.2f}%\033[0m\n")

    lms_grade = calculate_grade("LMS", 5, 0.30)
    major_exam_score = get_input("Enter your score for the Major Exam (out of 50)~~>")
    major_exam_grade = (major_exam_score / 50) * 0.20
    print(f"\033[33mYour grade in Major Exam is \033[31m{major_exam_grade:.2f}%\033[0m\n")

    final_onsite_lms_major_grade = final_onsite_grade + lms_grade + major_exam_grade
    print(f"\033[32mYour final grade (including LMS and Major Exam) is: \033[31m{final_onsite_lms_major_grade:.2f}%\033[0m")

    quarter = input("\033[32mEnter the quarter (prelim/midterm/finals): \033[0m")
    quarter_weight = get_quarter_weight(quarter)
    final_grade = final_onsite_lms_major_grade * quarter_weight
    print(f"\033[32mYour final grade (including LMS and Major Exam) for {quarter} is: \033[31m{final_grade:.2f}%\033[0m")

if __name__ == "__main__":
    main()

```
