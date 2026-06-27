# STRENGTHS:
# One of the key benefits to object-oriented programming is its inherent modularity. This seperation of concerns promotes readability by allowing developers to focus on 
# specific aspects of the code without needing to understand the entire codebase at once. Also, the simple and descriptive method names follow basic OOP principles 
# i.e. getters/setters (get_X). This allows for developers to easily undertand the purpose of each method without needing to read through the implementation details to gather 
# context. Also, this program utilizes smaller functions to implement built-in functions such as max, min, and sum. This level of abstraction improves readability by allowing 
# developers to understand the exact pupose of these function calls later in the program, rather than trying to parse the context for each function call. 
# This early abstraction intended for later implementation is very similar to the functional program's implementation.
#
# WEAKNESSES:
# While the modularity of OOP can enhance readability in many cases, it can also lead to a more fragmented program that negatively impacts readability if not implemented carefully.
# This is mainly caused by an unclear implementation of the methods within the working function which doesn't provide a clear flow of the program and method calls.

class GradeAnalyzer:
    def __init__(self,grades):
        self.grades = grades

    def get_count(self):
        return len(self.grades)

    def get_average(self):
        return sum(self.grades) / len(self.grades)

    def get_highest(self):
        return max(self.grades)

    def get_lowest(self):
        return min(self.grades)

    def get_pass_rate(self):
        passing_count = sum(1 for grade in self.grades if grade >= 70)
        return (passing_count / len(self.grades)) * 100

    def print_results(self):
        print("Grade Analysis Results:")
        print(f"Total Grades: {self.get_count()}")
        print(f"Average grade: {self.get_average():.1f}")
        print(f"Highest grade: {self.get_highest()}")
        print(f"Lowest grade: {self.get_lowest()}")
        print(f"Pass rate: {self.get_pass_rate():.1f}%")

### MODIFIED SECTION ### 
## inherit methods directly from GradeAnalyzer and override print_results to provide specific context for each type of analysis (class vs student)
class StudentAnalyzer(GradeAnalyzer):
    def print_results(self):
        print("Student Grade Analysis Results:")
        print(f"Total Classes: {self.get_count()}")
        print(f"Average grade: {self.get_average():.1f}")
        print(f"Highest grade: {self.get_highest()}")
        print(f"Lowest grade: {self.get_lowest()}")
        print(f"Pass rate: {self.get_pass_rate():.1f}%")

class ClassAnalyzer(GradeAnalyzer):
    def print_results(self):
        print("Class Grade Analysis Results:")
        print(f"Total Students: {self.get_count()}")
        print(f"Average grade: {self.get_average():.1f}")
        print(f"Highest grade: {self.get_highest()}")
        print(f"Lowest grade: {self.get_lowest()}")
        print(f"Pass rate: {self.get_pass_rate():.1f}%")

def analyze_grades():
    class_grades = [85, 92, 78, 96, 58, 73, 91, 87, 94, 82]
    student_grades = [73, 60, 91, 84]
    classroom_analyzer = ClassAnalyzer(class_grades)
    student_analyzer = StudentAnalyzer(student_grades)
    classroom_analyzer.print_results()
    student_analyzer.print_results()
################################

if __name__ == "__main__":
    analyze_grades()