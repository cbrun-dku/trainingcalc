from trainingcalc.calculator import Calculator


def trainingcalc_entry_point():
    print("Welcome to the calculator!")
    print("Available operations: +, -, *, /")
    calc = Calculator()

    while True:
        try:
            operation = input("Enter an operation (+, -, *, /) or 'q' to quit: ")
            if operation.lower() == "q":
                print("Goodbye!")
                break
            a = float(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            result = calc.calculate(operation, a, b)
            print(f"The result is: {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    trainingcalc_entry_point()
