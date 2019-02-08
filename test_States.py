#	Author: Kenneth Murry
#	CptS 422 
#	Objective: This file stores the Unit tests of the Class States.

import unittest
from States import States

class Test_test_States(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_case_number = 1
        cls.file = open('Test_States_Results.txt', 'w')
        cls.file.write('---Test States Results---\n')
        cls.file.write('Test Case\tInput\t\t\t\tExpected Output\t\tResult\n')
        cls.file.write('-----------------------------------------------------------\n')
    
    @classmethod
    def tearDownClass(cls):
        cls.file.close()

    #Unit testing the States Display method
    def test_States_Display_States(cls):
        current_states = States()
        file_path = 'pda.def'
        # Write the test case number
        cls.file.write(' ' + str(cls.test_case_number) + '\t\t\t')
        
        current_states.load(file_path)

        # Write the Input
        cls.file.write(str(current_states.states) + '\t')

        # Write the Expected Output
        cls.file.write('STATES: s0 s1 s2\t')

        display = current_states.view()
        try:
            cls.assertEqual(display, 'STATES: s0 s1 s2')
            # Write the results
            cls.file.write('Passed\n')
        except AssertionError:
            #Write the results
            cls.file.write('Failed\n')

        # Increment test case number
        cls.test_case_number += 1

    #Unit testing the States Load method
    def test_States_Load(cls):
        current_states = States()
        file_path = 'pda.def'

        # Write the test case number
        cls.file.write(' ' + str(cls.test_case_number + 3) + '\t\t\t')

        current_states.load(file_path)

        # Write the Input
        cls.file.write(str(current_states.states) + '\t')

        # Write the Expected Output
        cls.file.write(str(current_states.states) + '\t')

        try:
            assert current_states.states == ['s0', 's1', 's2']
            # Write the results
            cls.file.write('Passed\n')
        except AssertionError:
            #Write the results
            cls.file.write('Failed\n')

        # Increment test case number
        cls.test_case_number += 1

    #Unit testing the State Is_Element method
    def test_States_Is_Element_Valid(cls):
       current_states = States()
       file_path = 'pda.def'

       # Write the test case number
       cls.file.write(' ' + str(cls.test_case_number + 2) + '\t\t\t')

       current_states.load(file_path)

       # Write the Input
       cls.file.write('s1\t\t\t\t\t')

       # Write the Expected Output
       cls.file.write('True\t\t\t\t')

       try:
           cls.assertTrue(current_states.is_element('s1'))
           # Write the results
           cls.file.write('Passed\n')
       except AssertionError:
           #Write the results
           cls.file.write('Failed\n')

       # Increment test case number
       cls.test_case_number += 1

    #Unit testing the State Is_Element method
    def test_States_Is_Element_Invalid(cls):
        current_states = States()
        file_path = 'pda.def'

        # Write the test case number
        cls.file.write(' ' + str(cls.test_case_number + 1) + '\t\t\t')

        current_states.load(file_path)

        # Write the Input
        cls.file.write('s3\t\t\t\t\t')

        # Write the Expected Output
        cls.file.write('False\t\t\t\t')

        try:
            cls.assertFalse(current_states.is_element('s3'))
            # Write the results
            cls.file.write('Passed\n')
        except AssertionError:
            #Write the results
            cls.file.write('Failed\n')

        # Increment test case number
        cls.test_case_number += 1

if __name__ == '__main__':
    try:
        unittest.main()
    except:
        SystemExit(True)
