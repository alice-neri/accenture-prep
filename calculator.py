print("Simple Calculator")

def add(a, b): #addition
    return a + b

def sub(a, b): #subtraction
    return a - b

def mult(a, b): #multiplication
    return a * b

def div(a, b): #division
    if b == 0:
        return "Error: cannot divide by zero"
    else:
        return a / b

while True:
    a = float(input("Input a: "))
    b = float(input("Input b: "))
    act = input("Would you like to add, subtract, multiply, or divide (+, -, * or /)? ") #act = action

    if act == "+":
     res = add(a, b)
    elif act == "-":
        res = sub(a, b) 
    elif act == "*":
        res = mult(a, b)
    elif act == "/":
        res = div(a, b)
    else:
        res = "Invalid operation"

    answer = input(f"{res} is your answer. Would you like to continue? (y/n): ")
    if answer == "n":
        break
