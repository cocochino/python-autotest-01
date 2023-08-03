'''
Created on Aug 1, 2023

@author: Miho
'''

class Donor:
    '''
    Generic donor class
    '''

    def __init__(self, d_name, d_status):
        '''
        Creates a basic donor
        '''
        self.name = d_name
        self.status = d_status
        
    def __str__(self) -> str:
        '''
        String representation.
        '''
        return f"Donor name {self.name!r}, status {self.status!r}"
        
    def disqualify(self):
        '''
        Change donor status to disqualified.
        '''
        self.status = "disqualified"
        print("Donor status has been changed to disqualified.")
        