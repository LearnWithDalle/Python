class Parent:
    def func1(self):
        print("This function is in parent class.")
class Child1 (Parent):
    def func2(self):
        print("This function is in child 1.")
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")
class Child3(Parent):
    def func4(self):
        print("This function is in child 3.")

object1 = Child1()
object2 = Child2()
object3 = Child3()

object1.func1()
object1.func2()
object2.func1()
object2.func3()
object3.func1()
object3.func4()