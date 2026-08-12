"""
Problem Statement: Write a Python program that defines an Animal base class with a speak() method, then overrides it in Dog and Cat subclasses to return their respective sounds.

Purpose: This exercise introduces method overriding, one of the core pillars of polymorphism in OOP. It shows how different subclasses can share the same interface but provide their own specific behaviour.

Given Input: Objects of Dog and Cat classes

Expected Output:

Dog says: Woof!
Cat says: Meow!
"""

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

doggo = Dog()
print(f"Dog says: {doggo.speak()}")
catto = Cat()
print(f"Cat says: {catto.speak()}")
