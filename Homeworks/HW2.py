students = 5
exams = 3
name = 2
grades = [[0 for i in range(exams)]for j in range(students)]
names = [[0 for i in range(name)]for j in range(students)]

for i in range(students):
    for j in range(exams):
        grades[i][j] = int(input(f"{i+1}. öğrencinin sınav notlarını giriniz : \n"))
    for k in range(name):
        names[i][k] = input(f"{i+1}. öğrencinin ismini ve soy ismini giriniz : \n")

info = dict()
maxExam = 0
bestStudent = tuple()

for i in range(students):
    examGrade = (grades[i][0] + grades[i][1] + grades[i][2]) // 3
    studentsNames = (names[i][0], names[i][1])
    info[(studentsNames)] = examGrade
    if maxExam < examGrade:
        maxExam = examGrade
        bestStudent = (names[i][0], names[i][1])
print(info)
sortedInfo = sorted(info.values())
print("Puan Listesi : ", sortedInfo)
print("Tebrikler : ", bestStudent)
