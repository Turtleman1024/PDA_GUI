#	Author: Kenneth Murry
#	CptS 422 
#	Objective: This class holds the characters of the stack alphabet

from Parse_File import parse_file

class Stack_Alphabet:

    def __init__(self):
        self.stack_alphabet = []
    
    # The method load will load the stack alphabet into the attribute stack_alphabet.
    def load(self, file_path):        
        self.stack_alphabet = parse_file(file_path, 'STACK_ALPHABET:', 'TRANSITION_FUNCTION:')

    # The method is_element checks if the passed in value is contained within the attribute stack_alphabet.
    def is_element(self, value):
        return (value in self.stack_alphabet)

    # The method view returns a representation of the attribute stack_alphabet 
    def view(self):
        return 'STACK_ALPHABET: '+ ' '.join(self.stack_alphabet)





