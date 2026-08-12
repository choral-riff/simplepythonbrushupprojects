"""
Problem Statement: Write a Python program that defines a Media base class, then creates Book, Magazine, and DVD subclasses, each with type-specific attributes and a describe() method.

Purpose: This exercise shows how inheritance can model a taxonomy of related objects. Each media type shares a common identity (title, price) but carries unique attributes specific to its format, reflecting real-world library or inventory systems.

Given Input: Book("Clean Code", 499, "Robert C. Martin"), Magazine("Wired", 150, "Monthly"), DVD("Inception", 299, 148)

Expected Output:

Book: Clean Code by Robert C. Martin - Rs.499
Magazine: Wired (Monthly) - Rs.150
DVD: Inception, 148 mins - Rs.299
"""
class Media:
    pass

class Book(Media):
    def __init__(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author
    
    def describe(self):
        print(f"Book: {self.title} by {self.author} - Rs. {self.price}")

class Magazine(Media):
    def __init__(self, title, price, issued):
        self.title = title
        self.price = price 
        self.issued = issued 
        
    def describe(self):
        print(f"Magazine: {self.title} ({self.issued}) - Rs.{self.price}")

class DVD(Media):
    def __init__(self, title, price, length):
        self.title = title
        self.price = price
        self.length = length
    
    def describe(self):
        print(f"DVD: {self.title}, {self.length} mins - Rs.{self.price}")

b1, m1, d1 = Book("Clean Code", 499, "Robert C. Martin"), Magazine("Wired", 150, "Monthly"), DVD("Inception", 299, 148)
b1.describe()
m1.describe()
d1.describe()
