import numpy as np
import random
import copy
import matplotlib.pyplot as plt
from CRUD import *
def generareRandom(n):
    structura = list()
    matrice = [[0, 0]]
    i = 0
    positii = ["U", "D", "L", "R"]
    j=0
    while len(matrice) < n :
        k = random.randint(0, len(positii) - 1)
        lastPos = matrice[len(matrice) - 1].copy()
        nextPos = lastPos
        u=nextPos.copy()
        d=nextPos.copy()
        l=nextPos.copy()
        r=nextPos.copy()
        u[1]=u[1]+1
        d[1] = d[1] - 1
        l[0] = l[0] - 1
        r[0] = r[0] + 1
        if (positii[k] == "U"):
            nextPos[1] = nextPos[1] + 1
        if (positii[k] == "D"):
            nextPos[1] = nextPos[1] - 1
        if (positii[k] == "L"):
            nextPos[0] = nextPos[0] - 1
        if (positii[k] == "R"):
            nextPos[0] = nextPos[0] + 1
        if nextPos not in matrice:
            structura.append(positii[k])
            matrice.append(nextPos)
            i += 1
        if l in matrice and u in matrice and r in matrice and d in matrice:
            matrice[:]=matrice[:i//2]
            structura[:]=structura[:len(matrice)-1]
            i =i//2
    return structura, matrice

class Proteina():
    def __init__(self,n,amino):
        self.structura,self.matrice=generareRandom(n)
        self.fitness=0
        self.amino=amino
    def __str__(self):
        return f"My configuration: {self.structura} ,my positions: {self.matrice} and my fitness {self.fitness}"

    def plotMatrice(self):
        x=list()
        y=list()
        for i in range(len(self.matrice)):
            x.append (self.matrice[i][0])
            y.append (self.matrice[i][1])
            if (self.amino[i] == "P"):
                plt.plot(x[i], y[i], marker='o', markerfacecolor='blue', markersize=12)
            else:
                plt.plot(x[i], y[i], marker='o', markerfacecolor='red', markersize=12)
        plt.plot(x,y,color='green', linestyle='dashed')
        plt.title('Structura Proteina')
        plt.show()
    def getStructura(self):
        return self.structura
    def getMatrice(self):
        return self.matrice
    def setMatrice(self,matrice):
        self.matrice=matrice.copy()
    def setStructura(self, structura):
        self.structura = structura.copy()

    def getFitness(self):
        return self.fitness

    def Fitness(self):
        istoric=list()
        count=0
        for i in range(len(self.matrice)):
            if self.amino[i]=="H":
                u = self.matrice[i].copy()
                d = self.matrice[i].copy()
                l = self.matrice[i].copy()
                r = self.matrice[i].copy()
                u[1] = u[1] + 1
                d[1] = d[1] - 1
                l[0] = l[0] - 1
                r[0] = r[0] + 1
                if (u in self.matrice and u not in istoric and self.amino[self.matrice.index(u)]=="H"):
                    count-=1
                    istoric.append(self.matrice[i])
                if (d in self.matrice and d not in istoric and self.amino[self.matrice.index(d)]=="H"):
                    count-=1
                    istoric.append(self.matrice[i])
                if (l in self.matrice and l not in istoric and self.amino[self.matrice.index(l)]=="H"):
                    count-=1
                    istoric.append(self.matrice[i])
                if (r in self.matrice and r not in istoric and self.amino[self.matrice.index(r)]=="H"):
                    count-=1
                    istoric.append(self.matrice[i])
        self.fitness=count





'''amino=citireAmino()
for i in range(10):
    pr=Proteina(len(amino[5]),amino[5])
    pr.Fitness()
    if i==3:
        pr.plotMatrice()
    print(" ")
    print(len(pr.matrice))
    print(len(pr.structura))'''
