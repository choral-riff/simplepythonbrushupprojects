import random

quotes = [
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Stay hungry. Stay foolish. – Steve Jobs",
    "Be yourself; everyone else is already taken. – Oscar Wilde",
    "Do or do not. There is no try. – Yoda",
    "It always seems impossible until it's done. – Nelson Mandela",
    "fuck yourself - me"
]

print ("\nWelcome to the quote generator")

quote = random.choice(quotes)

while True:
    print("Here is your quote: \n")
    print(quote + "\n")
    choice = input("Do you want one more quote? ('no' or 'n' to quit) ")
    if choice.strip().lower() == "no" or choice.strip().lower() == "n":
        print("Ending ")
        break


"""
further improvements to be made:
* differentiate the list of quotes into dictionary of quotes so you can store them by genres. 
* store quotes in an external text file and read them using file handling 
* add author attribution to learn string formatting 
* add delay for next quote
* create a GUI using Tkinter
* build a quote API using Flask or FastAPI
"""

    