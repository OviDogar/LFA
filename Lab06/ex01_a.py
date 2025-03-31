# L={0^i 1^j | i > j}

def is_in_language(s):
    if not all(c in "01" for c in s):
        return False
    
    count_0 = 0
    count_1 = 0
    
    i = 0
    while i < len(s) and s[i] == '0':
        count_0 += 1
        i += 1
    
    while i < len(s) and s[i] == '1':
        count_1 += 1
        i += 1
    
    if i < len(s):
        return False  
    
    return count_0 > count_1

def generate_exemple(max_length=10):
    exemple = []
    
    for i in range(1, max_length + 1):
        for j in range(i): 
            s = '0' * i + '1' * j
            exemple.append(s)
    
    return exemple

test_strings = [
    "0", "00", "000", 
    "01", "001", "0001", "00001",
    "0011", "00011", "000111",
    "10", "100", "11", "111",
    "0101", "00110", "010101"
]

print("Siruri de test:")
for s in test_strings:
    status = "ESTE" if is_in_language(s) else "NU ESTE"
    print(f"'{s}' {status} in limbaj")

print("\nExemple din limbaj:")
for s in generate_exemple(5):
    print(s)