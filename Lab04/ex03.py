class MealyMachine:
    def __init__(self):
        # Definim starile posibile
        self.states = ['Q1', 'Q2']
        # Definim intrarile posibile
        self.inputs = ['X', 'Y']
        # Definim functia de tranzitie ca un dictionar: (stare curenta, intrare) -> stare urmatoare
        self.transition_function = {
            ('Q1', 'X'): 'Q2',
            ('Q1', 'Y'): 'Q1',
            ('Q2', 'X'): 'Q1',
            ('Q2', 'Y'): 'Q2'
        }
        # Definim functia de iesire ca un dictionar: (stare curenta, intrare) -> iesire
        self.output_function = {
            ('Q1', 'X'): 'O1',
            ('Q1', 'Y'): 'O1',
            ('Q2', 'X'): 'O2',
            ('Q2', 'Y'): 'O2'
        }
        # Starea initiala
        self.current_state = 'Q1'
    
    def process_input(self, input_symbol):
        if input_symbol not in self.inputs:
            raise ValueError(f"Input invalid: {input_symbol}. Trebuie sa fie unul dintre {self.inputs}")
        
        # Obtinem iesirea bazata pe starea curenta si intrare
        output = self.output_function[(self.current_state, input_symbol)]
        
        # Determinam starea urmatoare
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
    
    def reset(self):
        self.current_state = 'Q1'

if __name__ == "__main__":
    mealy_machine = MealyMachine()
    
    # Procesam o secventa de intrari
    input_sequence = ['X', 'Y', 'X', 'Y', 'X']
    outputs = []
    
    print("Demonstratie pas cu pas:")
    print(f"Stare initiala: {mealy_machine.get_current_state()}")
    
    for i, symbol in enumerate(input_sequence):
        output = mealy_machine.process_input(symbol)
        outputs.append(output)
        print(f"Intrare: {symbol}, Iesire: {output}, Stare noua: {mealy_machine.get_current_state()}")
    
    print("\nSecventa de intrare:", input_sequence)
    print("Secventa de iesire:", outputs)