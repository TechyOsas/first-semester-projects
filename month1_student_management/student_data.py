students = []

def add_student():
    """
    TODO: Prompt the user to enter student name, age, and grade.
    Append the student as a dictionary to the students list.
    """
    name = input("Enter your name: ").strip().lower()
    age = int(input("Enter your age: ").strip())
    grade = int(input("Enter your grade: "))

    #NAME VALIDATION
    if not name.replace(' ', '').isalpha():
        print('Name must contain only letters and must not be empty') #firstname_surname
        return
    
    if len(name) < 2:
        print('Name must contain at least two characters long')
        return
   
    #AGE VALIDATION
    if age not in range(4,70):
        print('Age must be between 4 and 20')
        return
    
    #GRADE VALIDATION
    if grade not in range(0,101):
        print('Grade should be between 0 and 100')
        return
    
    #CHECK FOR DUPLICATES
    for student in students:
        if student['name'] == name and student['age'] == age and student['grade'] == grade:
            print('Student already exists.')
            return
    
    student_record = {'name': name,
                      'age': age,
                      'grade': grade}
    students.append(student_record)



def view_students():
    """
    TODO: Loop through the students list and print each student's info.
    """
    if len(students) == 0:
        print('No students added yet, please proceed to add students.')
        return
    else:
        for student in students:
            print(student)
        pass


def get_average_grade():
    """
    TODO: Return the average grade of all students.
    """
    grade_list = []
    for student in students:
        grade_list.append(student['grade'])

    pass
    avg_grade = sum(grade_list)/len(grade_list)
    return avg_grade