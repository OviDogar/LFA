class LanguageAutomaton:
    def __init__(self):
        self.alphabet = {'a', 'b', 'c', 'd'}
        
        self.states = {'q0', 'q1', 'q2', 'q3'}
        self.initial_state = 'q0'
        self.final_states = {'q3'}
        
        self.transitions = {
            'q0': {'a': 'q1', 'b': 'q0', 'c': 'q0', 'd': 'q0'},
            'q1': {'a': 'q1', 'b': 'q2', 'c': 'q1', 'd': 'q1'},
            'q2': {'a': 'q2', 'b': 'q2', 'c': 'q2', 'd': 'q3'},
            'q3': {'a': 'q3', 'b': 'q3', 'c': 'q3', 'd': 'q3'}
        }

    def is_valid_word(self, word):
        if len(word) > 6:
            return False
        
        double_count = 0
        i = 0
        while i < len(word) - 1:
            if word[i] == word[i + 1]:
                double_count += 1
                i += 2
            else:
                i += 1
        
        return double_count == 3

    def run_automaton(self, word):
        current_state = self.initial_state
        
        for char in word:
            if char not in self.alphabet:
                return False
            current_state = self.transitions[current_state][char]
            
        return current_state in self.final_states

def main():
    automaton = LanguageAutomaton()
    
    test_words = ['aabbcc', 'ddbbaa', 'bbbaac']

    print("\nTestam cuvintele:")
    for word in test_words:
        is_valid = automaton.is_valid_word(word)
        print(f"Cuvantul '{word}': {' este valid' if is_valid else ' este invalid'} - " + 
              f"{'Are exact' if is_valid else 'Nu contine'} 3 litere duble si " +
              f"lungimea {'<=' if len(word) <= 6 else '>'} 6")
    
if __name__ == "__main__":
    main()