import string
import random


## characters to generate password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
	## length of password from the user
	length = input("Enter Length Of Password")
        if length > 0 and length < 50
	    ## shuffling the characters
	    random.shuffle(characters)
	
	    ## picking random characters from the list
	    password = []
	    for i in range(length):
		password.append(random.choice(characters))

	    ## shuffling the resultant password
	    random.shuffle(password)

	    ## converting the list to string
	    ## printing the list
	    print("".join(password))
            print(len(password))
        else:
            length = input("Enter Length Of Password")


## invoking the function
generate_random_password()
