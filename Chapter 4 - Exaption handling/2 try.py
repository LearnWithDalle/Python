n = (input("Enter the Number For create a Table: "))
# print("this is Sample")
try:
    for i in range(1, 11):
        print(f"{int(n)} X  {i} = {int(n) * i}")
    # a = n/0
    a = int(n)/0
    print(a)
except ValueError:
    print("this is ValueError")    
except TypeError:
    print("Input ka type check ker le")
except ZeroDivisionError:
    print("zero se mut ker divide")
finally:
    print("kuch bhi ho jay but main run hunga")
    
    
print("this is Very imp")


