from math import *
number = input("Enter number for create squar root: ")

try:
    if float(number) < 0:
        raise f"Negtive Number Not Allow {number}"
    ans = sqrt(float(number))
    print(f"Squar Root of {number} is: {int(ans)}")
except ValueError:
    print("Bhai type dek lee")
except TypeError:
    print("Number is not Valid")
except:
    print("Bhai kuch or hi Error aaye")
