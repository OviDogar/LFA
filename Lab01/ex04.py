# exercitiul 4

V = {"S", "A", "B"}
T = {"a", "b"}
P = {
    "S": ["AB"],
    "A": ["aA", "a", ""],
    "B": ["bB", "b", ""]
}

def generate_words(start, maxLen=5):
    if maxLen == 0:
        return {""}
    
    if start in T:
        return {start}
    
    words = set()
    
    for rule in P[start]:
        if rule == "":
            words.add("")
        else:
            first_symbol = rule[0]
            remainder = rule[1:]
            suffixes = generate_words(remainder, maxLen - 1) if remainder else {""}
            prefixes = generate_words(first_symbol, maxLen - 1)
            for prefix in prefixes:
                for suffix in suffixes:
                    words.add(prefix + suffix)
    
    return words


wordList = generate_words("S", 5)
wordList = sorted(list(wordList), key=len)

for word in wordList:
    print(word)
print()
