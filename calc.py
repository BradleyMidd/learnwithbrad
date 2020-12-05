# Basic Calculator
action = True

while action:
    num1 = int(input("Type a number: "))
    info = input("Do you want to add, subtract, multiply or divide? \nType [+], [-], [*] or [/]: ")
    num2 = int(input("Type a second number: "))

    if info == "+":
        print(num1 + num2)

    elif info == "-":
        print(num1 - num2)

    elif info == "*":
        print(num1 * num2)

    elif info == "/":
        print(num1 / num2)

    else:
        print("Invalid input")
        action = False