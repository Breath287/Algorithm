class Animal:
    def eat(self):
        print(1)
class dog(Animal):
    def eat(self):
        print('Dog')

class cat(Animal):
    def eat(self):
        print('Cat')

class pig(Animal):
    def eat(self):
        print('Pig')

class Bird:
    def eat(self):
        print('Bird')

def fun(creatures):
    creatures.eat()

fun(dog())
fun(cat())
fun(pig())
fun(Bird())

'''In this case, we call the behavior as polymorphism.
   It's like python only care about if objects are like the class we create
   .but we don't care if it is a real'''

