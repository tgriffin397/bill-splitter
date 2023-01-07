import random
import random as r


lucky_person = ''
n_people = 0
bill_value = 0
names = {}


def input_number_people():
    global n_people

    print('Enter the number of friends joining (including you):')
    n_people = int(input())
    if n_people <= 0:
        print('No one is joining for the party')
        quit()


def input_bill_value():
    global bill_value

    print('Enter the total bill value:')
    bill_value = float(input())


def divide_bill():
    global names

    for i in names:
        names[i] = round(bill_value / len(names), 2)


def recalculate_bill():
    global names

    for i in names:
        if i == lucky_person:
            names[i] = 0
            continue
        names[i] = round(bill_value / (len(names) - 1), 2)


def who_is_lucky():
    global lucky_person

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    user = input()
    if user == 'Yes':
        lucky_person = random.choice(list(names.keys()))
        print(f'{lucky_person} is the lucky one!')
        recalculate_bill()
    elif user == 'No':
        print(f'No one is going to be lucky')


def archive_people():
    global names

    print('Enter the name of every friend (including you), each on a new line:')
    for _ in range(n_people):
        user = input()
        names.update({user: 0})


input_number_people()
archive_people()
input_bill_value()
divide_bill()
who_is_lucky()
print(names)
