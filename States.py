#	Author: Kenneth Murry
#	CptS 422 
#	Objective: This file stores the Class States representing the states the 
#	           pushdown automaton can be in at any given time.

from Parse_File import parse_file

class States:

    def __init__(self):
        self.states = []
    
    # The method load will load the states into the attribute states.
    def load(self, file_path):
        self.states = parse_file(file_path, 'STATES:', 'INPUT_ALPHABET:')

    # The method is_element checks if the passed in value is contained within the attribute states.
    def is_element(self, value):
        return (value in self.states)

    # The method view returns a representation of the attribute states. 
    def view(self):
        return 'STATES: ' + ' '.join(self.states)

