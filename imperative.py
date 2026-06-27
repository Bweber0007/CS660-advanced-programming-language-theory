# STRENGTHS:
# The single function provides a simple and clear entry point for analysis.
# The flow of the program is straightforward and linear, which promotes a natural, 
# reading style similar to reading a book.
# The plain-language, concise variable names also promote readability and understanding.
# The control flow of the if statements within the for loop provide a simple process
# for analysis which is easy to follow and debug.
#
# WEAKNESSES:
# This specific function has very few, if any, weaknesses in terms of readability.
# In future iterations, the main drawback of this style of programming is that it 
# can lead to longer functions without being broken down into smaller, more manageable pieces.
# This can impact overall readability and understanding due to the sheer amount of code that 
# needs to be read, understood, and connected all at once.
# Since this specific function is on the shorter side, it does not fall victim to this issue.

def analyze_grades():
    class_grades = [85, 92, 78, 96, 58, 73, 91, 87, 94, 82] ### MODIFIED SECTION ###

    total = 0
    count = 0
    highest = class_grades[0] ### MODIFIED SECTION ###
    lowest = class_grades[0] ### MODIFIED SECTION ###
    passing_count = 0

    for grade in class_grades:
        total += grade
        count += 1
        
        if grade > highest:
            highest = grade
        
        if grade < lowest:
            lowest = grade
            
        if grade >= 70:
            passing_count += 1

    average = total / count
    pass_rate = (passing_count / count) * 100

    print("Class Grade Analysis Results:") ### MODIFIED SECTION ###
    print(f"Total students: {count}")
    print(f"Average grade: {average:.1f}")
    print(f"Highest grade: {highest}")
    print(f"Lowest grade: {lowest}")
    print(f"Pass rate: {pass_rate:.1f}%")

### MODIFIED SECTION ###
# duplicated analysis sections for same analysis of different data sets (class vs student)

    student_grades = [73, 60, 91, 84]

    total = 0
    count = 0
    highest = student_grades[0]
    lowest = student_grades[0]
    passing_count = 0

    for grade in student_grades:
        total += grade
        count += 1
        
        if grade > highest:
            highest = grade
        
        if grade < lowest:
            lowest = grade
            
        if grade >= 70:
            passing_count += 1

    average = total / count
    pass_rate = (passing_count / count) * 100

    print("Student Grade Analysis Results:")
    print(f"Total classes: {count}")
    print(f"Average grade: {average:.1f}")
    print(f"Highest grade: {highest}")
    print(f"Lowest grade: {lowest}")
    print(f"Pass rate: {pass_rate:.1f}%")

###############################

if __name__ == "__main__":
    analyze_grades()