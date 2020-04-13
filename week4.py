grade_one= {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}

grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}

grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}

def students_names(grade):
    if grade=='grade_one':
        return grade_one.keys()
    elif grade=='grade_two':
        return grade_two.keys()
    elif grade=='grade_three':
        return grade_three.keys()

def student_score(grade,student):
    if grade=='grade_one':
        list=grade_one.get(student)
        return sum(list)
    elif grade=='grade_two':
        list=grade_two.get(student)
        return sum(list)
    elif grade =='grade_three':
        list=grade_three.get(student)
        return sum(list)

def students_count(grade):
    return len('grade')

while True:
    a=input("Choose one: students_names, student_score, students_count: ")
    if a =='students_names':
        print(students_names(input('Enter grade: ')))
    elif a=='student_score':
        print(student_score(input('Enter grade:'), input('Enter student name: ')))
    elif a=='students_count':
        print(students_count(input('Enter grade: ')))
    z=(input('Enter Done to finish  or More to choose again: '))
    if z=='More':
        continue
    if z== 'Done':
        break
