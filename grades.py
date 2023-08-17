# [this tool is excusively for BCP students who has the same grading as I am on understanding yourself]
# but feel free to use this for testing
# I herebly take the owner of this code so if you will use on your project, a little credits will do. ty
from colorama import init, Fore

init(autoreset=True)

def logo():
    print(Fore.GREEN + """ 
 __    ___    __    ___   ____                                
/ /`_ | |_)  / /\  | | \ | |_                                 
\_\_/ |_| \ /_/--\ |_|_/ |_|__                                
 __     __    _     __    _     _      __   _____  ___   ___  
/ /`   / /\  | |   / /`  | | | | |    / /\   | |  / / \ | |_) 
\_\_, /_/--\ |_|__ \_\_, \_\_/ |_|__ /_/--\  |_|  \_\_/ |_| \
[You just need to enter your grade(0-100) and let the tool to the work]
""")
logo()

def get_input(prompt):
    return input(Fore.GREEN + prompt + Fore.RESET)

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

def attendance():
    print(Fore.YELLOW + "\033[1m>> ATTENDANCE <<\033[0m")
    attendanceGrades = [float(get_input(f"{Fore.GREEN}Enter your grade for Attendance Week {i + 1}~~>{Fore.RESET}")) for i in range(5)]
    attendanceGrade = (sum(attendanceGrades) / 5) * 0.1
    print(f"{Fore.YELLOW}Your grade in Attendance is {Fore.RED}{attendanceGrade:.2f}%{Fore.YELLOW}.\n")
    return attendanceGrade

def aae():
    print(Fore.YELLOW + "\033[1m>> AAE <<\033[0m")
    aaeGrades = [float(get_input(f"{Fore.GREEN}Enter your grade for AAE Week {i + 1}~~>{Fore.RESET}")) for i in range(5)]
    aaeGrade = (sum(aaeGrades) / 5) * 0.35
    print(f"{Fore.YELLOW}Your grade in AAE is {Fore.RED}{aaeGrade:.2f}%{Fore.YELLOW}.\n")
    return aaeGrade

def evaluation():
    print(Fore.YELLOW + "\033[1m>> EVALUATION <<\033[0m")
    evalGrades = [float(get_input(f"{Fore.GREEN}Enter your grade for Evaluation Week {i + 1}~~>{Fore.RESET}")) for i in range(5)]
    evalGrade = (sum(evalGrades) / 5) * 0.3
    print(f"{Fore.YELLOW}Your grade in Evaluation is {Fore.RED}{evalGrade:.2f}%{Fore.YELLOW}.\n")
    return evalGrade

def project():
    print(Fore.YELLOW + "\033[1m>> PROJECT <<\033[0m")
    projectGrades = [float(get_input(f"{Fore.GREEN}Enter your grade for Project {i + 1}~~>{Fore.RESET}")) for i in range(5)]
    projectGrade = (sum(projectGrades) / 5) * 0.25
    print(f"{Fore.YELLOW}Your grade in Project is {Fore.RED}{projectGrade:.2f}%{Fore.YELLOW}.\n")
    return projectGrade

attendanceGrade = attendance()
aaeGrade = aae()
evalGrade = evaluation()
projectGrade = project()

final_onsite_grade = (attendanceGrade + aaeGrade + evalGrade + projectGrade) * 0.50
print(Fore.GREEN + f"Your final OnSite grade is: {Fore.RED}{final_onsite_grade:.2f}%{Fore.RESET}\n")

def lms():
    print(Fore.YELLOW + "\033[1m>> LMS <<\033[0m")
    lmsGrades = [float(get_input(f"{Fore.GREEN}Enter your grade for LMS Week {i + 1}~~>{Fore.RESET}")) for i in range(5)]
    lmsGrade = (sum(lmsGrades) / 5) * 0.3
    print(f"{Fore.YELLOW}Your grade in LMS is {Fore.RED}{lmsGrade:.2f}%{Fore.YELLOW}.\n")
    return lmsGrade

def major_exam():
    print(Fore.YELLOW + "\033[1m>> MAJOR EXAM <<\033[0m")
    major_exam_score = float(get_input(f"{Fore.GREEN}Enter your score for the Major Exam (out of 50)~~>{Fore.RESET}"))
    major_exam_grade = (major_exam_score / 50) * 20
    print(f"{Fore.YELLOW}Your grade in Major Exam is {Fore.RED}{major_exam_grade:.2f}%{Fore.YELLOW}.\n")
    return major_exam_grade

lmsGrade = lms()
major_exam_grade = major_exam()

# Calculate and print final grades
final_onsite_lms_major_grade = final_onsite_grade + lmsGrade + major_exam_grade
print(Fore.GREEN + f"Your final grade (including LMS and Major Exam) is: {Fore.RED}{final_onsite_lms_major_grade:.2f}%{Fore.RESET}")

quarter = input(Fore.GREEN + "Enter the quarter (prelim/midterm/finals): ")
quarter_weight = get_quarter_weight(quarter)
final_grade = final_onsite_lms_major_grade * quarter_weight
print(Fore.GREEN + f"Your final grade (including LMS and Major Exam) for {quarter} is: {Fore.RED}{final_grade:.2f}%{Fore.RESET}")

