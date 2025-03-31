import re
from itertools import product

def generate_strings(length, alphabet='01'):
    return [''.join(p) for p in product(alphabet, repeat=length)]

def match_regex(regex, strings):
    pattern = re.compile(f"^{regex}$")
    return [s for s in strings if pattern.match(s)]

def regex_to_python(regex):
    regex = regex.replace("*", "{0,}")
    return regex

def test_equality():
    left_expr = "(1|00{0,}1)|(1|00{0,}1)(0|10{0,}1){0,}(0|10{0,}1)"
    right_expr = "0{0,}1(0|10{0,}1){0,}"
    
    test_strings = []
    for length in range(8):  
        test_strings.extend(generate_strings(length))
    
    left_matches = set(match_regex(left_expr, test_strings))
    right_matches = set(match_regex(right_expr, test_strings))
    
    are_equal = left_matches == right_matches
    
    print(f"Expresiile sunt egale: {are_equal}")
    
    if not are_equal:
        only_in_left = left_matches - right_matches
        only_in_right = right_matches - left_matches
        
        if only_in_left:
            print(f"Siruri doar in expresia din stanga: {sorted(only_in_left)[:5]}...")
        if only_in_right:
            print(f"Siruri doar in expresia din dreapta: {sorted(only_in_right)[:5]}...")
    
    return are_equal

def build_dfa_from_regex(regex_str):
    class DFA:
        def __init__(self, regex):
            self.regex = re.compile(f"^{regex}$")
        
        def accepts(self, string):
            return bool(self.regex.match(string))
    
    return DFA(regex_str)

def verify_with_automata():
    left_dfa = build_dfa_from_regex("(1|00{0,}1)|(1|00{0,}1)(0|10{0,}1){0,}(0|10{0,}1)")
    right_dfa = build_dfa_from_regex("0{0,}1(0|10{0,}1){0,}")
    
    test_strings = []
    for length in range(10):  
        test_strings.extend(generate_strings(length))
    
    for s in test_strings:
        left_accepts = left_dfa.accepts(s)
        right_accepts = right_dfa.accepts(s)
        
        if left_accepts != right_accepts:
            print(f"Sirul '{s}' este acceptat diferit: stanga={left_accepts}, dreapta={right_accepts}")
            return False
    
    print("Automatele sunt echivalente pentru toate sirurile testate.")
    return True

def show_example_strings():
    left_expr = "(1|00{0,}1)|(1|00{0,}1)(0|10{0,}1){0,}(0|10{0,}1)"
    right_expr = "0{0,}1(0|10{0,}1){0,}"
    
    test_strings = []
    for length in range(6):  
        test_strings.extend(generate_strings(length))
    
    left_matches = set(match_regex(left_expr, test_strings))
    right_matches = set(match_regex(right_expr, test_strings))
    
    common_matches = sorted(list(left_matches & right_matches))[:10]
    print("Exemple de siruri acceptate de ambele expresii:")
    for s in common_matches:
        print(f"  '{s}'")

if __name__ == "__main__":
    print("Verificarea egalitatii expresiilor regulate:")
    print("(1+00*1)+(1+00*1)(0+10*1)*(0+10*1) = 0*1(0+10*1)*")
    print("-" * 50)
    
    test_equality()
    print("-" * 50)
    
    verify_with_automata()
    print("-" * 50)
    
    show_example_strings()