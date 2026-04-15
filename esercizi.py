# 1) Occurrence counter
from collections import Counter
m = [1, 2, 3, 4, 5, 6, 7, 7, 1, 4, 4]

def occurrence_counter(items):
    counts = {}
    for i in items:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts

print(occurrence_counter(m))

cnt = Counter(m)
print(cnt)


# 2) Filter and Tranform
d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lc = [i ** 2 for i in d if i % 2 == 1]

print(lc)


# 3) Grades Mean
import statistics as st
grades = [
    {
        "name": "Anna",
        "grade": 8
    },
    {
        "name": "Luca",
        "grade": 6
    }
]

def grades_mean(items):
    if not items:
        print("List is empty!")
        return None
    grade_values = [student["grade"] for student in items]

    return st.mean(grade_values)

print(grades_mean(grades))
    

# 4) File read
try:
    with open("grades.txt", "r") as f:
        grades2 = [int(line.strip()) for line in f]

    if grades2:
        mean = st.mean(grades2)
        min_grade = min(grades2)
        max_grade = max(grades2)

        print(f"The mean is: {mean}.\n")
        print(f"The min is {min_grade}.\n")
        print(f"The max is {max_grade}.")
    else:
        print("List is empty!")
except FileNotFoundError:
    print("Error, the file does not exist!")
except ValueError:
    print("Error, file does not contain numeric data!")


# 5) Student class

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
    
    def add_grade(self, g):
        self.grades.append(g)
    
    def mean(self):
        if not self.grades:
            return 0.0

        return st.mean(self.grades)
    
    def __repr__(self) -> str:
        return f"Name: {self.name}, Grades: {self.grades}, Mean: {self.mean():.2f}"

marco = Student("Marco")
sara = Student("Sara")
jack = Student("Jack")

marco.add_grade(8)
sara.add_grade(10)
jack.add_grade(10)

marco.add_grade(5)
sara.add_grade(3)
jack.add_grade(9)

marco.add_grade(8)
sara.add_grade(10)
jack.add_grade(9)

students = [marco, sara, jack]

for s in students:
    print(s)