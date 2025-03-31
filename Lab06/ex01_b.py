# L={a^i b^j | i <= j}

def is_in_language(s):
    if not all(c in "ab" for c in s):
        return False
    
    count_a = 0
    count_b = 0
    
    i = 0
    while i < len(s) and s[i] == 'a':
        count_a += 1
        i += 1
    
    while i < len(s) and s[i] == 'b':
        count_b += 1
        i += 1
    
    if i < len(s):
        return False  
    
    return count_a <= count_b

def generate_exemple(max_length=10):
    exemple = []
    
    for j in range(1, max_length):
        for i in range(j):
            s = 'a' * i + 'b' * j
            exemple.append(s)
    
    return exemple

test_strings = [
    "a", "aa", "aaa", 
    "ab", "aab", "aaab", "aaaab",
    "aabb", "aaabb", "aaabbb",
    "ba", "baa", "bb", "bbb",
    "abab", "aabba", "ababab"
]

print("Siruri de test:")
for s in test_strings:
    status = "ESTE" if is_in_language(s) else "NU ESTE"
    print(f"'{s}' {status} in limbaj")

print("\nExemple din limbaj:")
for s in generate_exemple(5):
    print(s)