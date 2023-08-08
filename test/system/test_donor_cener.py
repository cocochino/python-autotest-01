'''
Created on Aug 4, 2023

@author: Miho
System test mocking
Mocking saves test execution time too
'''

from unittest import TestCase
from unittest.mock import patch

import donor_center as dc
class DonorCenterTest(TestCase):
    
    #Mock testing
    def test_print_regster_lists_empty(self):
        ''' Example 1. Use mocked print to verify specific text was called'''
        with patch('builtins.print') as mock_print:
            dc.print_regster_lists()
            mock_print.assert_called_with(dc.NO_DONOR)

    ''' Example 2. Use mocked print to verify class constant text was called '''
    '''  
    def test_show_options(self):
        with patch('builtins.print') as mock_print:
            with patch('builtins.input', return_value = 'q') as mock_input:
                dc.show_options()
                mock_print.assert_called_with(dc.NO_DONOR)
    '''
                   
    def test_show_options_display_registry(self):
        ''' Example 3-1 Use mocked  to check if custom method was called. NOTE: can't use import as short-hand
            Example 3-2 Mocking user input '''
        with patch('donor_center.print_regster_lists') as mock_print_regster_lists:
            #In below example, test feeds 'x' to any input requests 
            with patch('builtins.input', return_value = 'q') as mock_input:
                dc.print_regster_lists()
                mock_print_regster_lists.assert_called()

