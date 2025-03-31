class Automaton:
    def __init__(self):
        self.states = ['q0', 'q1', 'q2', 'q3', 'q4']
        self.inputs = ['a', 'b']
        self.transition_function = {
            ('q0', 'a'): ['q1', 'q2', 'q3', 'q4'],
            ('q1', 'a'): ['q1', 'q2', 'q3', 'q4'],
            ('q1', 'b'): ['q2', 'q3', 'q4'],
            ('q2', 'a'): ['q3', 'q4'],
            ('q2', 'b'): ['q3', 'q4'],
            ('q3', 'a'): ['q3', 'q4'],
            ('q3', 'b'): ['q1', 'q2', 'q3', 'q4'],
        }
        self.current_state = 'q0'

    def process_input(self, input_symbol):
        if input_symbol not in self.inputs:
            raise ValueError(f"Input invalid: {input_symbol}. Trebuie sa fie unul dintre {self.inputs}")

        # Verificam daca exista o tranzitie pentru starea curenta si simbolul de intrare
        transition_key = (self.current_state, input_symbol)
        if transition_key in self.transition_function:
            # Alegem doar prima stare posibila din lista (automat determinist)
            self.current_state = self.transition_function[transition_key][0]
        else:
            raise ValueError(f"Nu exista tranzitie pentru ({self.current_state}, {input_symbol})")

        return self.current_state  # Consideram ca iesirea este noua stare

    def process_sequence(self, input_sequence):
        outputs = []
        for input_symbol in input_sequence:
            output = self.process_input(input_symbol)
            outputs.append(output)
        return outputs

    def get_current_state(self):
        return self.current_state

    def reset(self):
        self.current_state = 'q0'


if __name__ == "__main__":
    automat = Automaton()

    input_sequence = ['a', 'b', 'a', 'b', 'a', 'b']
    outputs = []

    print(f"Stare initiala: {automat.get_current_state()}")

    for i, symbol in enumerate(input_sequence):
        output = automat.process_input(symbol)
        outputs.append(output)
        print(f"Intrare: {symbol}, Stare noua: {automat.get_current_state()}")
