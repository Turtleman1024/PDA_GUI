#	Author: Kenneth Murry
#	CptS 422 
#	Objective: This file stores the Unit tests of the Class Input_Alphabet.

import unittest
from Input_Alphabet import Input_Alphabet
from Parse_File import parse_file

class Test_test_Input_Alphabet(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_case_number = 1
        cls.file = open('Test_Input_Alphabet_Results.txt', 'w')
        cls.file.write('---Test Input Alphabet Results---\n')
        cls.file.write('Test Case\tInput\t\t\tExpected Output\t\t\tResult\n')
        cls.file.write('-----------------------------------------------------------\n')
    
    @classmethod
    def tearDownClass(cls):
        cls.file.close()
    
    #Unit testing the Input Alphabet Display method
    def test_Input_Alphabet_Display(cls):
        alphabet = Input_Alphabet()
        file_path = 'pda.def'

        # Write the test case number
        cls.file.write(' ' + str(cls.test_case_number) + '\t\t\t')

        alphabet.load(file_path)

        # Write the Input
        cls.file.write(str(alphabet.alphabet) + '\t\t')

        # Write the Expected Output
        cls.file.write('INPUT_ALPHABET: a b\t\t')

        display = alphabet.view()

        try:
            cls.assertEqual(display, 'INPUT_ALPHABET: a b')
            # Write the results
            cls.file.write('Passed\n')
        except AssertionError:
            #Write the results
            cls.file.write('Failed\n')

    #Unit testing the Input Alphabet Load method
    def test_Input_Alphabet_Load(cls):
        alphabet = Input_Alphabet()
        file_path = 'pda.def'

        # Write the test case number
        cls.file.write(' ' + str(cls.test_case_number + 3) + '\t\t\t')

        alphabet.load(file_path)

        # Write the Input
        cls.file.write(str(alphabet.alphabet) + '\t\t')

        # Write the Expected Input
        cls.file.write(str(alphabet.alphabet) + '\t\t\t\t')

        try:
            cls.assertEqual(alphabet.alphabet, ['a', 'b'])
            # Write the results
            cls.file.write('Passed\n')
        except AsertionError:
            #Write the results
            cls.file.write('Failed\n')

    #Unit testing the Input Alphabet Is_Element method
    def test_Input_Alphabet_Is_Element_Valid(cls):
        alphabet = Input_Alphabet()
        file_path = 'pda.def'
        # Write the test case number
        cls.file.write(' ' + str(cls.test_case_number + 2) + '\t\t\t')

        alphabet.load(file_path)
        # Write the Input
        cls.file.write('a\t\t\t\t')

        # Write the Expected Output
        cls.file.write('True\t\t\t\t\t')

        try:
            cls.assertTrue(alphabet.is_element('a'))
            # Write the results
            cls.file.write('Passed\n')
        except AssertionError:
            #Write the results
            cls.file.write('Failed\n')

    #Unit testing the Input Alphabet Is_Element method
    def test_Input_Alphabet_Is_Element_Invalid(cls):
        alphabet = Input_Alphabet()
        file_path = 'pda.def'
        # Write the test case number
        cls.file.write(' ' + str(cls.test_case_number + 1) + '\t\t\t')

        alphabet.load(file_path)

        # Write the Input
        cls.file.write('c\t\t\t\t')

        # Write the Expected Output
        cls.file.write('False\t\t\t\t\t')

        try:
            cls.assertFalse(alphabet.is_element('c'))
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
