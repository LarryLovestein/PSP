from Proteina import *
from CRUD import *
from  Population import *

def main():
    dim=int(input("dimensiunea populatiei:"))
    nrIter=int(input("Nr. Iteratii:"))
    T=float(input("T:"))
    minT=float(input("minT:"))
    alpha=float(input("alpha:"))
    nrRulari=int(input("Nr Rulari:"))
    topRulari=list()
    amino = citireAmino()
    i=0
    while i<nrRulari:
        i+=1
