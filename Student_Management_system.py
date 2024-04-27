def input_roll_numbers():
    global roll_number
    roll_number = []
    with open("stdnt_db.txt", "r") as f:
        header_found = False
        for line in f:
            if not header_found:
                if "roll no." in line.lower():
                    header_found = True
            else:
                parts = line.split()
                if len(parts) >= 2:
                    try:
                        roll_num = int(parts[1]) 
                        roll_number.append(roll_num)
                    except ValueError:
                        continue 

input_roll_numbers()
def stdnt_db(): 
    while True:
        try:
            std_name = input("Please enter student name: ")
            if not std_name.isalpha():
                raise ValueError('Invalid name, please use only alphabetic characters.')
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            std_roll = int(input("Please enter student roll number: "))
            if std_roll in roll_number:
                  raise ValueError('roll number already exists ')
            elif std_roll < 1:
                  raise ValueError('Roll number must be a positive integer.')
            roll_number.append(std_roll)
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            std_percentage = float(input("Please enter student percentage: "))
            if std_percentage < 0 or std_percentage > 100:
                raise ValueError('Percentage must be between 0 and 100.')
            break
        except ValueError as e:
            print(e)
    with open("stdnt_db.txt", "a") as f:
        if f.tell() == 0:
            f.write('student name        roll no.    percentage\n')
            f.write('~~~~~~~~~~~~        ~~~~~~~~    ~~~~~~~~~~\n')
            f.write("\n")
            f.write('-------------------------------------------\n')
        f.write(f'{std_name:<20}    {std_roll:<10}   {std_percentage:<10.2f}\n')

stdnt_db()
def print_data():               
    with open ("stdnt_db.txt","r") as f:
            data=f.read()
            print('  ')
            print(data,end='')
            print('-------------------------------------------')

def reinp():
    while True:
        try:
            reinput=int(input("for reentering roll number press 1 for exit press 2 "))
            if reinput!=1 and reinput != 2:
                raise ValueError("please enter valid input")
            elif reinput==1:
                roll_exist()
                break
            elif reinput==2:
                break
        except ValueError:
            print("please enter the valid input ")
def roll():
    rollnum = None
    while rollnum is None:
        try:
            rollnum = int(input("Enter the roll number of the student for correction: "))
            if rollnum < 1:
                raise ValueError("Roll number must be a positive integer.")
        except ValueError as e:
            print(e)
            rollnum = None
    found = False
    with open("stdnt_db.txt", "r") as f:
        for line in f:
            parts = line.split()
            if len(parts) >= 2: 
                try:
                    line_roll_num = int(parts[1])
                    if line_roll_num == rollnum:
                        print('')
                        print("Found the following data:")
                        print('----------------------------------------------')
                        print(line.strip())
                        print('----------------------------------------------')
                        found = True
                        break
                except ValueError:
                    continue
    if not found:
        print('----------------------')
        print("Roll number not found.")
        print('----------------------')


def roll_exist():
    rollnum = None
    while rollnum is None:
        try:
            rollnum = int(input("Enter the roll number of the student for correction: "))
            if rollnum < 1:
                raise ValueError("Roll number must be a positive integer.")
        except ValueError as e:
            print(e)
            rollnum = None
    
    found = False
    updated_lines = []
    
    with open("stdnt_db.txt", "r") as f:
        lines = f.readlines()
        if len(lines) < 4:  
            print("No student data found in the file.")
            return
        
        updated_lines.extend(lines[:3]) 
        
        for line in lines[3:]: 
            parts = line.split()
            if len(parts) >= 3:  
                try:
                    line_roll_num = int(parts[1])
                    if line_roll_num == rollnum:
                        print("Found the following data:")
                        print('----------------------------------------------')
                        print(line.strip())
                        print('----------------------------------------------')
                        found = True
                        
                        while True:
                            try:
                                choice = int(input("Select what you want to correct:\n1. Name\n2. Roll Number (requires reentering name and percentage)\n3. Percentage\nEnter your choice: "))
                                if choice not in [1, 2, 3]:
                                    raise ValueError('Invalid choice. Please enter 1, 2, or 3.')
                                break
                            except ValueError as e:
                                print(e)
                        
                        if choice == 1:
                            while True:
                                try:
                                    new_name = input("Enter the corrected name: ")
                                    if not new_name.isalpha():
                                        raise ValueError('Invalid name. Please use only alphabetic characters.')
                                    parts[0] = new_name 
                                    print('Name updated succesfully...')
                                    break
                                except ValueError as e:
                                    print(e)
                        elif choice == 2:
                            while True:
                                try:
                                    new_name = input("Enter the corrected name: ")
                                    new_percentage = float(input("Enter the corrected percentage: "))
                                    parts[0] = new_name 
                                    
                                    new_roll = None
                                    while new_roll is None:
                                        try:
                                            new_roll = int(input("Enter the new roll number: "))
                                            if new_roll < 1:
                                                raise ValueError("Roll number must be a positive integer.")
                                            if new_roll == line_roll_num or any(new_roll == int(p.split()[1]) for p in lines[3:]):
                                                raise ValueError("Roll number already exists.")
                                            parts[1] = new_roll
                                        except ValueError as e:
                                            print(e)
                                    print('Data updated succesfully...')
                                    break
                                except ValueError as e:
                                    print(e)
                        elif choice == 3:
                            while True:
                                try:
                                    new_percentage = float(input("Enter the corrected percentage: "))
                                    if new_percentage < 0 or new_percentage > 100:
                                        raise ValueError('Percentage must be between 0 and 100.')
                                    parts[2] = new_percentage 
                                    print('Percentage updated succesfully...')
                                    break
                                except ValueError as e:
                                    print(e)
        
                        updated_line = f"{parts[0]:<20} {parts[1]:<10} {float(parts[2]):<10.2f}\n"
                        updated_lines.append(updated_line)
                    else:
                        updated_lines.append(line)
                except (ValueError, IndexError):
                    continue
    
    if not found:
        print('----------------------')
        print("Roll number not found.")
        print('----------------------')
    
    with open("stdnt_db.txt", "w") as f:
        f.writelines(updated_lines)

def checker():
    while True:
        try:
            correction=int(input('for correction in data press 1 for exit press 2 : '))
            if correction!=1 and correction!=2:
                raise ValueError("please enter valid input ")
            elif correction==2 :
                print("terminated succesfully")
                print_data()
                break
            elif correction==1:
                while True:
                    try:
                        roll_exist()  
                        break      
                    except ValueError as e:
                        print(e)
        except ValueError as e:
                print(e)

def cntu():
      while True:
            try:
                  cntinue=int(input("press 1 for more enteries press 2 for exit : "))
                  if cntinue!=1 and cntinue!=2:
                        raise ValueError("please choose valid input")
                  elif cntinue==2:
                        print_data()
                        break
                  else:
                       stdnt_db()
            except ValueError as e:
                  print(e)
cntu()
checker()
