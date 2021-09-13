
def main():
    while True:
        mainmenu()
        choice = int(input('Please choose a sequence to start: '))
        if choice in [1, 2, 3, 4, 5, 6, 7, 0]:
            if choice == 0:
                answer = input('Are you sure to quit the system? Yes/No: ')
                if answer.upper() == 'YES':
                    print("Thanks for use!")
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                rank()
            elif choice == 6:
                collect()
            elif choice == 7:
                display()
            else:
                print('Wrong input, please try again!')

def mainmenu():
    print('=========================Student Information Management System=========================')
    print('-----------------------------------Function List---------------------------------------')
    print('\t\t\t\t\t\t\t1. Registrar')
    print('\t\t\t\t\t\t\t2. Inquire')
    print('\t\t\t\t\t\t\t3. Delete')
    print('\t\t\t\t\t\t\t4. Modify')
    print('\t\t\t\t\t\t\t5. Rank')
    print('\t\t\t\t\t\t\t6. collect')
    print('\t\t\t\t\t\t\t7. Display')
    print('\t\t\t\t\t\t\t0. Quit')
    print('---------------------------------------------------------------------------------------')

def insert():
    student_list = []
    while True:
        id = input('Please input the ID: ')
        if not id:
            break
        name = input('Please input the NAME: ')
        if not name:
            break

        try:
            english = float(input('Please input the English score: '))
            python = float(input('Please input the python score: '))
            java = float(input('Please input the java score: '))
        except:
            print('Wrong input, try again!')
            continue

        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        student_list.append(student)
        answer = input('Continue or not? Yes/No: ')
        if answer.upper() == 'YES':
            continue
        else:
            break

    save(student_list)
    print('Finish inserting student information!')

def save(lst):
    try:
        student_file = open(r'student.txt', 'a', encoding='utf-8')
    except:
        student_file = open(r'student.txt', 'w', encoding='utf-8')
    for item in lst:
        student_file.write(str(item) + '\n')
    student_file.close()

def search():
    pass

def delete():
    pass

def modify():
    pass

def rank():
    pass

def collect():
    pass

def display():
    pass

if __name__ == '__main__':
    main()






