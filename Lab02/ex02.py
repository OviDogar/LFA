class SubstringAutomaton:
    def __init__(self):
        self.q0 = 0  
        self.q1 = 1  
        self.q2 = 2  
        self.q3 = 3  
        
        self.current_state = self.q0
        
        self.transitions = {
            self.q0: lambda c: self.q1 if c == 'c' else self.q0,
            self.q1: lambda c: self.q2 if c == 'a' else (self.q1 if c == 'c' else self.q0),
            self.q2: lambda c: self.q3 if c == 't' else (self.q1 if c == 'c' else self.q0),
            self.q3: lambda c: self.q3  
        }
    
    def process_character(self, char):
        self.current_state = self.transitions[self.current_state](char)
    
    def process_string(self, text):
        for char in text.lower():
            self.process_character(char)
            if self.current_state == self.q3:
                return True
        return False

def gaseste_cat(text):
    automaton = SubstringAutomaton()
    return automaton.process_string(text)

def run_tests():
    test_cases = [
        ("cat", True),
        ("Categorie", True),
        ("Decat sa stiu", True),
        ("altceva", False),
        ("cccattt", True),
        ("act", False),
        ("catalog", True),
        ("mancaat", False),
        ("", False),
        ("cathedral", True),
        (myText, True)
    ]
    
    for text, expected in test_cases:
        result = gaseste_cat(text)
        print(f"Testam '{text}': {'OK' if result == expected else 'GRESIT'} (R: {result}, D: {expected})")

if __name__ == "__main__":
    myText="another CAPS LOCK killed the cat."
    run_tests()