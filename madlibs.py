print("Follow along, this is going to be fun!")
time = input("Enter a number from 1 to 12:  ")
items = input("Enter a noun in plural form:  ")
name = input("Enter a name:  ")
scream = input("Enter a weird sentence:  ")
action = input("Enter a verb:  ")

print("""
	It was %s o'clock when I heard a knock at the door.
	I opened the door and there was a box full of %s with a note saying "From Mr. %s."
	Just as I closed the door I heard a scream "%s."
	I froze in place and all I could do was %s.""" % (time, items, name.title(), scream.upper(), action))