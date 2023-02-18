
#list of operators used in calculator
operatorsList = ["+", "-", "*", "/", "%", "^" ]


keepCalculating = True


#calculator funcion that performs all the necessary operations
def calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    if operation == '-':
        return num1 - num2
    if operation == '*':
        return num1 * num2
    if operation == '/':
        return num1 / num2
    if operation == '%':
        return num1 % num2
    if operation == '^':
        return num1 ** num2
    

#function that takes input form user and checks if it's valid and then performs
#operations using calculator function
def calculation():    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Enter the operator (+, -, *, /, %, ^): ")
            if operation not in operatorsList:
                raise ValueError
            break
        except ValueError:
            print("Invalid input")
    result = calculator(num1, num2, operation)
    print("The result is: ", result)


#while True loop for performing endless operations, unless the user wants to exit
while keepCalculating:

    calculation()

    #user input if they want to exit or perform another operation
    newCal = input("Do You want to make a new calculation? (y/n)").lower()
    
    if newCal == "n" : 
        keepCalculating = False

#exit message
print("Thank You for using my calculator")




