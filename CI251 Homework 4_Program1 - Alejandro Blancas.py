# Alejandro Blancas
# CI251
# Homework 4 - Using Dictonaries
# There are two files that needed for this program to work:
# menu_choices.py & save_load_dict.py
import menu_choices
import save_load_dict
    #Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
    
def main():
    #Load the contacts dictionary
    contacts = save_load_dict.unpickle_it()
    choice = 0

    while choice != QUIT:
        choice = menu_choices.get_menu_choice()

        if choice == LOOK_UP:
            menu_choices.look_up(contacts)
        elif choice == ADD:
            menu_choices.add(contacts)
        elif choice == CHANGE:
            menu.choices.change(contacts)
        elif choice == DELETE:
            menu_choices.delete(contacts)

        # Save the contacts dictionary
        save_load_dict.pickle_it(contacts)
main()
