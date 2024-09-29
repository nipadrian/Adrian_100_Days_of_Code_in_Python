import art


def add(n1, n2):
#    return int(n1) + int(n2)
    return n1 + n2
def subtract(n1, n2):
#    return int(n1) - int(n2)
    return n1 - n2
def multiply(n1, n2):
#    return int(n1) * int(n2)
    return n1 * n2
def divide(n1, n2):
#    return int(n1) / int(n2)
    return n1 / n2


calc_key = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(art.logo)
    calc_continue = True
    choice = ""
    result = 0

    num_1 = float(input("Please enter the first number"))

    while calc_continue:

        operator = input("Please enter the mathematical operator of '+', '-', '*', '/'")
        num_2 = float(input("Please enter the second number"))

    #print(calculator["*"](n1=3,n2=5))

        result = calc_key[operator](n1=num_1,n2=num_2)
        print(f"{num_1} {operator} {num_2} = {result}")

        choice = input(f"Type 'y' if you want to continue calculating with {result}, or type 'n' to start a new calculation").lower()
        if choice == "y":
            num_1 = result
        else:
            calc_continue = False
            print("\n"*20)
            calculator()
calculator()
# TODO: Write out the other 3 functions - subtract, multiply and divide.
# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.