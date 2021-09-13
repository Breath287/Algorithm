file = open('/Users/jieli/Desktop/a.txt','r')
print(file.readlines())
file.close()

file = open('/Users/jieli/Desktop/a.txt', 'a')
file.write('age:25')
file.close