#	Author: Kenneth Murry
#	CptS 422 
#	Objective: This file stores the Class Validate Def File it will validate 
#              if the keywords are correct in the defintion file.
#              It will also validate the content of each keyword.

from Parse_File import parse_file
from Final_States import Final_States
from States import States
from Stack_Alphabet import Stack_Alphabet
from Input_Alphabet import Input_Alphabet
class Validate_Def_File:

    def __init__(self, file_path):        
        self.states_valid = False
        self.input_alph_valid = False
        self.stack_alpha_valid = False
        self.trans_func_valid = False
        self.init_state_valid = False
        self.start_char_valid = False
        self.final_states_valid = False
        self.def_valid = False
        self.invalid_keyword = False
        self.error_list = []
        self.validate(file_path)

    # A method that will validate the definition file keyword are present.
    def validate(self, file_path):
        with open(file_path, 'r') as f:
            for line in f:
                for word in line.split():
                    if (word.upper() or word.lower()) == 'STATES:':
                       self.states_valid = True
                    if (word.upper() or word.lower()) == 'INPUT_ALPHABET:':
                        self.input_alph_valid = True
                    if (word.upper() or word.lower()) == 'STACK_ALPHABET:':
                        self.stack_alpha_valid = True
                    if (word.upper() or word.lower()) == 'TRANSITION_FUNCTION:':
                        self.trans_func_valid = True
                    if (word.upper() or word.lower()) == 'INITIAL_STATE:':
                        self.init_state_valid = True
                    if (word.upper() or word.lower()) == 'START_CHARACTER:':
                        self.start_char_valid = True
                    if (word.upper() or word.lower()) == 'FINAL_STATES:':
                        self.final_states_valid = True
        f.close()
        self.is_valid_def()
        if(self.invalid_keyword == False):
            self.file_is_valid(file_path)
    
    # A method that will set the def_valid attribute.
    def is_valid_def(self):
        if (self.states_valid == True and
            self.input_alph_valid == True and
            self.stack_alpha_valid == True and
            self.trans_func_valid == True and
            self.init_state_valid == True and
            self.start_char_valid == True and
            self.final_states_valid == True):
            self.def_valid = True
            self.invalid_keyword = False
        else:
            self.invalid_keyword = True
            self.def_valid = False

    # A method used to validate the content of each component of the 
    # definition file.
    def file_is_valid(self, file_path):
        self.Input_Alpha = Input_Alphabet()
        self.Input_Alpha.load(file_path)

        self.Stack_Alpha = Stack_Alphabet()
        self.Stack_Alpha.load(file_path)

        self.States = States()
        self.States.load(file_path)

        self.Final_States = Final_States()
        self.Final_States.load(file_path)

        self.transitions = parse_file(file_path, 'TRANSITION_FUNCTION:', 'INITIAL_STATE:')
        self.initial_state = parse_file(file_path, 'INITIAL_STATE:', 'START_CHARACTER:')
        self.start_character = parse_file(file_path, 'START_CHARACTER:', 'FINAL_STATES:')

        ### CHECK STATES KEYWORD CONTENT ###
        # Check if each element of STATES is not in INPUT ALPHABET, STACK ALPHABET,
        # or is the reserved character \
        if not self.States.states:
            self.def_valid = False
            self.error_list.append('NO STATES FOUND!\n')
        for state in self.States.states:
            for letter in state:
                if (letter == '\\' or letter == '[' or letter == ']'):
                    self.def_valid = False
                    self.error_list.append('In STATES: ' + state + ' contains reserved character\n')
                elif (self.Input_Alpha.is_element(letter) == True):
                    self.def_valid = False
                    self.error_list.append('In STATES: ' + state + ' cannot contain INPUT_ALPHABET characters\n')
                elif (self.Stack_Alpha.is_element(letter) == True):
                    self.def_valid = False
                    self.error_list.append('In STATES: ' + state + ' cannot contain STACK_ALPHABET characters\n')
        
        ### CHECK INPUT ALPHABET KEYWORD CONTENT ###
        # Check if each element of INPUT_ALPHABET is not the reserved character \, [ or ]
        self.seen = []
        if not self.Input_Alpha.alphabet:
            self.def_valid = False
            self.error_list.append('NO INPUT ALPHABET CHARACTERS FOUND!\n')
        for alphabet in self.Input_Alpha.alphabet:
            for letter in alphabet:
                if (letter not in self.seen):
                    self.seen.append(letter)
                else:
                    self.def_valid = False
                    self.error_list.append('In INPUT_ALPHABET: ' + letter + ' is specified twice\n')
                if (letter == '\\' or letter == '[' or letter == ']'):
                    self.def_valid = False
                    self.error_list.append('In INPUT_ALPHABET: ' + letter + ' contains reserved character\n')
                #elif (self.Stack_Alpha.is_element(letter) == True):
                #   self.def_valid = False
                #   self.error_list.append('In INPUT_ALPHABET: ' + letter + ' cannot be in both STACK_ALPHABET and INPUT_ALPHABET\n')
        
        ### CHECK STACK ALPHABET KEYWORD CONTENT ###
        # Check if each element of STACK_ALPHABET is not the reserved character \, [ or ]
        self.seen = []
        if not self.Stack_Alpha.stack_alphabet:
            self.def_valid = False
            self.error_list.append('NO STACK ALPHABET CHARACTERS FOUND!\n')
        for alphabet in self.Stack_Alpha.stack_alphabet:
            for letter in alphabet:
                if (letter not in self.seen):
                    self.seen.append(letter)
                else:
                    self.def_valid = False
                    self.error_list.append('In STACK_ALPHABET: ' + letter + ' is specified twice\n')
                if (letter == '\\' or letter == '[' or letter == ']'):
                    self.def_valid = False
                    self.error_list.append('In STACK_ALPHABET: ' + letter + ' contains reserved character\n')
                #elif (self.Input_Alpha.is_element(letter) == True):
                #   self.def_valid = False
                #   self.error_list.append('In STACK_ALPHABET: ' + letter + ' cannot be in both INPUT_ALPHABET and STACK_ALPHABET\n')
        
        ### CHECK TRANSITION FUNCTION KEYWORD CONTENT ###
        # Check if the transitions is not empty
        if not self.transitions:
            self.def_valid = False
            self.error_list.append('NO TRANSITIONS FOUND!\n')
        # While the transition list is not empty
        while(len(self.transitions) > 0):
            # Get a transition
            transition = self.transitions[0:5]
            # Delete the transition extracted from the transitions list
            del self.transitions[0:5]

            ### CHECK SOURCE STATE ###
            # Check if the source state is a valid state
            if(self.States.is_element(transition[0]) == False):
               self.def_valid = False
               self.error_list.append('In Transition: \n' + ' '.join(transition) + ' \n' + transition[0] + ' is not a valid source state\n')
            # Check if each element of source state is not in INPUT ALPHABET, STACK ALPHABET,
            # or is the reserved characters
            else:
               for letter in transition[0]:
                   if (letter == '\\' or letter == '[' or letter == ']'):
                       self.def_valid = False
                       self.error_list.append('In Transition: \n' + ' '.join(transition) + ' \n' + transition[0] + ' cannot contain reserved character\n')
                   elif (self.Input_Alpha.is_element(letter) == True):
                         self.def_valid = False
                         self.error_list.append('In Transition: \n' + ' '.join(transition) + ' \n' + transition[0] + ' cannot contain INPUT_ALPHABET characters\n')
                   elif (self.Stack_Alpha.is_element(letter) == True):
                         self.def_valid = False
                         self.error_list.append('In Transition: \n' + ' '.join(transition) + ' \n' + transition[0] + ' cannot contain STACK_ALPHABET characters\n')

            ### CHECK READ CHARACTER ###
            # Check if the read character is a valid input alphabet
            if(len(transition[1]) != 1):
                self.def_valid = False
                self.error_list.append('In Transition: \n' + ' '.join(transition) + ' \n' + transition[1] + ' is not a valid read character\n')
            elif(self.Input_Alpha.is_element(transition[1]) == False):
                 if(transition[1] == '\\'):
                    # Reserved character \ is allowed in a transition
                    # The pass needs to stay DO NOT DELETE IT
                    pass
                 elif(transition[1] == '[' or transition[1] == ']'):
                    self.def_valid = False
                    self.error_list.append('In Transition: \n' + ' '.join(transition) + ' \n' + transition[1] + ' cannot contain reserved character\n')
                 else:
                    self.def_valid = False
                    self.error_list.append('In Transition: \n' + ' '.join(transition) + ' \n' + transition[1] + ' is not a valid read character\n')
            
            ### CHECK TOP OF STACK CHARACTER ###
            # Check if the top of stack character is a valid stack character
            if(len(transition[2]) != 1):
               self.def_valid = False
               self.error_list.append('In Transition: \n' + ' '.join(transition) + ' \n' + transition[2] + ' is not a valid top of stack character\n')
            elif(transition[2] == '\\' or letter == '[' or letter == ']'):
                 self.def_valid = False
                 self.error_list.append('In Transition: \n' + ' '.join(transition) + ' \n' + transition[2] + ' cannot contain reserved character\n')
            elif(self.Stack_Alpha.is_element(transition[2]) == False):
                 self.def_valid = False
                 self.error_list.append('In Transition: \n' + ' '.join(transition) + ' \n' + transition[2] + ' is not a valid top of stack character\n')
            
            ### CHECK DESTINATION STATE ###
            # Check if the destination state is a valid state
            if(self.States.is_element(transition[3]) == False):
               self.def_valid = False
               self.error_list.append('In Transition: \n' + ' '.join(transition) + ' \n' + transition[3] + ' is not a valid destination state\n')
            else:
               for letter in transition[3]:
                   if (letter == '\\' or letter == '[' or letter == ']'):
                       self.def_valid = False
                       self.error_list.append('In Transition: \n' + ' '.join(transition) + ' \n' + transition[3] + ' cannot contain reserved character\n')
                   elif (self.Input_Alpha.is_element(letter) == True):
                         self.def_valid = False
                         self.error_list.append('In Transition: \n' + ' '.join(transition) + ' \n' + transition[3] + ' cannot contain INPUT_ALPHABET characters\n')
                   elif (self.Stack_Alpha.is_element(letter) == True):
                         self.def_valid = False
                         self.error_list.append('In Transition: \n' + ' '.join(transition) + ' \n' + transition[3] + ' cannot contain STACK_ALPHABET characters\n')            
            
            ### CHECK WRITE TO STACK CHARACTERS ###
            # Check if the write to stack characters are valid
            for letter in transition[4]:
                if(letter == '\\' and len(transition[4]) == 1):
                    # Reserved character allowed in a transition
                    # The pass needs to stay DO NOT DELETE IT
                    pass
                elif(letter == '\\' and len(transition[4]) > 1):
                     self.def_valid = False
                     self.error_list.append('In Transition: \n' + ' '.join(transition) + ' \n' + letter + ' needs to be only character\n')
                elif(letter == '[' or letter == ']'):
                    self.def_valid = False
                    self.error_list.append('In Transition: \n' + ' '.join(transition) + ' \n' + letter + ' cannot contain reserved character\n')
                elif(self.Stack_Alpha.is_element(letter) == False):
                     self.def_valid = False
                     self.error_list.append('In Transition: \n' + ' '.join(transition) + ' \n' + letter + ' is not a valid write to stack character\n')

        ### CHECK INITIAL STATE KEYWORD CONTENT ###
        # Check if there are multiple start states
        if not self.initial_state:
            self.def_valid = False
            self.error_list.append('NO INITIAL STATE FOUND!\n')
        if(len(self.initial_state) != 1):
           self.def_valid = False
           self.error_list.append('In INITIAL_STATES: Only one initial state permitted\n')
        # Check if the start state is a element of the set of states
        elif (self.States.is_element(self.initial_state[0]) == False):
           self.def_valid = False
           self.error_list.append('In INITIAL_STATE: ' + self.initial_state[0] + ' is not in the set of STATES\n')
        # Check that the initial state does not contains INPUT_ALPHABET, STACK_ALPHABET, or reserved character
        else:
            for state in self.initial_state:
                for letter in state:
                    if (letter == '\\' or letter == '[' or letter == ']'):
                        self.def_valid = False
                        self.error_list.append('In INITIAL_STATES: ' + state + ' cannot contain reserved character\n')
                    elif (self.Input_Alpha.is_element(letter) == True):
                        self.def_valid = False
                        self.error_list.append('In INITIAL_STATES: ' + state + ' cannot contain INPUT_ALPHABET characters\n')
                    elif (self.Stack_Alpha.is_element(letter) == True):
                        self.def_valid = False
                        self.error_list.append('In INITIAL_STATES: ' + state + ' cannot contain STACK_ALPHABET characters\n')

        ### CHECK START CHARACTER KEYWORD CONTENT ###
        # Check if there are multiple start characters
        if not self.start_character:
            self.def_valid = False
            self.error_list.append('NO START CHARACTER FOUND!\n')
        if(len(self.start_character) != 1):
            self.def_valid = False
            self.error_list.append('In STATE_CHARACTER: Only one start character permitted\n')
        # Check if the start character is a element of the set of stack characters
        elif (self.Stack_Alpha.is_element(self.start_character[0]) == False):
            self.def_valid = False
            self.error_list.append('In START_CHARACTER: '+ self.start_character[0] + ' is not in stack alphabet\n')
        # Check that the start character does not contain the INPUT_ALPHABET and reserved character
        else:
            for alphabet in self.start_character:
                for letter in alphabet:
                    if (letter == '\\' or letter == '[' or letter == ']'):
                        self.def_valid = False
                        self.error_list.append('In START_CHARACTER: ' + alphabet + ' cannot contain reserved character\n')
                    elif (self.Input_Alpha.is_element(letter) == True):
                        self.def_valid = False
                        self.error_list.append('In START_CHARACTER: ' + alphabet + ' cannot contain INPUT_ALPHABET characters\n')
        
        ### CHECK FINAL STATES KEYWORD CONTENT ###
        # Check if each final state is valid
        if not self.Final_States.final_states:
            self.def_valid = False
            self.error_list.append('NO FINAL STATES FOUND!\n')
        for state in self.Final_States.final_states:
            # Check if each final state is an element of states
            if (self.States.is_element(state) == False):
                self.def_valid = False
                self.error_list.append('In FINAL_STATES: ' + state + ' is not in the set of STATES\n')
            for letter in state:
                # Check for reserved character
                if (letter == '\\' or letter == '[' or letter == ']'):
                    self.def_valid = False
                    self.error_list.append('In FINAL_STATES: ' + state + ' cannot contain reserved character\n')
                # Check for input alphbet character
                elif (self.Input_Alpha.is_element(letter) == True):
                    self.def_valid = False
                    self.error_list.append('In FINAL_STATES: ' + state + ' cannot contain INPUT_ALPHABET characters\n')
                # Check for stack alphabet
                elif (self.Stack_Alpha.is_element(letter) == True):
                    self.def_valid = False
                    self.error_list.append('In FINAL_STATES: ' + state + ' cannot contain STACK_ALPHABET characters\n')
   
    # A method used to get the error list if the defintion file keywords are 
    # not found.
    def is_invalid_def(self):
        if self.states_valid == False:
           self.error_list.append('ERROR: Keyword STATES: not found\n')
        if self.input_alph_valid == False:
           self.error_list.append('ERROR: Keyword INPUT_ALPHABET: not found\n')
        if self.stack_alpha_valid == False:
           self.error_list.append('ERROR: Keyword STACK_ALPHABET: not found\n')
        if self.trans_func_valid == False:
           self.error_list.append('ERROR: Keyword TRANSITION_FUNCTION: not found\n')
        if self.init_state_valid == False:
           self.error_list.append('ERROR: Keyword INITIAL_STATE: not found\n')
        if self.start_char_valid == False:
           self.error_list.append('ERROR: Keyword START_CHARACTER: not found\n')
        if self.final_states_valid == False:
           self.error_list.append('ERROR: Keyword FINAL_STATES: not found\n')
        return self.error_list


# Testing if Validation working on components of definition file.
#valid = Validate_Def_File('invalid2_pda.def')
#
#if valid.def_valid == True:
#    print('Valid')
#else:
#    error_list = []
#    error_list = valid.is_invalid_def()
#    for item in error_list:
#        print(item)



# Testing if Validation working on finding invalid keywords
#valid = Validate_Def_File('invalid_pda.def')
#
#if valid.def_valid == True:
#    print('Valid')
#else:
#    error_list = []
#    error_list = valid.is_invalid_def()
#    for item in error_list:
#        print(item)

