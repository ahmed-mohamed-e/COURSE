
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        print("You didn't provide valid inputs.")
    else:
        return print(f"Result: {f_name + " " + l_name}".title())

first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")
format_name(first_name,last_name)