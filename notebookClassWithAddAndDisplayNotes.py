"""
Problem Statement: Write a Python program to create a Notebook class that maintains an internal list of notes. Add an add_note(note) method that appends a new note to the list, and a show_notes() method that prints all stored notes.

Purpose: This exercise shows how a class can manage a growing collection of data over its lifetime. It practices initializing a mutable data structure inside __init__ and writing methods that both modify and read that structure, a pattern that appears in todo lists, message queues, logs, and many other applications.

Given Input: Add three notes: "Buy groceries", "Read a book", "Call the doctor".

Expected Output:

1. Buy groceries
2. Read a book
3. Call the doctor
"""
class Notebook:
    def __init__(self):
        self.storedNotes = []
    
    def add_note(self, note):
        self.storedNotes.append(note)
    
    def show_notes(self):
        for note in self.storedNotes:
            print(note)

nb = Notebook()
nb.add_note("Buy groceries")
nb.add_note("Read a book")
nb.add_note("Call the doctor")
nb.show_notes()
