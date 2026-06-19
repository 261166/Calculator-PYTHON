def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "You are not allowed to divide by 0!"

print("Welcome to the calculator")
calc_on = 1

while calc_on != 0:

    choice = int(input("What operation would you like to perform?\nSum - type '1'\nSubtraction - type '2'\nMultiplication - type '3'\nDivision - type '4'\nExit - 0\n"))

    if choice == 0:
        print("Goodbye")
        calc_on = 0
    else:
        num1 = int(input("Type in the first number:\n"))
        num2 = int(input("Type in the second number:\n"))

        if choice == 1:
            print("The answer:\n", num1, "+", num2, "=", int(add(num1, num2)), "\n")

        elif choice == 2:
            print("The answer:\n", num1, "-", num2, "=", int(sub(num1, num2)), "\n")

        elif choice == 3:
            print("The answer:\n", num1, "*", num2, "=", int(mul(num1, num2)), "\n")

        elif choice == 4:
            if num2 != 0:
                print("The answer:\n", num1, "/", num2, "=", div(num1, num2), "\n")
            else:
                print(div(num1, num2), "\n")

