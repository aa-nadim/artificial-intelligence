from prettytable import PrettyTable

# Specify the Column Names while initializing the Table
myTable = PrettyTable(["Student Name","Roll No", "Mark"])

# Add rows
print("ICE-4101 Obtained Marks")
print("-------------------------")
name=['Nazmul Hasan','Fatema Jannat Dihan','Robel Hossain Badhon','Sharifur Rahman','Khalid Hossen','Tahmina Yeasmin','Shariful Islam']
roll_no=['ASH1811024M','MUH1811025F','ASH1811026M','ASH1811027M','ASH1811030M','BKH1811032F','ASH1811033M']
marks=[45,67,55,84,76,35,90]
for i in range(7):
    myTable.add_row([name[i],roll_no[i], marks[i]])
print(myTable)
myTable = PrettyTable(["Student Name","Roll No", "Mark", "Letter Grade", "Grade Point"])
mark=[]
letter_grade=[]
grade_point= []
for i in range(7):
    print("Enter Mark for Roll",roll_no[i] ,":")
    mark.insert(i, int(input()))
    if mark[i]>=80 and mark[i]<=100:
        letter_grade.append("A+")
        grade_point.append("4.00")
    elif mark[i]>=75 and mark[i]<80:
        letter_grade.append("A")
        grade_point.append("3.75")
    elif mark[i]>=70 and mark[i]<75:
        letter_grade.append("A-")
        grade_point.append("3.50")
    elif mark[i]>=65 and mark[i]<70:
        letter_grade.append("B+")
        grade_point.append("3.25")
    elif mark[i]>=60 and mark[i]<65:
        letter_grade.append("B")
        grade_point.append("3.00")
    elif mark[i]>=55 and mark[i]<60:
        letter_grade.append("B-")
        grade_point.append("2.75")
    elif mark[i]>=50 and mark[i]<55:
        letter_grade.append("C+")
        grade_point.append("2.50")
    elif mark[i] >= 45 and mark[i] < 50:
        letter_grade.append("C")
        grade_point.append("2.25")
    elif mark[i] >= 40 and mark[i] < 45:
        letter_grade.append("D")
        grade_point.append("2.00")
    elif mark[i] < 40:
        letter_grade.append("F")
        grade_point.append("0.00")

    else:
        print("Invalid Input!")
    myTable.add_row([name[i], roll_no[i], marks[i],letter_grade[i],grade_point[i]])


print(myTable)