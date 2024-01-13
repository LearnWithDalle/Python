class animal:
    def eat(self):
        print("Eating..........")
class Dog(animal):
    def bark(self):
        print("Barking...... Bhau Bhau ")
class BabyDog(Dog):
    def weep(self):
        print("Weeping........")
        

d =BabyDog()
d.eat()
d.bark()
d.weep()