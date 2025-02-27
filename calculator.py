# This is a calculator app that takes two numbers as input and an operator and performs the arithmetic operation.



def calculator():

    try:
        first_num = int(input("Please give the first number: "))  # Taking the first input.
    except:
        print("Please give a number")
        return
    try:   
        second_num = int(input("Please give the second number: "))  # Taking the first input.
    except:
        print("Please give a valid number")
        return

    operator = input("Please provide the operator/sign: ")  # Taking the operator

    if operator == "+":
        result = first_num + second_num
    elif operator =="-":
        result = first_num - second_num
    elif operator == "*":
        result = first_num * second_num
    elif operator == "/":
        result = first_num/second_num
    else:
        return "Please provide a valid operator (+, -, * or /)" 

    return result  

print(calculator())  
