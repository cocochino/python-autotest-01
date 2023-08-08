'''
Created on Aug 1, 2023

@author: Miho
'''

from donor import Donor 

class BloodDonor(Donor):
    '''
    Inherit generic donor class
    '''
    max_volume = 600
    remaining_volume = max_volume 
    #Below will extend the parent init methods (which is super).
    #Make sure to pass all required arguments the super 
    def __init__(self, d_name: str, d_status: str, blood_type: str):
        super().__init__(d_name, d_status)
        self.blood_type = blood_type
    
        
    def __str__(self) -> str:
        return f"{super().__str__()}. Blood type is {self.blood_type!r}. "

    
    def json(self):
        return{
            'name': self.name,
            'status': self.status,
            'blood type': self.blood_type
            }

    
    def donate_blood(self, volume: int):
        if self.status == 'disqualified':
            print(f"{self.name} is not qualified to donate.")
            return 
        self.remaining_volume -= volume 
        print(f"{self.name} donated {volume}ml. {self.remaining_volume}ml remaining.")