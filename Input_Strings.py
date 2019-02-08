#	Author: Kenneth Murry
#	CptS 422 
#	Objective: This file stores the Class Input_String representing the input strings for the 
#              pushdown automaton.

from Input_Alphabet import Input_Alphabet

class Input_Strings:
    
    def __init__(self):
        self.input_strings = []

    # The method load will load the input string into the attribute input_strings.
    def load(self, file_path):
        # Remove last three characters of the file_path
        path = file_path[:-3]
        # Adding str to end of file path
        path = path + 'str'
        #print(path)
        try:
            with open(path) as f:
                self.input_strings = f.read().splitlines()    
            f.close()
            self.duplicate()
        except IOError:
            self.input_strings = []

    # The method get_input_string will return the string at a given index or 'Error' in not in range
    def get_input_string(self, index):
        length = len(self.input_strings)
        if index > (length - 1) or index < 0:
            return 'Error'
        else:
            return self.input_strings[index]

    # The method add_input_string will add a string to the list of strings
    # and check if the string to add is a duplicate string
    def add_input_string(self, input_alpha, new_string):
        if self.validate(input_alpha, new_string) == True:
           self.input_strings.append(new_string)
           self.duplicate()

    # The method display input string will display the input strings
    # mainly used for debugging
    def view(self):
        return ' '.join(self.input_strings)

    # The method duplicate will check if there are duplicate strings
    # and remove them if duplicate strings exist.
    def duplicate(self):
        seen = set()
        result = []
        for item in self.input_strings:
            if item not in seen:
                seen.add(item)
                result.append(item)
        self.input_strings = result

    # Check if the passed in string is a duplicate string
    def is_duplicate(self, string):
        if string in self.input_strings:
            return True
        else:
            return False
    
    # The method remove string will remove the passed in string
    def remove_string(self, del_string):
        try:
           self.input_strings.remove(del_string)
        except ValueError:
            pass

    # The method validate validates the passed in string based on the passed
    # in input alphabet.
    def validate(self, input_alpha, input_string):
        valid = True
        for input in set(input_string):
            if input is '\\' and len(input_string) <= 1:
                continue
            elif input == '[' or input == ']':
                valid = False
            else:
                for letter in input:
                    if letter not in input_alpha:
                        valid = False
        if valid == False:
            self.remove_string(input_string)
            return valid
        else:
            return valid

# White box unit testing 
# Uncomment code below to run the unit tests
#
#Strings = Input_Strings()
#Input_alpha = Input_Alphabet()
#file_path = 'invalid_pda.str'
#file_def_path = 'pda.def'
#invalid_string = 'abc'
#invalid_string2 = 'ab\\'
#invalid_string3 = 'ab['
#invalid_string4 = 'ab]'
#
#Strings.load('pda.de')
#print('String Should be empty: ' + Strings.view())
#
#Strings.load(file_path)
#Input_alpha.load(file_def_path)
#
#print('Loading valid strings')
#print(Strings.view())
#
#print('Size of input strings: {}'.format(len(Strings.input_strings)-1) )
#print('Out of bounds index -1: ' + Strings.get_input_string(-1))
#print('String a index 0: ' + Strings.get_input_string(0))
#print('String a index 1: ' + Strings.get_input_string(1))
#print('String a index 4: ' + Strings.get_input_string(4))
#print('String a index 8: ' + Strings.get_input_string(8))
#print('String a index 9: ' + Strings.get_input_string(9))
#print('Out of bounds index 10: ' + Strings.get_input_string(10))
#
#print('\nAdding Invalid String: ' + invalid_string)
#Strings.add_input_string(Input_alpha.alphabet, invalid_string)
#print(Strings.view())
#print('Adding Invalid String: ' + invalid_string2)
#Strings.add_input_string(Input_alpha.alphabet, invalid_string2)
#print(Strings.view())
#print('Adding Invalid String: ' + invalid_string3)
#Strings.add_input_string(Input_alpha.alphabet, invalid_string3)
#print(Strings.view())
#print('Adding Invalid String: ' + invalid_string4)
#Strings.add_input_string(Input_alpha.alphabet, invalid_string4)
#print(Strings.view())
#
#print('\n')
#print(Strings.view())
# # Test Suite
#for string in Strings.input_strings:
#    if Strings.validate(Input_alpha.alphabet, string) == True:
#        print('String {} is valid'.format(string))
#    else:
#        print('String {} is invalid'.format(string))
#
#print(Strings.view())
#
#print('\nAdding String aba again')
#Strings.add_input_string(Input_alpha.alphabet, 'aba')
#print(Strings.view())






