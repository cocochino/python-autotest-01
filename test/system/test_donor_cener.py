'''
Created on Aug 4, 2023

@author: Miho
System test mocking
Mocking saves test execution time too
'''

from unittest import TestCase
from unittest.mock import patch

from donor_list import DonorList
from blood_donor import BloodDonor

import donor_center as dc

class DonorCenterTest(TestCase):
    
    
    #Mock testing   
    def test_1_show_options(self):
        ''' Example 2. Use mocked print to verify class constant text was called '''
        with patch('builtins.print') as mock_print:
            with patch('builtins.input', return_value = 'q') as mock_input:
                dc.show_options()
                mock_print.assert_called_with(dc.NO_DONOR)

                       
    def test_2_print_donor_lists_empty(self):
        ''' Example 1. Use mocked print to verify specific text was called'''
        with patch('builtins.print') as mock_print:
            dc.print_donor_lists()
            mock_print.assert_called_with(dc.NO_DONOR)


    def test_option_create_donor_list(self):
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ('c', 'Boston', 'SV1', 'q')
            dc.show_options()
            self.assertIsNotNone(dc.lists['Boston'])
    
    
    def test_show_options_display_registry(self):
        ''' Example 3-1 Use mocked  to check if custom method was called. NOTE: can't use import as short-hand
            Example 3-2 Mocking user input '''
        with patch('donor_center.print_donor_lists') as mock_print_regster_lists:
            #In below example, test feeds 'x' to any input requests 
            with patch('builtins.input', return_value='q') as mock_input: #This will always return 'q' as input
                dc.print_donor_lists()
                mock_print_regster_lists.assert_called()


    def test_create_donor_list(self):#ask_create_blog
        '''Example 4 -  Handling multiple input by using side_effect'''
        with patch('builtins.input') as mocked_input:
            #mocked_input.side_effect = ('Test', 'Author')
            mocked_input.side_effect = ('Newton', 'Preston S') #Multiple input will be sent to test in this order
            dc.create_donor_list()
            #self.assertIsNotNone(dc.create_donor_list('Newton'))
            self.assertIsNotNone('Newton')
            self.assertIsNotNone('Preston S')
                 
     
    def test_read_donor(self): #ask_read_blog()
        '''Example 5 Handling list'''
        dList = DonorList('Newton', 'Preston S')
        dc.lists = {'Test register':dList} # This test list will be called below
        with patch('builtins.input', return_value='Test register') as mock_input:
            with patch('donor_center.print_donors') as mock_print_donors:
                dc.read_donor()
                mock_print_donors.assesrt_called_with(dList)
                
                
    def test_print_donors(self):
        ''' Example 6 - calling embedded method '''
        dList = DonorList('Newton', 'Preston S')
        dList.create_blood_donor('Donor 1', 'active','B')
        #print("dList 0 is", dList.donors[0])
        with patch('donor_center.print_donor') as mock_print_donor:
            dc.print_donors(dList)
            mock_print_donor.assert_called_with(dList.donors[0])
            
            
    def test_print_donor(self):
        name = 'Donor 1'
        blood_type = 'B'
        donor = BloodDonor(name, 'active', blood_type)
        expected = f"Donor info: {name} {blood_type}"
        with patch('builtins.print') as mocked_print:
            dc.print_donor(donor)
            mocked_print.assert_called_with(expected)
            
            
    def test_add_donor(self):
        dList = DonorList('Newton', 'Preston S')
        dc.lists = {'Test register':dList} # This test list will be called below
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test register', 'Donor 2', 'AB')
            dc.add_donor()
            self.assertEqual(dList.donors[0].name, 'Donor 2')
            self.assertEqual(dList.donors[0].status, 'active')
            self.assertEqual(dList.donors[0].blood_type, 'AB')
            self.assertEqual(list(dc.lists.keys())[0], 'Test register')


