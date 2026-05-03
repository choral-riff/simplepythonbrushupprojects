import time 

print("\n \nHello, welcome to the interactive adventure story!  \n")

name = input("What shall I call you? \n")
print(f"\n Welcome {name}, let's begin this adventure, shall we? \n")

playing = input("Do you want to play? (yes/no) \n").strip().lower()

# talking the walk to the park 
def parkWalk():
    print("\n You just decided to take a walk to the park. \n")
    time.sleep(1)
    print("\n The streets are quieter, the trees are about to bloom in the spring, and you can see and hear the presence of south richmond hill folks around you. \n")
    time.sleep(1)
    print("\n You get to the park and see a group of people playing cricket, some people walking their dogs, and some people just sitting on the benches enjoying the weather. \n")
    stay = input("\n Do you want to stay and watch the cricke game (yes/no)? \n").strip().lower()
    if stay == "yes":
        print("\n You decide to stay and watch the cricket game. \n")
        time.sleep(1)
        print("\n You see some of the players are really good, and you start to feel like you want to join in on the fun. \n")
        time.sleep(1)
        print("\n You ask one of the players if you can join in, and they say yes! \n")
        time.sleep(1)
        print("\n You start playing cricket with the group, and you have a great time! \n")


# going and ordering food at the punjabi restaurant 
def punjabiRestaurant():
    pass

# going to the convenience store and choosing some snacks to buy 
def convenienceStore():
    pass

print("\n You find youself walking in a hustling, bustling Queens. \n")
print("\nYou get out of your door and find yourself in South Richmond Hill, Queens. \n")
while playing == "yes":
    print("\n So what shall we do? \n")
    print("\n1. Go on a walk to the nearest partk. \n")
    print("2. Go to the Punjabi restaurant down the street. \n")
    print("3. Go to the Elevated Convenience store and buy some snacks. \n")
    choice = input("Enter the number of your choice: \n").strip()
    if choice == "1":
        parkWalk()
    elif choice == "2":
        punjabiRestaurant()
    elif choice == "3":
        convenienceStore()
    else:
        print("\n That sounded like an invalid choice. Do you still wanna continue? \n")
        playing = input ("Enter yes or no: \n").strip().lower()
        if playing != "yes":
            print("\n Alright, see you next time! \n")
            break
        print("\n Alright, let's try again! \n")











