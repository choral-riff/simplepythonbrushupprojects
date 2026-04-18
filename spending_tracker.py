"""
two methods used;
log_expenses() and view_expenses()
using with open() as file to to do file handling 
"""

def log_expenses():
    while True:
        item = input("Enter the item purchased (or type 'done' to finish): ")
        if "done" in item.strip().lower():
            break
        amount = input("Enter the amount spent on this item: ")
        with open("expenses.txt", "a") as file:
            file.write(f"{item} : ${amount}\n")
    
    print("Expneses logged successfully!")

def view_expenses():
    with open("expenses.txt", "r") as file:
        print(file.read())


log_expenses()
view_expenses()


