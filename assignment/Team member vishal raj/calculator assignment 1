def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:

    opt = input("Enter your option(1/2/3/4): ")


    if opt in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if opt == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif opt == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif opt == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif opt == '4':
            print(num1, "/", num2, "=", divide(num1, num2))


        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")
