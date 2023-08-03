'''
Created on Aug 1, 2023

@author: Miho

Integration test for donor_list.py
This is integration since donor creation causes import of blood_donor.py 
'''
from unittest import TestCase
from src.donor_list import DonorList


location1 = 'Boston'        
sv1 = 'Phrito S'
d1 = "Loren"
s1 = "Plasma 1"
sts1 = "active"
msg = "Test failed."
type1 = 'A'

class DonorListIntegrationTest(TestCase):
         
    def test_create_donor(self):
        '''Test blood donor creation'''
        dl = DonorList(location1, sv1)
        dl.create_blood_donor(d1, sts1, type1)
        self.assertEqual(dl.donors[0].name, d1, msg)
        self.assertEqual(dl.donors[0].status, sts1, msg)      
        
    
    def test_no_donor(self):
        '''Test JSON output when there is no donor created'''
        dl = DonorList(location1, sv1)
        expected = {'Location': location1, 
                    'supervisor': sv1, 
                    'donors': []
                    }
        
        self.assertDictEqual(dl.json(), expected, msg)        
        
    
    def test_json(self):
        '''JSON output test'''
        dl = DonorList(location1, sv1)
        dl.create_blood_donor(d1, sts1, type1)
        
        expected = {'Location': location1, 
                    'supervisor': sv1, 
                    'donors': [{'name': d1, 'status': sts1, 'blood type': type1}]
                    }
        
        self.assertDictEqual(dl.json(), expected, msg)