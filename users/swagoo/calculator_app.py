def calculator():
    
    first_digit = int(input('Please enter a first digit: '))

    second_digit = int(input('Please enter a second digit: '))    

    operator_selected = input('Please enter a operator: ')
    if operator_selected == "+":
        print(first_digit+second_digit)
    elif operator_selected == "-":
        print(first_digit-second_digit)
    elif operator_selected == "*":
        print(first_digit*second_digit)
    elif operator_selected == "/":
        print(first_digit/second_digit)
    else:
        print("Please select a correct operator")


#################################################################

calculator()
