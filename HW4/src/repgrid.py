
from src.data import Data
from src.globals import *
from src.num import NUM
from src.cols import Col

class repgrid:
    def repCols(self, cols):
        cols=copyDefined(cols)
        for i,col in enumerate(cols):
            col[len(col)-1]=col[0]+":"+col[len(col)-1]
            for j in range(1,len(col)):
                col[j-1]=col[j]
            col[len(col)-1]= None 
        s = []
        for i in range(len(cols[0])):
            s.append("Num" + str(i))
        cols.insert(0,s)
        cols[0][len(cols[0])-1]="thingX"
        return Data(cols)


rep=repgrid()
t=rep.repCols(dofile("data/repgrid1.csv")["cols"])

for i in t.cols.all:
    print(i.__dict__)

print(oo(t.rows))