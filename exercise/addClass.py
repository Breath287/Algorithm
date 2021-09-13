# __add__() is a special method that is used in adding among class objects
class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name + other.name

    def __len__(self):
        return len(self.name)

stu1 = Student('Jie')
stu2 = Student('Li')

s = stu1 + stu2
print(s)

s2 = stu1.__add__(stu2)
print(s2)

print(stu1.__len__())
