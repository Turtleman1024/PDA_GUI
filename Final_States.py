#	Author: Kenneth Murry
#	CptS 422 
#	Objective: This file stores the Class Final_States representing the final states the 
#	           pushdown automaton can be in at any given time.

from Parse_File import parse_file

class Final_States:
    
    def __init__(self):
        self.final_states = []

    # The method load will load the final states into the attribute final_states.
    def load(self, file_path):
        self.final_states = parse_file(file_path, 'FINAL_STATES:', '')

    # The method is_element checks if the passed in value is contained within the attribute final_states.
    def is_element(self, value):
        return (value in self.final_states)

    # The method view returns a representation of the attribute final_states. 
    def view(self):
        return 'FINAL_STATES: ' + ''.join(self.final_states)

    # The method validate checks if the final state is a subset of the States class
    def validate(self, states):
        return set(self.final_states).issubset(states)



