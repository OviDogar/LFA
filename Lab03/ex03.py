class NDA:
    def __init__(self, states, alphabet, transitions, start_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.final_states = final_states
    
    def accept(self, input_string):
        current_states = {self.start_state}
        
        for symbol in input_string:
            new_states = set()
            for state in current_states:
                if (state, symbol) in self.transitions:
                    new_states.update(self.transitions[(state, symbol)])
            current_states = new_states
        
        return any(state in self.final_states for state in current_states)

states = {"q0", "q1", "q2"}
alphabet = {"0", "1", "2"}
transitions = {
    ("q0", "0"): {"q0", "q1", "q2"},
    ("q0", "1"): {"q1", "q2"},
    ("q1", "1"): {"q1","q2"},
    ("q1", "2"): {"q2"},
    ("q2", "2"): {"q2"} 
}
start_state = "q0"
final_states = {"q2"}

nda = NDA(states, alphabet, transitions, start_state, final_states)

print(nda.accept("0"))
print(nda.accept("02"))
print(nda.accept("012"))
print(nda.accept("112"))
print(nda.accept("103"))
