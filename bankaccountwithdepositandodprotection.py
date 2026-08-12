"""
Bank Account with Deposit & Overdraw Protection
Problem Statement: Write a Python program to create a BankAccount class with a balance attribute and two methods: deposit(amount) that adds funds to the balance, and withdraw(amount) that deducts funds but prevents the balance from going below zero.

Purpose: Learn data validation and conditional logic inside instance methods. Preventing overdraw is a real-world business rule, and implementing it here teaches you how classes can enforce constraints on their own data, a core idea behind encapsulation in OOP.

Given Input: Starting balance of 1000, deposit 500, withdraw 200, then attempt to withdraw 2000.

Expected Output:

Balance after deposit: 1500
Balance after withdrawal: 1300
Insufficient funds. Current balance: 1300
"""
class BankAccount:
    def __init__(self, balance):
        self.balance = balance 
    
    def deposit(self, amount):
        self.balance = self.balance + amount 
        print(f"Balance after deposit: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds. Current balance: {self.balance}")
        else:
            self.balance = self.balance - amount 
            print(f"Balance after withdrawal: {self.balance}")
            
myAccount = BankAccount(1000)
myAccount.deposit(500)
myAccount.withdraw(200)
myAccount.withdraw(2000)
