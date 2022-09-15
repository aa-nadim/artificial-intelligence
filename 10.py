id=[]
letterpoint=[]
gradepoint=[]

n=int(input('Enter number of student: '))
for i in range(n):
    student=input('Enter Student id:  ');
    id.append(student)
    marks=int(input('Enter Student marks obtained in course 3201: '))
    if marks>=80:
        letterpoint.append('A+')
        gradepoint.append('4.00')
    elif marks <= 79 and marks >=75:
        letterpoint.append('A')
        gradepoint.append('3.70')
    elif marks <= 74 and marks >=70 :
        letterpoint.append('A-')
        gradepoint.append('3.50')
    elif marks <= 69 and marks >=65:
        letterpoint.append('B+')
        gradepoint.append('3.25')
    elif marks <= 64 and marks >=60:
        letterpoint.append('B')
        gradepoint.append('3.00')
    elif marks <= 59 and marks >=50:
        letterpoint.append('B-')
        gradepoint.append('2.75')
    elif marks <= 49 and marks >=45:
        letterpoint.append('C')
        gradepoint.append('2.50')
    elif marks <=44  and marks >=40:
        letterpoint.append('D')
        gradepoint.append('2.00')
    else:
        letterpoint.append('F')
        gradepoint.append('0.00')

print('Student ID    Gradepoint  Letterpoint')
for i in range(n):
    print(id[i] , end='            ')
    print(gradepoint[i], end='           ')
    print(letterpoint[i])
    print()



