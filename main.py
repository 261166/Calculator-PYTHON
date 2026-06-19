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

    if choice == 1:
        num1 = int(input("Type in the first number:\n"))
        num2 = int(input("Type in the second number:\n"))
        answer = int(add(num1, num2))
        print("The answer:\n", num1, "+", num2, "=", answer, "\n")

    elif choice == 2:
        num1 = int(input("Type in the first number:\n"))
        num2 = int(input("Type in the second number:\n"))
        answer = int(sub(num1, num2))
        print("The answer:\n", num1, "-", num2, "=", answer, "\n")

    elif choice == 3:
        num1 = int(input("Type in the first number:\n"))
        num2 = int(input("Type in the second number:\n"))
        answer = int(mul(num1, num2))
        print("The answer:\n", num1, "*", num2, "=", answer, "\n")

    elif choice == 4:
        num1 = int(input("Type in the first number:\n"))
        num2 = int(input("Type in the second number:\n"))
        answer = div(num1, num2)
        if num2 != 0:
            print("The answer:\n", num1, "/", num2, "=", answer, "\n")
        else:
            print(answer, "\n")

    elif choice == 0:
        print("Goodbye")
        calc_on = 0