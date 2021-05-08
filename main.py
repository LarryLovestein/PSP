from Proteina import *
from CRUD import *
from  Population import *

'''amino=citireAmino()
pr=Proteina(len(amino[0]),amino[0])
print(pr.structura == detStructura(pr.getMatrice()) )
print(detStructura([[0,0],[0,1],[1,1],[1,2],[2,2],[2,1],[2,0],[1,0]]))'''

'''a=[1,2,3,4,5,6,7,3,4,5,6,7]
b=a[2:3]
a[:3]=b
print(a)'''
from fuzzywuzzy import fuzz


Str1 = "LLLUU"
Str2 = "LULUU"
ratio= fuzz.ratio(Str2,Str1)
print(ratio)
