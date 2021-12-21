#functions with outputs 

# def format_name(f_name, l_name):
#   if f_name == "" or l_name == "":
#     return "Invalid input"
#   return f_name.capitalize() + " " + l_name.capitalize()
# print(format_name(input("What is your first name? "), input("What is your last name? ")))


#find number of days in month

# check if it's a leap year
# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return "yes"
#       else:
#         return "no"
#     else:
#       return "yes"
#   else:
#     return "no"
# # days in month
# def days_in_month(the_year, the_month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
#   if is_leap(the_year) == "yes" and the_month == 2:
#     return 29
#   else:
#     return  month_days[the_month - 1]
# # user input
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)


#calculator

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
running = True
num1 = int(input("What's the first number?: "))
while running:
  num2 = int(input("What's the second number?: "))
  op = input("Do you want to add, subtract, multiply, or divide? ")
  if op == "add" or op == "+":
    op = "+"
  elif op == "subtract" or op == "-":
    op = "-"
  elif op == "multiply" or op == "*":
    op = "*"
  elif op == "divide" or op == "/":
    op = "/"
  else:
    print("Invalid input")
  function = operations[op]
  num3 = function(num1, num2)
  print(num3)
  cont = input(f"Type 'y' to continue calculating with {num3} or type 'n' to exit. ")
  if cont == "y":
    num1 = num3
  else:
    running = False
    print("Goodbye.")
