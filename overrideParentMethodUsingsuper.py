"""
Problem Statement: Write a Python program where a Vehicle parent class has a seating_capacity() method that accepts a capacity argument. Create a Bus child class that overrides this method to provide a default seating capacity of 50, using super() to call the parent’s version internally.

Purpose: This exercise covers method overriding and the use of super(), two key tools in OOP inheritance. Overriding lets a child class customize or extend a parent method’s behavior without rewriting it from scratch. super() delegates part of the work back to the parent, keeping the code DRY and maintaining the original logic as a foundation.

Given Input: bus = Bus("School Bus", 120)

Expected Output: School Bus seating capacity is: 50
"""

class Vehicle:
    
    def __init__(self, name, max_speed):
        self.name = name 
        self.max_speed = max_speed
        self.capacity = 4 

    def seating_capacity(self, capacity):
        self.capacity = capacity
        print(f"{self.name} seating capacity is: {self.capacity}")

class Bus(Vehicle):
    def seating_capacity(self):
        super().seating_capacity(50)
        
bus = Bus("School Bus", 120)
bus.seating_capacity()
