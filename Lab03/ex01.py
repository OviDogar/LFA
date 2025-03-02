class CoffeeAutomaton:
    def __init__(self):
        self.alphabet = {'C', 'T', 'A', 'H', 'OK'}
        
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5'}
        self.initial_state = 'q0'
        self.final_states = {'q5'}
        
        self.transitions = {
            'q0': {'C': 'q1', 'T': 'q2', 'A': 'q3', 'H': 'q4'},
            'q1': {'OK': 'q5', 'C': 'q1', 'T': 'q2', 'A': 'q3', 'H': 'q4'},
            'q2': {'OK': 'q5', 'C': 'q1', 'T': 'q2', 'A': 'q3', 'H': 'q4'},
            'q3': {'OK': 'q5', 'C': 'q1', 'T': 'q2', 'A': 'q3', 'H': 'q4'},
            'q4': {'OK': 'q5', 'C': 'q1', 'T': 'q2', 'A': 'q3', 'H': 'q4'},            
        }

    def run_automaton(self):
        current_state = self.initial_state
       
        while current_state not in self.final_states:
            print(f'Stare curenta: {current_state}')
            print('Optiunea dvs. (C, T, A, H, OK): ')
            input_symbol = input()
            if input_symbol not in self.alphabet:
                print('Input invalid. Reintroduceti.')
                continue
            current_state = self.transitions[current_state].get(
                input_symbol, None)
            if current_state is None:
                print('Input invalid. Reintroduceti.')
                continue

        if current_state in self.final_states:
            print('Bautura este gata! Va mai asteptam! :)')
            return

        return current_state in self.final_states

def main():
    automaton = CoffeeAutomaton()
    automaton.run_automaton()
    
if __name__ == "__main__":
    main()
