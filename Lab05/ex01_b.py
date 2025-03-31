class MooreTrafficControl:
    def __init__(self):
        self.states = ['S0', 'S1']
        self.inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
        self.transition_function = {
            ('S0', (0, 0)): 'S0',
            ('S0', (0, 1)): 'S1',
            ('S0', (1, 0)): 'S0',
            ('S0', (1, 1)): 'S1',
            ('S1', (0, 0)): 'S1',
            ('S1', (0, 1)): 'S1',
            ('S1', (1, 0)): 'S0',
            ('S1', (1, 1)): 'S0'
        }
        self.output_function = {
            'S0': 0,
            'S1': 1
        }
        self.current_state = 'S0'
    
    def process_input(self, input_signal):
        if input_signal not in self.inputs:
            raise ValueError(f"Input invalid: {input_signal}")
        
        output = self.output_function[self.current_state]
        
        self.current_state = self.transition_function[(self.current_state, input_signal)]
        
        return output
    
    def get_current_state(self):
        return self.current_state
    
    def get_current_output(self):
        return self.output_function[self.current_state]
    
    def reset(self):
        self.current_state = 'S0'

if __name__ == "__main__":
    moore_traffic = MooreTrafficControl()
    
    input_sequence = [(0, 0), (0, 1), (1, 0), (1, 1), (0, 0)]
    
    print("\nDemonstratie Moore:")
    print(f"Stare initiala: {moore_traffic.get_current_state()}, Iesire initiala: {moore_traffic.get_current_output()}")
    
    for i, signal in enumerate(input_sequence):
        output = moore_traffic.process_input(signal)
        print(f"Intrare: {signal}, Iesire: {output} (Strada {'B' if output == 1 else 'A'} are verde), Stare noua: {moore_traffic.get_current_state()}")