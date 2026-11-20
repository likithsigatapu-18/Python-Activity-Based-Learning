students = []
eligible = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of student", i + 1)

    name = input("Enter student name: ")
    aggregate = float(input("Enter aggregate marks: "))

    subjects = []
    for j in range(3):
        mark = float(input("Enter subject " + str(j + 1) + " marks: "))
        subjects.append(mark)

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    if (aggregate >= 75 and
        all(mark >= 60 for mark in subjects) and
        attendance >= 75 and
        income <= 250000):

        eligible.append([name, aggregate, attendance, income])

    else:
        print(name, "is Not Eligible")

eligible.sort(key=lambda x: (-x[1], -x[2], x[3]))

print("\n===== SCHOLARSHIP ALLOCATION RESULTS =====")

if len(eligible) == 0:
    print("No students are eligible for scholarship.")

else:
    print("\nRank  Name       Aggregate  Attendance  Income")

    for i, student in enumerate(eligible):
        print(i + 1, student[0], student[1],
              student[2], student[3])
