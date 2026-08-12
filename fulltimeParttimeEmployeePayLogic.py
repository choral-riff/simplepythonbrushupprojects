"""
Problem Statement: Write a Python program that defines an Employee base class, then creates FullTimeEmployee and PartTimeEmployee subclasses, each implementing different pay calculation logic.

Purpose: This exercise models a common HR scenario and teaches you how to use inheritance to share common attributes while allowing each subclass to define its own business logic for calculating pay.

Given Input: FullTimeEmployee("Alice", 60000) and PartTimeEmployee("Bob", 500, 20)

Expected Output:

Alice's monthly pay: 5000.0
Bob's monthly pay: 10000
"""
class Employee:
    pass

class FullTimeEmployee(Employee):
    def __init__(self, name, annualSalary):
        self.name = name 
        self.annualSalary = annualSalary
    
    def monthly_pay(self):
        monthly_pay = self.annualSalary/12
        return monthly_pay

class PartTimeEmployee:
    def __init__(self, name, hours_worked, hourly_wage):
        self.hours_worked = hours_worked
        self.hourly_wage = hourly_wage
    
    def monthly_pay(self):
        monthly_pay = self.hourly_wage*self.hours_worked
        return monthly_pay

alice = FullTimeEmployee("Alice", 60000)
bob = PartTimeEmployee("Bob", 500, 20)
print(f"Alice's monthly pay: {alice.monthly_pay()}")
print(f"Bob's monthly pay: {bob.monthly_pay()}")

    
