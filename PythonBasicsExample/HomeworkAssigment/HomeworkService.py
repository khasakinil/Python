
def calculate_homework_grades(homework_assignment_grades) :
    sum_of_grades = 0
    for grade in homework_assignment_grades.values() : 
        sum_of_grades += grade
    final_grade = sum_of_grades/len(homework_assignment_grades)
    print("final_grade : " , round(final_grade, 2))
    