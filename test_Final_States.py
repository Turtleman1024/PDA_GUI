#	Author: Kenneth Murry
#	CptS 422 
#	Objective: This file stores the Unit tests of the Class Final_States.

import unittest
from Final_States import Final_States
from States import States
from Parse_File import parse_file

class Test_test_Final_States(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_case_number = 1
        cls.file = open('Test_Final_States_Results.txt', 'w')
        cls.file.write('---Test Final States Results---\n')
        cls.file.write('Test Case\tInput\t\t\tExpected Output\t\tResult\n')
        cls.file.write('-----------------------------------------------------------------------\n')
    
    @classmethod
    def tearDownClass(cls):
        cls.file.close()

    #Unit testing the Final States Display method
    def test_Final_States_Display_States(cls):

       final_states = Final_States()
       file_path = 'pda.def'
       # Write the test case number
       cls.file.write(' ' + str(cls.test_case_number) + '\t\t\t')
    
       final_states.load(file_path)
       # Write the Input
       cls.file.write(str(final_states.final_states) + '\t\t\t')

       # Write the Expected Output
       cls.file.write('FINAL_STATES: s2\t')

       display = final_states.view()
       try:
           cls.assertEqual( display, 'FINAL_STATES: s2')
           # Write the results
           cls.file.write('Passed\n')
       except AssertionError:
           #Write the results
           cls.file.write('Failed\n')

    #Unit testing the Final States Load method
    def test_Final_States_Load(cls):
       final_states = Final_States()
       file_path = 'pda.def'

       # Write the test case number
       cls.file.write(' ' + str(cls.test_case_number + 3) + '\t\t\t')
       
       final_states.load(file_path)
       # Write the Input
       cls.file.write(str(final_states.final_states) + '\t\t\t')

       # Write the Expected Output
       cls.file.write(str(final_states.final_states) + '\t\t\t\t')

       try:
           cls.assertEqual(final_states.final_states, ['s2'])
           # Write the results
           cls.file.write('Passed\n')
       except AssertionError:
           #Write the results
           cls.file.write('Failed\n')

    #Unit testing the Final States Is_Element method
    def test_Final_States_Is_Element_Valid(cls):
       final_states = Final_States()
       file_path = 'pda.def'
       # Write the test case number
       cls.file.write(' ' + str(cls.test_case_number + 2) + '\t\t\t')
       
       final_states.load(file_path)
       # Write the Input
       cls.file.write('s2\t\t\t\t')

       # Write the Expected Output
       cls.file.write('True\t\t\t\t')

       try:
           cls.assertTrue(final_states.is_element('s2'))
           # Write the results
           cls.file.write('Passed\n')
       except AssertionError:
           #Write the results
           cls.file.write('Failed\n')

    #Unit testing the Final States Is_Element method
    def test_Final_States_Is_Element_Invalid(cls):
       final_states = Final_States()
       file_path = 'pda.def'
       # Write the test case number
       cls.file.write(' ' + str(cls.test_case_number + 1) + '\t\t\t')
       
       final_states.load(file_path)

       # Write the Input
       cls.file.write('s3\t\t\t\t')

       # Write the Expected Output
       cls.file.write('False\t\t\t\t')

       try:
           cls.assertFalse(final_states.is_element('s3'))
           # Write the results
           cls.file.write('Passed\n')
       except AssertionError:
           #Write the results
           cls.file.write('Failed\n')

    #Unit testing the Final States Validate method
    def test_Validate_Valid(cls):
        final_states = Final_States()
        current_states = States()

        file_path = 'pda.def'

        # Write the test case number
        cls.file.write(' 6\t\t\t')
        
        final_states.load(file_path)
        current_states.load(file_path)

        #Write the Input
        cls.file.write(str(final_states.final_states) + '\t\t\t')

        # Write the Expected Output
        cls.file.write('True\t\t\t\t')

        valid = final_states.validate(current_states.states)
        try:
            cls.assertTrue(final_states.validate(current_states.states))
            # Write the results
            cls.file.write('Passed\n')
        except AssertionError:
            #Write the results
            cls.file.write('Failed\n')

    #Unit testing the Final States Validate method
    def test_Validate_Invalid(cls):
        final_states = Final_States()
        current_states = States()

        final = ['s4']
        file_path = 'pda.def'

        # Write the test case number
        cls.file.write(' 5\t\t\t')

        final_states.final_states = final
        current_states.load(file_path)

        # Write the Input
        cls.file.write(str(final_states.final_states) + '\t\t\t')
        
        # Write the Expected Output
        cls.file.write('False\t\t\t\t')

        try:
            cls.assertFalse(final_states.validate(current_states.states))
            # Write the results
            cls.file.write('Passed\n')
        except AssertionError:
            #Write the results
            cls.file.write('Failed\n')


if __name__ == '__main__':
    try:
        unittest.main()
    except:
        SystemExit(True)

