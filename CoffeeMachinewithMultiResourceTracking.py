"""
Problem Statement: Write a Python program to create a CoffeeMachine class that tracks three resource attributes: water, coffee, and milk (in ml/g). Add a make_latte() method that checks whether sufficient resources are available, deducts them if so, and prints an appropriate message in either case.

Purpose: This exercise combines state management, resource tracking, and conditional logic inside a single class. It mirrors how real-world stateful systems (vending machines, inventory systems, game resource managers) check preconditions before executing an action and update their internal state only when the action is valid.

Given Input: CoffeeMachine(water=300, coffee=100, milk=200). A latte requires 200ml water, 20g coffee, and 150ml milk.

Expected Output:

Latte made! Remaining - Water: 100ml, Coffee: 80g, Milk: 50ml
Not enough resources to make a latte.
"""
class CoffeeMachine:
    def __init__(self, water, coffee, milk):
        self.water = water
        self.coffee = coffee
        self.milk = milk 
    
    def make_latte(self):
        #requires 200 ml of water
        #requires 20g of coffee
        #requires 150ml of milk 
        if (self.water < 200 or self.coffee < 20 or self.milk < 150):
            print("Not enough sources to make a latte.")
        else:
            self.water = self.water - 200
            self.coffee = self.coffee - 20
            self.milk = self.milk - 150 
            print(f"Latte made! Remaining - Water: {self.water}, Coffee: {self.coffee}, Milk: {self.milk}")

keurig = CoffeeMachine(water = 300, coffee = 100, milk = 200)
keurig.make_latte()
keurig.make_latte()
