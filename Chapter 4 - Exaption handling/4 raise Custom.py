# for Licence
age = int(input("Enter age for Checking Ur eligibal for Driving:"))

def eligible(x):
    if x < 0:
        raise TypeError ("tum gadde ho dalle")

    else:
        print("this is Work")

eligible(age)