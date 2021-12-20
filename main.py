#functions with outputs 
def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "Invalid input"
  return f_name.capitalize() + " " + l_name.capitalize()
print(format_name(input("What is your first name? "), input("What is your last name? ")))

