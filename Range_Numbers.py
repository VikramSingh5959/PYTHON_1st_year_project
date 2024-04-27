start_val = int(input("Enter starting number : "))
end_val = int(input("Enter ending point : "))
step = int(input("Enter step value : "))
choice_vertical = int(input("Enter 1 for vertical result or 2 for horizontal result : "))
choice_order = int(input("Enter 1 for forward order or 2 for reverse order : "))

if step < 0:
    print("Enter a positive value")
else:
    if start_val <= end_val:
        if choice_order == 1 and (choice_vertical == 1 or choice_vertical == 2):
            if choice_vertical == 1:
                print("Forward order in vertical ")
            else:
                print("Forward order in horizontal ")
            for i in range(start_val, end_val + 1, step):
                if choice_vertical == 1:
                    print(i)
                elif choice_vertical == 2:
                    print(i, end=" ")
                else:
                    print("Enter valid choices")
        elif choice_order == 2 and (choice_vertical == 1 or choice_vertical == 2):
            if choice_vertical == 1:
                print("Reversed order in vertical ")
            elif choice_vertical == 2:
                print("Reversed order in horizontal ")
            for i in range(end_val, start_val, -step):
                if choice_vertical == 1:
                    print(i)
                elif choice_vertical == 2:
                    print(i, end=" ")
                else:
                    print("Enter valid choices")
        else:
            print("Enter valid choice of order of printing ")
    else:
        if choice_order == 1 and (choice_vertical == 1 or choice_vertical == 2):
            if choice_vertical == 1:
                print("Forward order in vertical ")
            elif choice_vertical == 2:
                print("Forward order in horizontal ")
            for i in range(end_val, start_val + 1, step):
                if choice_vertical == 1:
                    print(i)
                elif choice_vertical == 2:
                    print(i, end=" ")
                else:
                    print("Enter valid choices")
        elif choice_order == 2 and (choice_vertical == 1 or choice_vertical == 2):
            if choice_vertical == 1:
                print("Reversed order in vertical ")
            else:
                print("Reversed order in horizontal ")
            for i in range(start_val, end_val, -step):
                if choice_vertical == 1:
                    print(i)
                elif choice_vertical == 2:
                    print(i, end=" ")
                else:
                    print("Enter valid choices")
        else:
            print("Enter valid choices")

print("\nProgram completed. Exiting now...")
