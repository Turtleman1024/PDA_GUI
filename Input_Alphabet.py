#	Author: Kenneth Murry
#	CptS 422 
#	Objective: This class holds the characters of the input string alphabet

from Parse_File import parse_file

class Input_Alphabet:

    def __init__(self):
        self.alphabet = []

    # The method load will load the input alphabet into the attribute alphabet.
    def load(self, file_path):
        self.alphabet = parse_file(file_path, 'INPUT_ALPHABET:', 'STACK_ALPHABET:')

    # The method is_element checks if the passed in value is contained within the attribute alphabet.
    def is_element(self, value):
        return (value in self.alphabet)

    # The method view returns a representation of the attribute alphabet. 
    def view(self):
        return 'INPUT_ALPHABET: '  + ' '.join(self.alphabet)




