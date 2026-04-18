print("Welcome to the temperature converter.")

def printMenu():
	print("Here are your options: \n")
	print("1. C to F")
	print("2. F to C")
	print("3. C to K")
	print("4. K to C")
	print("5. F to K")
	print("6. K to F")
	print("7. Quit")


def one_c2f(c):
	f = ((9*c)/5) + 32
	print (f"the temperature {c} degree Celsius is equal to {f} degree Fahrenheit")

def two_f2c(f):
	c = (5/9)*(f-32)
	print(f"the temperature {f} degree Fahrenheit is equal to {c} degree Fahrenheit")

def three_c2k(c):
	k = c + 212
	print(f"the temperature {c} degree Celsius is equal to {k} Kelvin")

def four_k2c(k):
	c = k - 212
	print(f"the temperature {k} Kelvin is equal to {c} degree Celsius")

def five_f2k(f):
	k = ((5/9)*(f-32)) + 212
	print(f"the temperature {f} degree Fahrenheit is equal to {k} Kelvin")

def six_k2f(k):
	f = ((9/5)*(k-212)) + 32
	print(f"the temperature {k} Kelvin is equal to {f} degree Fahrenheit")


def runProgram():
	while True: 
		printMenu()
		choice = input("Input the number for the option. (For ex: 5 for Fahrenheit to Kelvin) : ")
		if choice == "7":
			print("Ending Program...")
			break

		tem = input("Input the temperature in numbers that you want to convert. ")

		if choice == "1":
			one_c2f(int(tem))
		elif choice == "2":
			two_f2c(int(tem))
		elif choice == "3":
			three_c2k(int(tem))
		elif choice == "4":
			four_k2c(int(int(tem)))
		elif choice == "5":
			five_f2k(int(tem))
		elif choice == "6":
			six_k2f(int(tem))


#start of the program
runProgram()




