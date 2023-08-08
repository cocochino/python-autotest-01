'''
Created on Aug 1, 2023

@author: Miho

Demo of simple comparison of strings and JSON outputs
'''

from unittest import TestCase
from blood_donor import BloodDonor

d1Name = 'Boston'        
d1Status = 'active'
d1BloodTpe = 'A'   
negativeName = 'Bad Name'        
negativeStatus = 'N/A'
negativeBloodTpe = 'No Type'   
msg = "Test failed."

class BloodDonorTest(TestCase):
    '''
    Blood Donor attribute test
    '''

    def test_create_donor(self):
        #AssertEqual
        d1 = BloodDonor(d1Name, d1Status, d1BloodTpe)
        self.assertEqual(d1.name, d1Name, msg)
        self.assertEqual(d1.status, d1Status, msg)
        self.assertEqual(d1.blood_type, d1BloodTpe, msg)

    
    def test_negative_create_donor(self):
        #AssertNotEqual
        d1 = BloodDonor(d1Name, d1Status, d1BloodTpe)
        self.assertNotEqual(d1.name, negativeName, msg)
        self.assertNotEqual(d1.status, negativeStatus, msg)
        self.assertNotEqual(d1.blood_type, negativeBloodTpe, msg)

        
    def test_json(self):
        #Dictionary comparison
        expected = {
            'name': d1Name,
            'status': d1Status,
            'blood type': d1BloodTpe
            }
        d1 = BloodDonor(d1Name, d1Status, d1BloodTpe)
        self.assertDictEqual(d1.json(), expected, msg)

 
    def test_json_elements(self):
        #Dictionary element comparison
        d1 = BloodDonor(d1Name, d1Status, d1BloodTpe)
        self.assertEqual(d1.json().get('name'), d1Name, msg) #Accessing single element in JSON output

       
    def test_negative_json_elements(self):
        #Dictionary element comparison
        d1 = BloodDonor(d1Name, d1Status, d1BloodTpe)
        self.assertNotEqual(d1.json().get('name'), negativeName, msg) #Accessing single element in JSON output
