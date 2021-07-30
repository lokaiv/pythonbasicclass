student_list = []

with open('students_list.csv', 'rt') as file:
    file.readline()
    while True:
        line = file.readline()
        if not line:
            break
        student = line.split(',')
        student_list.append(student)
print(student_list)