"""
Student Class with Average Grade
Problem Statement: Write a Python program to create a Student class that stores a student’s name and a list of marks. Add a method average() that calculates and returns the average of all marks.

Purpose: This exercise shows how instance attributes can store complex data types such as lists, not just simple values. It also practices combining OOP with list operations and arithmetic, a pattern common in gradebooks, dashboards, and reporting tools.

Given Input: s1 = Student("Alice", [85, 90, 78, 92, 88])

Expected Output: Alice's Average Grade: 86.6
"""
class Student:
    
    def __init__(self, name:str, marks:list[int]):
        self.name = name 
        self.marks = marks 
    
    def average(self):
        sum = 0
        n = len(self.marks)
        print(f"n:{n}")
        for mark in self.marks:
            sum = sum + mark
        print(f"sum: {sum}")
        mean = sum/n
        print(f"mean: {mean}")
        return f"{self.name}'s Average Grade: {mean}"

s1 = Student("Alice", [85, 90, 78, 92, 88])
print(s1.average())
