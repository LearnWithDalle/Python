# Create a randome Password Genreter
# import Randome
import random
# getting our charecters
lower = "abcdefghijklmnopqrstuvwxyz"
upperCase = lower.upper()
symbol = "~!@#$%^^&*())_+=-"
number = "0123456789"
all = lower + upperCase + symbol + number;

# length of pass
length = 10
# OR
# length = int(input("Enter the Length of the Password"))

# pass save here
password = ""
for _ in range(length):
    password = "".join([password, random.choice(all)])

print(password)