#	Author: Kenneth Murry
#	CptS 422 
#	Objective: This file stores the Unit tests of the Class Stack_Alphabet.

import unittest
from Stack_Alphabet import Stack_Alphabet
from Parse_File import parse_file

class Test_test_Stack_Alphabet(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_case_number = 1
        cls.file = open('Test_Stack_Alphabet_Results.txt', 'w')
        cls.file.write('---Test Stack Alphabet Results---\n')
        cls.file.write('Test Case\tInput\t\t\t\tExpected Output\t\t\tResult\n')
        cls.file.write('---------------------------------------------------------------\n')
    
    @classmethod
    def tearDownClass(cls):
        cls.file.close()
        
    #Unit testing the Stack Alphabet Display method
    def test_Dispaly_Stack_Alphabet(cls):
        stack_alphabet = Stack_Alphabet()
        file_path = 'pda.def'

        # Write the test case number
        cls.file.write(' ' + str(cls.test_case_number) + '\t\t\t')

        stack_alphabet.load(file_path)

        # Write the Input
        cls.file.write(str(stack_alphabet.stack_alphabet) + '\t\t')

        # Write the Expected Output
        cls.file.write('STACK_ALPHABET: X Y Z\t')

        display = stack_alphabet.view()
        try:
            cls.assertEqual(display, 'STACK_ALPHABET: X Y Z')
            # Write the results
            cls.file.write('Passed\n')
        except AssertionError:
            #Write the results
            cls.file.write('Failed\n')

    #Unit testing the Stack Alphabet Load method
    def test_Stack_Alphabet_Load(cls):
        stack_alphabet = Stack_Alphabet()
        file_path = 'pda.def'

        # Write the test case number
        cls.file.write(' ' + str(cls.test_case_number + 3) + '\t\t\t')

        stack_alphabet.load(file_path)

        # Write the Input
        cls.file.write(str(stack_alphabet.stack_alphabet) + '\t\t')

        # Write the Expected Input
        cls.file.write(str(stack_alphabet.stack_alphabet) + '\t\t\t')
        try:
            cls.assertEqual(stack_alphabet.stack_alphabet, ['X', 'Y', 'Z'])
            # Write the results
            cls.file.write('Passed\n')
        except AsertionError:
            #Write the results
            cls.file.write('Failed\n')

    #Unit testing the Stack Alphabet Is_Element method
    def test_Stack_Alphabet_Is_Element_Valid(cls):
        stack_alphabet = Stack_Alphabet()
        file_path = 'pda.def'
        # Write the test case number
        cls.file.write(' ' + str(cls.test_case_number + 2) + '\t\t\t')

        stack_alphabet.load(file_path)
        # Write the Input
        cls.file.write('X\t\t\t\t\t')

        # Write the Expected Output
        cls.file.write('True\t\t\t\t\t')
        try:
            cls.assertTrue(stack_alphabet.is_element('X'))
            # Write the results
            cls.file.write('Passed\n')
        except AssertionError:
            #Write the results
            cls.file.write('Failed\n')

    #Unit testing the Stack Alphabet Is_Element method
    def test_Stack_Alphabet_Is_Element_Invalid(cls):
        stack_alphabet = Stack_Alphabet()
        file_path = 'pda.def'
        # Write the test case number
        cls.file.write(' ' + str(cls.test_case_number + 1) + '\t\t\t')

        stack_alphabet.load(file_path)

        # Write the Input
        cls.file.write('M\t\t\t\t\t')

        # Write the Expected Output
        cls.file.write('False\t\t\t\t\t')
        try:
            cls.assertFalse(stack_alphabet.is_element('M'))
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

