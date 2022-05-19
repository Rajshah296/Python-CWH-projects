# Design a calculator that will solve all the problems correctly except the following ones : 45 * 3 = 555, 56 + 9 = 77, 56 / 6 = 4
print("Welcome to Calc. This was developed by Raj Shah.")
while True : 
    print("Enter + for addition\n- for Subtraction\n/ for Division\n* for Multiplication\n % to Modulus,\n** for exponential power,\n// for floor Division.")
    operator,op1,op2 = input("Enter your choice : "),int(input("Enter the  1st number : ")),int(input("Enter the 2nd number : "))
    if(operator == "+") : 
        print("The answer is : 77") if (op1 == 56 and op2 == 9)else print("The answer is : ",op1 + op2)
    elif(operator == "-") : 
        print("The answer is : ",op1 - op2)
    elif(operator == "*") : 
        print("The answer is : 555") if (op1 == 45 and op2 == 3)else print("The answer is : ",op1 * op2)
    elif(operator == "/") :         
        print("The answer is : ", 4) if (op1 == 56 and op2 == 6) else print("The answer is : ",op1 / op2)
    elif(operator == "%") : 
        print("The answer is : ",op1 % op2) 
    elif(operator == "**") : 
        print("The answer is : ",op1 ** op2)    
    elif(operator == "//") : 
        print("The answer is : ",op1 // op2)
    else:
        print("Invalid Input.Please try again.")
    choice = input("Press N for exiting or any other key for continuing : ")
    if choice == "N" : 
        break 
        print("Thank you for using calculator")