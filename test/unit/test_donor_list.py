'''
Created on Aug 1, 2023

@author: Miho

Unit test for donor_list.py file
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

class DonorListTest(TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_donor_list(self):
        dl = DonorList(location1, sv1)
        ''' Check the location and the site supervisor '''
        self.assertEquals(dl.location, location1 , msg)
        self.assertEquals(dl.supervisor, sv1 , msg)
        


    def test_initian_assign_station(self):
        '''Test initial station status'''
        empty_list = []

        dl = DonorList(location1, sv1)      
        '''Comparing the list itself'''
        self.assertListEqual(dl.donors, empty_list, msg)
        
        '''Test initial donor list'''
        self.assertEqual(len(dl.donors), len(empty_list), msg)


    def test_assign_station(self):
        '''Test donation station assignment'''
        dl = DonorList(location1, sv1)      
        dl.assign_station(d1, s1)
        self.assertEqual(len(dl.donors), 1, msg)

        
    def test_repr(self):
        '''Test 0 list'''
        dl = DonorList(location1, sv1)
        expected = f"Location = {location1!r}, supervisor = {sv1!r}, 0 donor."
        self.assertEqual(dl.__repr__(), expected, msg) #WARNING! comparing with dl will cause failure
        

    def test_repr_multiple_donors(self):
        '''Test non-0 list'''
        dl = DonorList(location1, sv1)
        dl.assign_station(d1, s1)
        dl.assign_station('donor 2', 'station 2')
        expected = f"Location = {location1!r}, supervisor = {sv1!r}, 2 donors."
        self.assertEqual(dl.__repr__(), expected, msg) #WARNING! comparing with dl will cause failure




