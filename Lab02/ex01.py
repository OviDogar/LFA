af = {
    0: {0: 1, 1: 2},
    1: {0: 3, 1: 0},
    2: {0: 1, 1: 3}
}

s = 0

print("    0  1", end="")
print()

print("--------", end="")
print()

for i in range(0, 3):
    print("q" + str(i), end=" ")
    for j in range(0, 2):
        print("q" + str(af[i][j]), end=" ")
    print()
print("Start: q0; End: q3")