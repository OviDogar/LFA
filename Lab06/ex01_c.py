# L={a^n b^n c^n | n > 0}

def is_in_language(s):
    if not all(c in "abc" for c in s):
        return False
    
    count_a = 0
    count_b = 0
    count_c = 0
    
    i = 0
    while i < len(s) and s[i] == 'a':
        count_a += 1
        i += 1
    
    while i < len(s) and s[i] == 'b':
        count_b += 1
        i += 1
    
    while i < len(s) and s[i] == 'c':
        count_c += 1
        i += 1

    if i < len(s):
        return False  
    
    return count_a == count_b == count_c

def generate_exemple(max_length=10):
    exemple = []
    
    for i in range(1, max_length):
            s = 'a' * i + 'b' * i + 'c' * i
            exemple.append(s)
    
    return exemple

test_strings = [
    "abb", "abc", "aaa", 
    "abcc", "aab", "aabbcc", "aaaab",
    "ccaabb", "aaabbc", "aaabbbccc",
    "bac", "baac", "abbc", "bbbcc",
    "ababccc", "aabbac", "abababc"
]

print("Siruri de test:")
for s in test_strings:
    status = "ESTE" if is_in_language(s) else "NU ESTE"
    print(f"'{s}' {status} in limbaj")

print("\nExemple din limbaj:")
for s in generate_exemple(5):
    print(s)