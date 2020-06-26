while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    # for user to pick an operator above
    choice =  int (input("Choose Operater: "))
    
    if (choice>=1 and choice<=4 ): # setting num 1 & 2 variables
        num1 = int(input("1st Number: "))
        num2 = int(input("2nd Number: "))
        
        if choice == 1:
            res = num1 + num2
            print("Result = ", res)
        elif choice == '2':
            res = num1 - num2
            print("Result = ", res)
        elif choice == '3':
            res = num1 * num2
            print("Result = ", res)
        else:
            res = num1 / num2
            print("Result = ", res)
   
    elif choice == 5:
        print("Take Care..  ;)")
        break
    else:
        print("Error!! Was thvt supposed to do something?")