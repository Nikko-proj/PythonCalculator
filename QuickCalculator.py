def addnum(a, b):
    return a + b

def subnum(a, b):
    return a - b

def multinum(a, b):
    return a * b

def divnum(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return print("Zero division error.")

def expnum(a, b):
    return a ** b

def sqrtnum(a):
    return a ** 0.5

def quickcalculator():
    running = True
    operation = input("First pick an operation.\n"
                      "+ for addition.\n"
                      "- for subtraction.\n"
                      "* for multiplication.\n"
                      "/ for division.\n"
                      "** for exponential.\n"
                      "sqrt for square root.\n"
                      "Q or q to quit.\n")

    while running:
        if operation == "q" or operation == "Q":
                running = False
        elif operation == "+":
            val1 = int(input("Enter first number: "))
            val2 = int(input("Enter second number: "))
            print("{} + {} = {}".format(val1, val2, addnum(val1, val2)))
        elif operation == "-":
            val1 = int(input("Enter first number: "))
            val2 = int(input("Enter second number: "))
            print("{} - {} = {}".format(val1, val2, subnum(val1, val2)))
        elif operation == "*":
            val1 = int(input("Enter first number: "))
            val2 = int(input("Enter second number: "))
            print("{} * {} = {}".format(val1, val2, multinum(val1, val2)))
        elif operation == "/":
            val1 = int(input("Enter first number: "))
            val2 = int(input("Enter second number: "))
            print("{} / {} = {}".format(val1, val2, divnum(val1, val2)))
        elif operation == "**":
            val1 = int(input("Enter first number: "))
            val2 = int(input("Enter second number: "))
            print("{} ** {} = {}".format(val1, val2, expnum(val1, val2)))




def main():
    quickcalculator()


if __name__ == "__main__":
    main()
