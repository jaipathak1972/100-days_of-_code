#Calculator
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
num1 = float(input("What's the first number?: "))

for symbol in operations:
    print(symbol)
while True:

    operation_symbol = input("Pick an operation: ") 
    num2 = float(input("What's the next number?: "))

    calculation_function = operations[operation_symbol]
    first_answer = int(calculation_function(num1, num2))

    print(f"{num1} {operation_symbol} {num2} = {first_answer}")
    
    
    if input("Enter 'y' to cotinue or else 'n' ") == "y":
       num1 = first_answer
    else:
       break
    
        




# print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
