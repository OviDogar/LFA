class MooreMachine:
    def __init__(self):
        self.states = ['S1', 'S2']
        self.inputs = ['A', 'B']
        self.transition_function = {
            ('S1', 'A'): 'S1',
            ('S1', 'B'): 'S2',
            ('S2', 'A'): 'S1',
            ('S2', 'B'): 'S2'
        }
        self.output_function = {
            'S1': 'O1',
            'S2': 'O2'
        }
        self.current_state = 'S1'
    
    def process_input(self, input_symbol):
        if input_symbol not in self.inputs:
            raise ValueError(f"Input invalid: {input_symbol}. Trebuie sa fie unul dintre {self.inputs}")
        
        output = self.output_function[self.current_state]
        
        self.current_state = self.transition_function[(self.current_state, input_symbol)]
        
        return output
    
    def process_sequence(self, input_sequence):
        outputs = []
        for input_symbol in input_sequence:
            output = self.process_input(input_symbol)
            outputs.append(output)
        return outputs
    
    def get_current_state(self):
        return self.current_state
    
    def get_current_output(self):
        return self.output_function[self.current_state]
    
    def reset(self):
        self.current_state = 'S1'

if __name__ == "__main__":
    moore_m = MooreMachine()
    
    input_sequence = ['A', 'B', 'B', 'A', 'B']
    outputs = []
    
    print(f"Stare initiala: {moore_m.get_current_state()}")
    
    for i, symbol in enumerate(input_sequence):
        output = moore_m.process_input(symbol)
        outputs.append(output)
        print(f"Intrare: {symbol}, Iesire: {output}, Stare noua: {moore_m.get_current_state()}")
    
    print("\nIntrare:", input_sequence)
    print("Iesire:", outputs)