'''
Created on Aug 1, 2023

@author: Miho
'''
from src.blood_donor import BloodDonor

class DonorList(object):
    '''
    List of a blood donation center's blood donors
    '''

    def __init__(self, location: str, supervisor: str ):
        '''
        Constructor
        '''
        self.location = location
        self.supervisor = supervisor
        self.donors = []
        self.donors_str = ''
    
        
    def __repr__(self) -> str:
        '''
        String representation
        '''
        return f"Location = {self.location!r}, supervisor = {self.supervisor!r}, {len(self.donors)} donor{'s' if len(self.donors) > 1 else ''}."
    
    
    def create_blood_donor(self, d_name, d_status, blood_type):
        '''
        Create blood donors
        '''
        self.donors.append(BloodDonor(d_name, d_status, blood_type))

    
    def assign_station(self, donor:str, station:str):
        '''
        Assign donation station
        '''
        self.donors.append([donor, station])
    
    
    def json(self):
        #self.donors_str = ''             
        return {
            'Location': self.location,
            'supervisor': self.supervisor,
            'donors': [donor.json() for donor in self.donors],
        }
            
        