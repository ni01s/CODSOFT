print("BASIC CALCULATOR")

while True:
    num1=int(input("enter first number: "))
    num2=int(input("enter second number: "))

    print("Select Operations")
    print("1. Addition\n"
        "2. Subtraction\n"
        "3. Multiplication\n"
        "4. Division\n")

    op = int(input("Enter choice for operation: "))

    if op== 1:
        print("RESULT: "+ str(num1+num2))
    elif op == 2:
        print("RESULT: "+ str (num1-num2))
    elif op== 3:
        print("RESULT: "+str (num1*num2))
    elif op == 4:
        print("RESULT: "+ str (num1/num2))
    else:
        print("INVALID CHOICE")
    
    calculate_again=input("Do you want to perform another calculation?\nPlease select- y/n: ")
    if calculate_again.lower() != "y":
        break
