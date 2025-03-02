print("Welcome to pizza_land... ")
print("S for small size\nM for medium size\nL for large size")
database = {"S":15,"M":20,"L":25}
total = 0
while True:
    size = input("Enter your choice: ").upper()
    if size in database.keys():
        total += database[size]
        break
    else:
        print("Enter a valid choice...")
if size == "S":
    add_pepperoni = input("Do you wanna add pepperoni (Y or N): ").upper()
    if add_pepperoni == "Y":
        total += 2
    else:
        pass
elif size == "M":
    add_pepperoni = input("Do you wanna add pepperoni (Y or N): ").upper()
    if add_pepperoni == "Y":
        total += 3
    else:
        pass
else:
    pass
extra_cheese = input("Do you wanna add extra cheese (Y or N): ").upper()
if extra_cheese == "Y":
    total += 1
else:
    pass
print(f"Total is ${total}")
print("You are welcomed anytime(^_^)")
EXIT = input()