'''
Created on Aug 4, 2023

@author: Miho
Blood donor center functions
'''

from donor_list import DonorList
import donor

OPTIONS = "Welcome to Blood Donation Center \
Enter c to create a donor list, \
p to existing donor lists, \
s to show a list,\
a to add a donor to a list, \
q to quit. "

NO_DONOR = 'No donors.'
lists = dict() #blogs

def show_options():
    print_donor_lists()
    selection = input(OPTIONS)
    while selection != 'q':
        if selection == 'c': #ask_create_blog()
            create_donor_list()
        elif selection == 'l': #print_blogs()
            print_donor_lists()
        elif selection == 'r': #ask_read_blog()
            read_donor()
        elif selection == 'p':#ask_create_post()
            add_donor()
        selection = input(OPTIONS)

        
def print_donor_lists(): #print_blogs()
    ''' If registory is empty, return a generic message'''
    if lists:
        for k, l in lists.items():
            print(f'{k} - {l}')
    else:
        print(NO_DONOR)

            
def create_donor_list():  #ask_create_blog()
    loc = input('Enter donor center location: ')
    sv = input('Enter supervisor name: ')
    lists[loc] = DonorList(loc, sv)
    #print(lists[loc])
    

def read_donor(): #ask_read_blog()
    title = input('Enter the donor list to be displayed: ')
    print_donors(lists[title])


def print_donors(dLlist): #print_posts
    for l in dLlist.donors:
        #print_donor("inside1", list)
        #print("list contest is: ", lists[list])
        print_donor(l)


def print_donor(donor): #print_post
    print(f"Donor info: {donor.name} {donor.blood_type}")


def add_donor():#ask_create_post()
    theList = input('Enter donor list name: ')
    donor_name = input('Enter donor name: ')
    blood_type = input('Enter donor blood type: ')
    lists[theList].create_blood_donor(donor_name, 'active', blood_type )
    #pass


