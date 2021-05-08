
def citireAmino():
    proteine=list()
    f=open("amino.txt","r")
    for i in range(6):
        line=f.readline()
        prot=line.split()
        proteine.append(prot)
    return proteine

'''def plotMatrice(self):
    for i in range(len(self.matrice)):
        x = (self.matrice[i][0])
        y = (self.matrice[i][1])
        if (self.amino[i] == "P"):
            plt.plot(x, y, marker='o', markerfacecolor='blue', markersize=12)
        else:
            plt.plot(x, y, marker='o', markerfacecolor='red', markersize=12)
    plt.title('Structura Proteina')
    plt.show()'''


'''
from Proteina import *

from logic import *
def detStructura(matrice):
    structura=list()
    i=0
    while len(structura)<len(matrice)-1:
        i=len(structura)
        curent=matrice[i].copy()
        next=matrice[i+1].copy()
        if curent[0] < next[0] and (curent[1] == next[1]):
            structura.append("R")
        if curent[0] > next[0] and (curent[1] == next[1]):
            structura.append("L")
        if curent[1] < next[1] and (curent[0] == next[0]):
            structura.append("U")
        if curent[1] > next[1] and (curent[0] == next[0]):
            structura.append("D")

    return structura

def repozitionareZero(matrice):
    x=0-matrice[0][0]
    y=0-matrice[0][1]
    for i in matrice:
        i[0]=i[0]+x
        i[1]=i[1]+y
    return matrice

class Population(Proteina):
    def __init__(self,amino):
        self.pop=list()
        self.amino=amino

    def generarePop(self,n):
        for i in range(n):
            self.pop.append(Proteina(len(self.amino),self.amino))
    def detFitnessPop(self):
        for i in self.pop:
            i.Fitness()
    def __str__(self):
        return f"My population len: {len(self.pop)} and my amino len:{len(self.amino)}"
    def parentsCrossover(self):
        a=random.sample(range(1,len(self.pop)-2), 2)
        p1=copy.copy(self.pop[a[0]])
        p2 = copy.copy(self.pop[a[1]])
        point=random.randint(1,len(p1.getStructura())-1)
        #point=5
        m1=p1.getMatrice()[:point+1]
        p1.setMatrice(m1)
        m1 = p1.getStructura()[:point]
        m2 = p2.getStructura()[point:]
        m1=m1+m2
        p1.setStructura(m1)
        i=point-1
        #print(point)

        positii = ["U", "D", "L", "R"]
        while len(p1.getMatrice())<len(p2.getMatrice()):
            i=len(p1.getMatrice())-1
            curentP=p1.getMatrice()[i].copy()
            if p1.getStructura()[i] == "U":
                curentP[1]=curentP[1] + 1
            if p1.getStructura()[i] == "D":
                curentP[1] = curentP[1] - 1
            if p1.getStructura()[i] == "R":
                curentP[0] = curentP[0] + 1
            if p1.getStructura()[i] == "L":
                curentP[0] = curentP[0] - 1
            if curentP not in p1.getMatrice():
                p1.getMatrice().append(curentP)
            else:
                curentP=p1.getMatrice()[i].copy()
                k = random.randint(0, len(positii) - 1)
                if (positii[k] == "U"):
                    curentP[1]=curentP[1] + 1
                if (positii[k] == "D"):
                    curentP[1] = curentP[1] - 1
                if (positii[k] == "L"):
                    curentP[0] = curentP[0] - 1
                if (positii[k] == "R"):
                    curentP[0] = curentP[0] + 1
                if curentP not in p1.getMatrice():
                    p1.getMatrice().append(curentP)
                u = curentP.copy()
                d = curentP.copy()
                l = curentP.copy()
                r = curentP.copy()
                u[1] = u[1] + 1
                d[1] = d[1] - 1
                l[0] = l[0] - 1
                r[0] = r[0] + 1
                if l in p1.getMatrice() and u in p1.getMatrice() and r in p1.getMatrice() and d in p1.getMatrice():
                    p1.getMatrice()[:] = p1.getMatrice()[:point]
        return p1



    def mutation(self):
        a = random.randint(1, len(self.pop) - 2)
        point = random.randint(2, len(self.amino) - 2)
        p=copy.copy(self.pop[a]) #see selecteaza un individ random din pop
        p.plotMatrice()
        current = p.getMatrice()[point].copy()
        next = p.getMatrice()[point + 1].copy() #urmatorul din lant
        prev = p.getMatrice()[point - 1].copy() #precedentul din lant


        L=detL(p.getMatrice(),point).copy()

        histo=p.getMatrice()[2:point]
        C=detC(current,next,L)
        if C==prev or C not in p.getMatrice():
            p.getMatrice()[point]=L
            p.getMatrice()[point-1]=C
            p.getMatrice()[:point-2]=histo
        print(point)
        #repozitionareZero(p.getMatrice())
        p.setStructura(detStructura(p.getMatrice()))
        print(len(p.getMatrice()))
        p.plotMatrice()

amino=citireAmino()
popor=Population(amino[0])
popor.generarePop(10)
popor.detFitnessPop()
popor.mutation()


    #def crossOver(self):
'''