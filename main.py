#functions with outputs 
# def format_name(f_name, l_name):
#   if f_name == "" or l_name == "":
#     return "Invalid input"
#   return f_name.capitalize() + " " + l_name.capitalize()
# print(format_name(input("What is your first name? "), input("What is your last name? ")))


#find number of days in month
# check if it's a leap year
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return "yes"
      else:
        return "no"
    else:
      return "yes"
  else:
    return "no"
# days in month
def days_in_month(the_year, the_month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if is_leap(the_year) == "yes" and the_month == 2:
    return 29
  else:
    return  month_days[the_month - 1]
# user input
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)