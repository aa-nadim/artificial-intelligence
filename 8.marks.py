from tabulate import tabulate
members = [
    ["Rabia", "1811001", 88],
    ["Rashed", "1811007", 78],
    ["Maisha", "1811012", 70],
    ["Taspia", "1811013", 68],
    ["Shatabdi", "1811017", 60],
    ["Nurul", "1811021", 59],
    ["Akib", "1811022", 49]
]

head = ["Name", "Roll", "Marks"]
print(tabulate(members, headers=head, tablefmt="grid"))

####### THE CODE FOR CALCULATING GRADE POINTS #######
obtained_marks = {
    'Rabia': 88,
    'Rashed': 78,
    'Maisha': 70,
    'Taspia': 68,
    'Shatabdi': 60,
    'Nurul': 59,
    'Akib': 49
}
for item in obtained_marks:
    if obtained_marks[item] >= 80:
        print(item, 'has secured a point 4.00 (Letter Grade A+)')
    elif 80 > obtained_marks[item] >= 75:
        print(item, 'has secured a point 3.75 (Letter Grade A)')
    elif 75 > obtained_marks[item] >= 70:
        print(item, 'has secured a point 3.50 (Letter Grade A-)')
    elif 70 > obtained_marks[item] >= 65:
        print(item, 'has secured a point 3.25 (Letter Grade B+)')
    elif 65 > obtained_marks[item] >= 60:
        print(item, 'has secured a point 3.00 (Letter Grade B)')
    elif 60 > obtained_marks[item] >= 55:
        print(item, 'has secured a point 2.75 (Letter Grade B-)')
    elif 55 > obtained_marks[item] >= 50:
        print(item, 'has secured a point 2.50 (Letter Grade C+)')
    elif 50 > obtained_marks[item] >= 45:
        print(item, 'has secured a point 2.25 (Letter Grade C)')
    elif 45 > obtained_marks[item] >= 40:
        print(item, 'has secured a point 2.00 (Letter Grade D)')
    else:
        print(item, 'has unfortunately failed this course')
