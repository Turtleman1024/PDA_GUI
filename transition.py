import os
import re

class transition:
    def __init__(self):
        self.stack = ''
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))

        def_file = open(os.path.join(__location__, 'pda.def'))
        data = def_file.read()
        transitions = re.findall(r'TRANSITION_FUNCTION:(.*?)INITIAL_STATE:',data,re.DOTALL)
        transitions = transitions[0].replace('\n', ' ').replace('\r', '')
        transitions_raw = transitions.split()
        self.transitions_index = []

        for i in range(0, len(transitions_raw), 5):  
            self.transitions_index.append(transitions_raw[i:i + 5])

    def run(self, current_state, string, stack_symbol):
        self.stack = self.stack + stack_symbol
        #stack = stack.append(stack_symbol)
        print(self.stack)
        info_list = []
        for i in range(0, len(self.transitions_index)):
            temp_list = []
            if self.transitions_index[i][0] == current_state and self.transitions_index[i][1] == string and self.transitions_index[i][2] == stack_symbol:
                temp_list.append(self.transitions_index[i][3])
                temp_list.append(self.transitions_index[i][4])
                info_list.append(temp_list)
        return info_list
            
'''Self Test'''
# t = transition()
# a = t.run('s0', 'a', 'Z')
# curr_state = a[0][0]
# curr_sym = a[0][1]

# t.run(curr_state, curr_sym, 'X')
# t.run('s1', 'a', 'X')
# t.run('s0', 'a', 'Z')
# t.run('s1', '\\', 'Z')
#stack = 'X'

