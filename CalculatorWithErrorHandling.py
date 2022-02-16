name = input("HEY USER, PLEASE ENTER YOUR NAME = ")
print("Hello" + " " + name + ", " + "WELCOME TO THE CALCULATOR APPLICATION")
print("PLEASE CHOOSE THE OPERATION, WHICH YOU WANT TO PERFORM")
thislist = ['1. Addition = Enter 1', '2. Subtraction = Enter 2', '3. Multiplication = Enter 3', '4. Division = Enter 4']
for x in thislist:
 print(x)
choice = int(input("ENTER YOUR CHOICE IN THE ABOVE FORMAT = "))
n1 = input("Enter 1st Number = ")
if n1.isalpha():
    raise Exception("Only Integers are Allowed")
n2 = input("Enter 2nd Number = ")
if n2.isalpha():
    raise Exception("Only Integers are allowed")
if choice == 1:
    print("Sum = ", int(n1) + int(n2))
elif choice == 2:
    print("Subtraction = ", int(n1) - int(n2))
elif choice == 3:
    print("Multiplication = ", int(n1) * int(n2))
elif choice == 4:
    '''if n2 == 0:
        raise Exception("Can't Divided By Zero")
        or 
       try:
           n2 == 0
        except ZeroDivisionError:
            print("Can't Divided By Zero")'''
    print("Division = ", int(n1) / int(n2))
else:
    print("***PLEASE ENTER VALID CHOICE***")
    
print("\nTHANKS FOR USING THIS CALCULATOR \n HAVE A GOOD DAY!")