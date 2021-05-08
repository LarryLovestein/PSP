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
    def parentsCrossover(self,a1,a2):
        #a=random.sample(range(1,len(self.pop)-2), 2)
        p1=copy.copy(self.pop[a1])
        p2 = copy.copy(self.pop[a2])
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


    '''
    a pct random din pop
    '''
    def mutation(self,a):

        point = random.randint(2, len(self.amino) - 2)
        p=copy.copy(self.pop[a]) #see selecteaza un individ random din pop
       # p.plotMatrice()
        current = p.getMatrice()[point].copy()
        next = p.getMatrice()[point + 1].copy() #urmatorul din lant
        prev = p.getMatrice()[point - 1].copy() #precedentul din lant

        if detL(p.getMatrice(),point)==False:
            return p
        else:
            L=detL(p.getMatrice(),point).copy()

        b=p.getMatrice()[2:point+1]
        b1=p.getMatrice()[1:point]
        histo1=b1.copy()
        histo=b.copy()
        C=detC(current,next,L)
       # print(C)
       # print(L)
        if C[0]==prev[0] and C[1]==prev[1]:
            p.getMatrice()[point]=L

        elif C not in p.getMatrice():
            p.getMatrice()[point] = L
            p.getMatrice()[point - 1] = C
            p.getMatrice()[:point - 1] = histo
        #print(point)
        #print(histo)
        #repozitionareZero(p.getMatrice())  # comenteaza asta daca nu merge SA-ul
        p.setStructura(detStructura(p.getMatrice()))
       # print(len(p.getMatrice()))
       # p.plotMatrice()
        return p

    def SaMutation(self,nrIter,T,minT,alpha):
        a=random.randint(0,len(self.pop)-1)
        p = copy.copy(self.pop[a])  # see selecteaza un individ random din pop
        #print(p)
        bestP = copy.copy(p)
        while T > minT:
            j = 0
            while j < nrIter:
                x = self.mutation(a)
                x.Fitness()
                bestP.Fitness()
                delta = x.getFitness() - bestP.getFitness() # daca x mai bun inseamna ca e negativ delta
                if delta < 0:
                    bestP=copy.copy(x)
                elif random.uniform(0,1) < math.exp(delta/T):
                    bestP=copy.copy(x)
                j += 1
            T = alpha * T
        return bestP

    def SaCrossover(self, nrIter, T, minT, alpha,a1,a2):

        p1 = copy.copy(self.pop[a1])  # p1 selectat random
        p2 = copy.copy(self.pop[a2])  # p2 selectat random
        bestP = copy.copy(p1)
        while T > minT:
            j = 0
            while j < nrIter:
                x = self.parentsCrossover(a1,a2)
                x.Fitness()
                bestP.Fitness()
                delta = x.getFitness() - bestP.getFitness()  # daca x mai bun inseamna ca e negativ delta
                if delta < 0:
                    bestP = copy.copy(x)
                elif random.uniform(0, 1) < math.exp(-delta / T):
                    bestP = copy.copy(x)
                j += 1
            T = alpha * T
        return bestP
    def genKids(self,n,nrIter, T, minT, alpha):
        a=random.sample(range(0,len(self.pop)-1), 2) # aici e problema daca imi da ceva greist la gen kids
        kids=list()
        while len(kids) < n:
            k=self.SaCrossover(nrIter,T,minT,alpha,int(a[0]),int(a[1]))
            kids.append(k)
            print(len(kids))
        return kids

    def genMutation(self, n, nrIter, T, minT, alpha):
        mutation = list()
        while len(mutation) < n:
            k = self.SaMutation(nrIter, T, minT, alpha)
            mutation.append(k)
            print(len(mutation))
        return mutation

    


amino=citireAmino()
popor=Population(amino[0])
popor.generarePop(10)
pr=popor.genMutation(10,10,10,0.001,0.999)
print(len(pr))
'''
amino=citireAmino()
popor=Population(amino[0])
popor.generarePop(10)
popor.detFitnessPop()
popor.pop[0].plotMatrice()
pr=popor.SaCrossover(10,10,0.001,0.999,1,2)
pr.plotMatrice()
print(pr)
'''

    #def crossOver(self):
