def chatbot():
    print("Hello! I am a dumb chatbot. Type 'bye' to end our conversation!")

    #you can change the while True section to add some personality
    while True:
        message = input("You: ")
        if message.strip().lower()== "bye":
            print("Chatbot: Goodbye! It was nice talking to you.")
            break #breaks the while loop and ends the conversation
        elif "how are you" in message.strip().lower():
            print("Chatbot: I'm so dumb that I am always confused and so maybe... wait i am confused.")
        elif "name" in message.strip().lower():
            print("i am a dumb chatbot, i for got my name, what's name mean anyway?")
        else:
            print("huh?... oh!!! AHHHH!!!!..... yes i understand... wait no i don't understand... i am dumb...")

chatbot()