import math
def distEuclid(A,B):
    return math.sqrt((A[0]-B[0])**2+(A[1]-B[1])**2)


def detC(p1,p2,p3):
    pct=[p1,p2,p3]
    p4=list()
    for i in range(len(pct)):
        for j in range(i+1,len(pct)):
            if distEuclid(pct[i],pct[j]) != 1 :
                p4.append([pct[i][0],pct[j][1]])
                p4.append([pct[j][0], pct[i][1]])

    for i in p4:
        if i not in pct :
            C=i
    return C

#print(detC([0,0],[0,-1],[-1,0]))

def detL(matrice,pct):
    point=matrice[pct].copy()
    next=matrice[pct+1].copy()
    d1 = point.copy()
    d2=d1.copy()
    diagonala=list()
    if next[0] > point[0]:
        d1[0] = d1[0] + 1
        d1[1] = d1[1] + 1
        d2[0] = d2[0] + 1
        d2[1] = d2[1] - 1
        diagonala.append(d1)
        diagonala.append(d2)
    if next[0] < point[0]:
        d1[0] = d1[0] - 1
        d1[1] = d1[1] + 1
        d2[0] = d2[0] - 1
        d2[1] = d2[1] - 1
        diagonala.append(d1)
        diagonala.append(d2)
    if next[1] > point[1]:
        d1[0] = d1[0] - 1
        d1[1] = d1[1] + 1
        d2[0] = d2[0] + 1
        d2[1] = d2[1] + 1
        diagonala.append(d1)
        diagonala.append(d2)
    if next[1] < point[1]:
        d1[0] = d1[0] + 1
        d1[1] = d1[1] - 1
        d2[0] = d2[0] - 1
        d2[1] = d2[1] - 1
        diagonala.append(d1)
        diagonala.append(d2)

    for i in diagonala:
        if i not in matrice:
            return i
    return False
'''a=[[0,0],[0,-1],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
L=detL(a,5)
print(L)
print(a[5],a[6],L)
print(detC(a[5],a[6],L))
'''