more_entries = True
while more_entries:
    while True:
        student_name = input('Enter Name Of Student: ')
        if student_name.isnumeric():
            print('Please enter only alphabetic characters')
        else:
            break

    while True:
        try:
            num_subjects = int(input('Enter number of subjects student has: '))
            if num_subjects < 1:
                raise ValueError('Please enter a valid value')
            elif num_subjects > 15:
                raise ValueError('Too many subjects. Please enter subjects in the range from 1 to 15 only')
            else:
                break
        except ValueError as e:
            print(e)

    marks_list = []
    for i in range(num_subjects):
        while True:
            try:
                print("Enter marks of subject ", i + 1, ': ', end=' ')
                marks = float(input())
                if marks < 1 or marks > 100:
                    raise ValueError('Please enter marks from 1 to 100 only')
                else:
                    marks_list.append(marks)
                    break
            except ValueError as e:
                print(e)

    total_marks = sum(marks_list)
    avg_marks = total_marks / num_subjects

    if avg_marks < 40:
        print('')
        print('------------------------------')
        print('Student result: Fail')
        print('Student average score is ', avg_marks)
        print('Student subjects wise score:')
        for i, marks in enumerate(marks_list):
            print('Score in subject ', i + 1, ' is = ', marks)
    elif 40 <= avg_marks <= 50:
        print('')
        print('------------------------------')
        print('Student GRADE IS: C')
        print('Student average score is ', avg_marks)
        print('Student subjects wise score:')
        for i, marks in enumerate(marks_list):
            print('Score in subject ', i + 1, ' is = ', marks)
    elif 51 <= avg_marks <= 60:
        print('')
        print('------------------------------')
        print('Student GRADE: B')
        print('Student average score is ', avg_marks)
        print('Student subjects wise score:')
        for i, marks in enumerate(marks_list):
            print('Score in subject ', i + 1, ' is = ', marks)
    elif 61 <= avg_marks <= 70:
        print('')
        print('------------------------------')
        print('Student GRADE: B+')
        print('Student average score is ', avg_marks)
        print('Student subjects wise score:')
        for i, marks in enumerate(marks_list):
            print('Score in subject ', i + 1, ' is = ', marks)
    elif 71 <= avg_marks <= 80:
        print('')
        print('------------------------------')
        print('Student GRADE: A')
        print('Student average score is ', avg_marks)
        print('Student subjects wise score:')
        for i, marks in enumerate(marks_list):
            print('Score in subject ', i + 1, ' is = ', marks)
    elif 81 <= avg_marks <= 90:
        print('')
        print('------------------------------')
        print('Student GRADE: A+')
        print('Student average score is ', avg_marks)
        print('Student subjects wise score:')
        for i, marks in enumerate(marks_list):
            print('Score in subject ', i + 1, ' is = ', marks)
    elif 91 <= avg_marks <= 100:
        print('')
        print('------------------------------')
        print('Student GRADE: O ')
        print('Student average score is ', avg_marks)
        print('Student subjects wise score:')
        for i, marks in enumerate(marks_list):
            print('Score in subject ', i + 1, ' is = ', marks)

    while True:
        try:
            more_entries = int(input('For MORE ENTRIES press 1\nTo QUIT press any numeric value other than 1: '))
            if more_entries not in [1, 2]:
                raise ValueError('Please enter a valid input')
            else:
                break
        except ValueError as e:
            print(e)

    if more_entries == 1:
        continue
    else:
        more_entries = False
