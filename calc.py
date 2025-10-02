while True:
    try:
        z=int(input("Press 1:Add, 2:Subtract, 3:Product, 4:Division, 5:Exit: "))
        if z==5:
            print("Thanks for using the calculator")
            break
        if z<1 or z>5:
            print("Enter valid option from menu")
            continue
        x=float(input("Enter the first number: "))
        y=float(input("Enter the second number: "))
        
        if z==1:
            print("Result:",x+y)
        elif z==2:
            print("Result:",x-y)
        elif z==3:
            print("Result:",x*y)
        elif z==4:
            print("Result:",x/y)
        else:
            print("Invalid Value")
    except ZeroDivisionError:
        print("Division by 0 isn't allowed")
    except ValueError:
        print("Enter valid value")
    except KeyboardInterrupt:
        print("Thanks for using the calculator")
        break
