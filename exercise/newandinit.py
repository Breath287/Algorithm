class Person:
    def __new__(cls, *args, **kwargs):
        print('__new__method is called and its id: {0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('the id of new obj is {0}'.format(id(obj)))
        return obj

    def __init__(self, name, age):
        print('__init__ method is called and its id: {0}'.format(id(self)))
        self.name = name
        self.age = age

print('The id of object is {0}'.format(id(object)))

print('The id of person is {0}'.format(id(Person)))

p1 = Person('Jie Li', 25)
print('The id of p1 is {0}'.format(id(p1)))






