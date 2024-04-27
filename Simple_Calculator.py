
first_value = float(input('Enter first value: '))
second_value = float(input('Enter second value: '))
operator = input('Enter operator: ')

match operator:
    case '+':
        print('Addition is', first_value + second_value)
    case '-':
        print('Subtraction is', first_value - second_value)
    case '*':
        print('Multiplication is', first_value * second_value)
    case '/':
        print('Division is', first_value / second_value)
    case _:
        print("Please enter a valid operator")
