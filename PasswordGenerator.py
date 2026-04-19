import random # library to perform shuffling or sampling operations
import secrets # library to generate number sequences

#Beginner Project One - Password Generator      

#Declaring variables
lower = "abcdefghijklmnopqrstuvwxyz" 
upper = "ABCDEFGHIJKLMNOQRSTUVWXYZ"
numerical = "01234567890"
character = "!@#$%^&*()?/"

#Defining Output
string = lower + upper + numerical + character
length = 16
Password = "".join(random.sample(string,length))

#Final Output: Random Password
print("Your new password is: " + Password )

