'''
Created on Aug 4, 2023

@author: Miho
Blood donor center functions
'''

OPTIONS = "Welcome to Blood Donation Center \
Enter c to create a donor list, \
p to existing donor lists, \
s to show a list,\
a to add a donor to a list, \
q to quit. "

NO_DONOR = 'No donors.'

registory = ()

def show_options():
    print_regster_lists()
    selection = input(OPTIONS)
    while selection != 'q':
        if selection == 'c':
            create_donot_register()
        elif selection == 'l':
            print_regster_lists()
        elif selection == 'r':
            show_donor_register()
        elif selection == 'p':
            add_donor()
        selection = input(OPTIONS)
        
        
def create_donot_register():
    pass


def show_donor_register():
    pass


def add_donor():
    registory
    pass


def print_regster_lists():
    ''' If registory is empty, return a generic message'''
    if registory:
        for donor, bloodtype in registory:
            print(f'  {donor}-{bloodtype}')
    else:
        print(NO_DONOR)
    