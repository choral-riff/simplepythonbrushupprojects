"""
Problem Statement: Write a Python program that creates a Vehicle parent class with a base fare, then extends a Taxi child class that adds a 10% maintenance fee on top of the base fare using super().

Purpose: This exercise teaches you how to use super() to call the parent class constructor, extend child class behaviour by building on inherited attributes, and model real-world pricing logic using inheritance.

Given Input: base_fare = 500

Expected Output: Total fare with maintenance fee: 550.0
"""
class Vehicle:
    def __init__(self, base_fare):
        self.base_fare = base_fare
    
class Taxi(Vehicle):
    def __init__(self, base_fare):
        super().__init__(base_fare)
        self.maintenance_fee = base_fare*0.10
        self.total_fare = self.base_fare + self.maintenance_fee

cab = Taxi(500)
print(f"Total fare with maintenance fee: {cab.total_fare}")
