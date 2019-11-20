def get_user_operation_choice():
  choice = ""
  while choice == "":
    try:
      choice = int(input("Enter the corresponding number of the operation you want to perform: "))
      if choice < 1 or choice > 6:
        print("\n" + "Please enter a number listed in the options.")
        choice = ""
    except ValueError:
      print("\n" + "That's not a number. Please enter a number: ")
  return choice

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

def remainder(x, y):
  return x % y

def exponent(x, y):
  return x ** y

print("Choose whether you want to:" + "\n" + "1. Add two numbers" + "\n" + "2. Subtract two numbers" + "\n" + "3. Multiply two numbers" + "\n" + "4. Divide two numbers" + "\n" + "5. Find the remainder when dividing two numbers" + "\n" + "6. Find a number raise to the power of another number" + "\n")
user_operation = get_user_operation_choice()

num1 = float(input("\n" + "Enter your first number: "))
num2 = float(input("Enter your second number: "))

if user_operation == 1:
  print("\n" + f"{num1} + {num2} = {add(num1, num2)}")
elif user_operation == 2:
  print("\n" + f"{num1} - {num2} = {subtract(num1, num2)}")
elif user_operation == 3:
  print("\n" + f"{num1} * {num2} = {multiply(num1, num2)}")
elif user_operation == 4:
  print("\n" + f"{num1} / {num2} = {divide(num1, num2)}")
elif user_operation == 5:
  print("\n" + f"The remainder when dividing {num1} by {num2} is {remainder(num1, num2)}.")
elif user_operation == 6:
  print("\n" + f"{num1} raised to the power of {num2} is {exponent(num1, num2)}.")