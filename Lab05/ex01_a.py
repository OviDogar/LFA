class MealyTrafficControl:
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
            ('S0', (0, 0)): 0,
            ('S0', (0, 1)): 1,
            ('S0', (1, 0)): 0,
            ('S0', (1, 1)): 1,
            ('S1', (0, 0)): 1,
            ('S1', (0, 1)): 1,
            ('S1', (1, 0)): 0,
            ('S1', (1, 1)): 0
        }
        self.current_state = 'S0'
    
    def process_input(self, input_signal):
        if input_signal not in self.inputs:
            raise ValueError(f"Input invalid: {input_signal}")
        
        output = self.output_function[(self.current_state, input_signal)]
        self.current_state = self.transition_function[(self.current_state, input_signal)]
        
        return output
    
    def get_current_state(self):
        return self.current_state
    
    def reset(self):
        self.current_state = 'S0'

if __name__ == "__main__":
    traffic_control = MealyTrafficControl()
    
    input_sequence = [(0, 0), (0, 1), (1, 0), (1, 1), (0, 0)]
    
    print("Demonstratie:")
    print(f"Stare initiala: {traffic_control.get_current_state()}")
    
    for i, signal in enumerate(input_sequence):
        output = traffic_control.process_input(signal)
        print(f"Intrare: {signal}, Iesire: {output} (Strada {'B' if output == 1 else 'A'} are verde), Stare noua: {traffic_control.get_current_state()}")