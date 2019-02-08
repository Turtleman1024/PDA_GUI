from Input_Alphabet import Input_Alphabet
from Parse_File import parse_file
from Final_States import Final_States
from States import States
from Stack_Alphabet import Stack_Alphabet
from transition import transition



class Automaton:
    def __init__(self):
        self.Input_Alpha = Input_Alphabet()
        self.Stack_Alpha = Stack_Alphabet()
        self.States = States()
        self.Final_States = Final_States()
        self.Transition = transition()
        self.operating = False
        #Add Transition_Function here
        file_path = ''
        description = ''
        initial_state = ''
        start_character = ''

    def load(self, path):
        file_path = path
        description = parse_file(path, '', 'STATES:')
        self.States.load(path)
        self.Input_Alpha.load(path)
        self.Stack_Alpha.load(path)
        self.initial_state = parse_file(path, 'INITIAL_STATE:', 'START_CHARACTER:')
        self.start_character = parse_file(path, 'START_CHARACTER:', 'FINAL_STATES:')
        self.current_state = self.initial_state[0]
        self.stack = self.start_character[0]
        self.transitions_list = []
        self.next_symbol = self.stack
        self.Final_States.load(path)

    def run_string(self, string):
        self.operating = True
        self.string = string
        processed_string = ''

        for i in self.string:
            processed_string += i #Keeps track of how much of the string has been processed
            next_transition = self.run_through(i)
            self.transitions_list.append(next_transition)

            if len(next_transition) > 0:
                self.current_state = next_transition[0][0]
                self.stack = next_transition[0][1] + self.stack
                self.next_symbol = self.stack[0:1]

                if processed_string != self.string: #If the entire string has been processed then DON'T consume the top of the stack.
                    self.stack = self.stack[1:]

            else:
                print('Could not process string')

        #return next_transition

    def run_through(self, char):
        next_transition = self.Transition.run(self.current_state, char, self.next_symbol)
        print(next_transition)
        return next_transition
        
#if __name__ == "__main__":
#    aut = Automaton()
#    aut.load('pda.def')
#    aut.run_string('bbaaaaab')