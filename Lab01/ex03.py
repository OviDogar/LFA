# exercitiul 3

def invers(s):
    return s[::-1]


E=["", "0", "1", "2"]

lista=[]

for i in range(4):
    for j in range(4):
        for k in range(4):
            if i>j: #  ppee
                continue
            a=str(E[i])+str(E[j])
            b=str(E[k])
            lista.append(a+b+invers(a))

listaFinala=sorted(lista, key=len)

for i in listaFinala:
    print(i)
