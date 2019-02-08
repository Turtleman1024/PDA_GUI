#	Author: Kenneth Murry
#	CptS 422 
#	Objective: This file stores the Class Configuration_Settings representing the configuration settings
#	           for the pushdown automaton.

from Parse_File import parse_file

class Configuration_Settings:
    
    def __init__(self):
        self.max_trans = []
        self.max_char = []

    # The method load will load the configuration setting into the class attributes
    def load(self, file_path):
        # Remove last three characters of the file_path
        path = file_path[:-3]
        # Adding cfg to end of file path
        path = path + 'cfg'

        self.max_trans = parse_file(path, 'MAXIMUM_TRANSITIONS=', 'MAXIMUM_CHARACTERS=')
        self.max_char = parse_file(path, 'MAXIMUM_CHARACTERS=', '')

        # If the max transition could not be found set to default
        if self.max_trans == 'Error' or self.max_trans == []:
           self.max_trans = [1]
        
        # If the max characters could not be found set to default
        if self.max_char == 'Error' or self.max_char == []:
           self.max_char = [32]

        # If the max transition is not a digit set to default
        if self.max_trans[0].isdigit() == False:
           self.max_trans = [1]

        # If the max character is not a digit set to default
        if self.max_char[0].isdigit() == False:
           self.max_char = [32]
        






#config = Configuration_Settings()
#path = 'invalid_pda.def'
#path = 'pda.def'
#
#config.load(path)
#
#print(config.max_trans)
#print(config.max_char)

        


