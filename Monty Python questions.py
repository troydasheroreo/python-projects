print("Hello World")

name = input("What is your name? ")
print("Hello " + name)

quest = input("What is your quest")
print("Your quest is " + quest)

while True:
	color = input("What is your favorite color? ")
	print("Your favorite color {}!".format(quest))

	if color == "blue":
		print("My favorite color is "+ color +", no wait")
		print("You get flung off the edge of the cliff")
		break
	elif color == "yellow":
		print("My favorite color is "+ color)
		print("Okay move along")
		break

	else:
		print("Is that Assyrian?")

