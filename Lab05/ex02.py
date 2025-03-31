from collections import defaultdict

nfa = defaultdict(list)


nfa['q3'].append(('a', 'qf2'))

nfa['q0'].append(('eps', 'q1'))
nfa['q1'].append(('b', 'q2'))

nfa['q2'].append(('eps', 'q4'))  
nfa['q4'].append(('eps', 'q5'))  
nfa['q4'].append(('eps', 'q7')) 
nfa['q5'].append(('a', 'q6'))
nfa['q7'].append(('b', 'q8'))
nfa['q6'].append(('eps', 'q9'))  
nfa['q8'].append(('eps', 'q9'))

nfa['q9'].append(('eps', 'q10'))
nfa['q10'].append(('eps', 'q11'))
nfa['q11'].append(('eps', 'q12'))  
nfa['q11'].append(('eps', 'q14'))  
nfa['q12'].append(('a', 'q13'))
nfa['q14'].append(('b', 'q15'))
nfa['q13'].append(('eps', 'q16'))
nfa['q15'].append(('eps', 'q16'))
nfa['q16'].append(('eps', 'q11'))  
nfa['q11'].append(('eps', 'q17'))  
nfa['q17'].append(('eps', 'qf1'))  

nfa['q0'].append(('eps', 'q3'))

for state in nfa:
    for symbol, dest in nfa[state]:
        print(f"{state} --{symbol}--> {dest}")
