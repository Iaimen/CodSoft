# Calculator to perform arthemetic operations

# functions for basic operations for calculator
def add(x,y):
    return x+y
def subtr(a,b):
    return a-b
def mult(c,d):
    c*d
def div(e,f):
    e/f

# Symbols to perform operations
operation={
    "+":add,
    "-":subtr,
    "*":mult,
    "/":div,
}

# Main function asking for two numbers and operation to perform between them. 
def calculator():
    a= float(input("What's the first number? "))
    for symbols in operation:
        print(symbols)
    scontinue=True

# Asking user that the program should continue? 
    while scontinue:
        o_symbol=input("Pick an operation: ")
        b= float(input("What's the second number? "))
        calculator_func=operation[o_symbol]
        answer=calculator_func(a,b)
        print(f"{a} {o_symbol} {b} = {answer}")
        if input(f"Type 'y' to continue with {answer} or type 'n' to start a new operation ")=='y':
            a=answer
        else:
           scontinue=False
           calculator()
calculator()      # calling function