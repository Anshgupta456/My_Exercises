name = input("HEY USER, PLEASE ENTER YOUR NAME = ")
print("Hello" + " " + name + ", " + "WELCOME TO THE CALCULATOR APPLICATION")
print("PLEASE CHOOSE THE OPERATION, WHICH YOU WANT TO PERFORM")
thislist = ['1. Addition = Enter 1', '2. Subtraction = Enter 2', '3. Multiplication = Enter 3', '4. Division = Enter 4']
for x in thislist:
 print(x)
choice = int(input("ENTER YOUR CHOICE IN THE ABOVE FORMAT = "))
N1 = int(input("Enter 1st Number = "))
N2 = int(input("Enter 2nd Number = "))
if choice == 1:
    print("Sum = ", N1+N2)
elif choice == 2:
    print("Subtraction = ", N1-N2)
elif choice == 3:
    print("Multiplication = ", N1*N2)
elif choice == 4:
    print("Division = ", N1/N2)
else:
    print("***PLEASE ENTER VALID CHOICE***")
print("\nTHANKS FOR USING THIS CALCULATOR \n HAVE A GOOD DAY!")