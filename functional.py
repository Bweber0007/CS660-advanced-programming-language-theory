from functools import reduce, partial

### single-line functions' readability ###
#
# STRENGTHS:
# These functions are concise, single-line functions. This allows there purpose to be easily
# understood at a glance, without needing to read through multiple lines of code.
# The function names provide descriptive context, making it clear what each function is calculating or checking.
# This enhances readability and makes each function self-explanatory.
#
# WEAKNESSES:
# Even though these functions are concise, they may be less readable for those who are not familiar with 
# functional programming concepts or lambda functions. This could make it harder for some developers to 
# understand the code quickly.
# Brevity does not always equate to clarity. For example, the use of lambda functions and higher-order functions like map and filter 
# may require a deeper understanding of functional programming paradigms, which could be a barrier for some readers.

calculate_count = len
calculate_sum = sum
calculate_average = lambda grades: sum(grades) / len(grades)
find_maximum = lambda grades: reduce(max, grades)
find_minimum = lambda grades: reduce(min, grades)

is_passing = lambda grade: grade >= 70
count_passing = lambda grades: len(list(filter(is_passing, grades)))
calculate_pass_rate = lambda grades: (count_passing(grades) / len(grades)) * 100

### Multline functions' readability ###
# These functions share many of the same strengths and weaknesses as the single-line functions.
#
# STRENGTHS:
# These functions also utilize descriptive names, which helps in understanding their purpose without 
# intense analysis. Also, the integrated use of the previous single-line functions within these multi-line functions 
# produces more concise functions overall which helps to maintain a level of readability and modularity.
# 
# WEAKNESSES:
# The use of lambda functions and higher-order functions like filter and reduce can make the code
# harder to understand for those unfamiliar with functional programming or more advanced programming tools/functions.

### MODIFIED SECTION ###
# dictionaries for immutable data lookup and tuples for immutable data storage
# 
grade_count_labels = {
    "student": "Total classes",
    "class": "Total students"
}

report_titles = {
    "student": "Student Grade Analysis Results:",
    "class": "Class Grade Analysis Results:"
}

grades = {
    "class": (85, 92, 78, 96, 58, 73, 91, 87, 94, 82),
    "student": (73, 60, 91, 84)
}

def create_analysis_functions(grade_type):
    return (
        lambda grades: f"{grade_count_labels.get(grade_type)}: {calculate_count(grades)}",
        lambda grades: f"Average grade: {calculate_average(grades):.1f}",
        lambda grades: f"Highest grade: {find_maximum(grades)}",
        lambda grades: f"Lowest grade: {find_minimum(grades)}",
        lambda grades: f"Pass rate: {calculate_pass_rate(grades):.1f}%"
    )

def generate_report(grades, grade_type):
    analysis_functions = create_analysis_functions(grade_type)
    return tuple(map(lambda func: func(grades), analysis_functions))

def print_report(report_lines, grade_type):
    print(report_titles.get(grade_type))
    tuple(map(print, report_lines))
    print()

def analyze_grades():
    class_grades = grades.get("class")
    student_grades = grades.get("student")
    class_report = generate_report(class_grades,"class")
    student_report = generate_report(student_grades,"student")
    print_report(class_report,"class")
    print_report(student_report,"student")
############################
if __name__ == "__main__":
    analyze_grades()