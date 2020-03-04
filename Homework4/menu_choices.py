    #Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

def get_menu_choice():

    print('Contacts and Their Email Addresses')
    print('1. Look up a contact')
    print('2. Add a new contact')
    print('3. Edit a contact')
    print('4. Delete a contact')
    print('5. Quit\n')

    choice = int(input('Enter your choice: '))
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a vaild choice: '))
    # Return the user's choice
    return choice

def look_up(contacts):
    name = input('Enter a name: ')

    if name in contacts:
        print('Email Address:', contacts[name])
    else:
        print('That name is not found.')

def add(contacts):
    name = input('Enter a name: ')
    email = input('Enter an email address: ')

    if name not in contacts:
        contacts[name] = email
    else:
        print('That entry already exists.')

def change(contacts):
    name = input('Enter a name: ')

    if name in contacts:
        email = input('Enter the new email address: ')

        contacts[name] = email
    else:
        print('That name is not found.')

def delete(contacts):
    name = input('Enter a name: ')

    if name in contacts:
        del contacts[name]
    else:
        print('That name is not found.')
    
