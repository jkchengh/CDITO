def move(L, i, j):
    newL = L.copy()
    p = newL.pop(i)
    if i < j:
        newL.insert(j, p)
    else:
        newL.insert(j+1, p)
    return newL

n = 4
nminus1 = n-1
L = list(range(0, n))
O = [L]
P = [(0, 0, nminus1)]
while P != []:
    print("\n")
    print("L =", L)
    print("P =", P)
    (i, j, l) = P[-1]
    if j != nminus1:
        (iplus, jplus)  = (i, j + 1)
    else:
        (iplus, jplus) = (i + 1, i + 2)
    print("(i+, j+): ", "(" + repr(iplus) + " , " + repr(jplus) + ")")
    if iplus < l:
        P[-1] = (iplus, jplus, l)
        L = move(L, iplus, jplus)
        O.append(L)
        P.append((0, 0, iplus))
        print("Move to", L)
    else:
        P.pop()
        if P != []:
            (ip, jp, lp) = P[-1]
            L = move(L, jp, ip-1)
        print("Backtrack to", L, "by taking", "(" + repr(jp) + " ," + repr(ip-1) + ")")

print("\n")
for o in O:
    print(o)



