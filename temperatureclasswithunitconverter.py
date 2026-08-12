"""
Problem Statement: Write a Python program to create a Temperature class that stores a temperature in Celsius. Add two methods: to_fahrenheit() that converts and returns the value in Fahrenheit, and to_kelvin() that converts and returns the value in Kelvin.

Purpose: This exercise demonstrates how a class can act as a data container with built-in conversion logic. It reinforces writing multiple methods that all operate on the same instance attribute, and applies straightforward mathematical formulas in a practical scientific context.

Given Input: t = Temperature(100)

Expected Output:

Celsius: 100
Fahrenheit: 212.0
Kelvin: 373.15
"""
class Temperature:
    def __init__(self, temperatureInCelsius):
        self.temp = temperatureInCelsius
    
    def to_fahrenheit(self):
        fahrenheit = ((self.temp*180)/100) + 32
        return fahrenheit
    
    def to_Kelvin(self):
        kelvin = self.temp + 212
        return kelvin 

t = Temperature(100)
print(f"Celsius: {t.temp}")
print(f"Fahrenheit: {t.to_fahrenheit()}")
print(f"Kelvin: {t.to_Kelvin()}")
