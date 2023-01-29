from src.data import Data
from src.globals import rnd,o

class TestAround:
    def testaround(self):
        data = Data("../data/auto93.csv")
        listVal = data.around(data.rows[0])
        print(0,0,o(data.rows[0].cells))
        for k in range(len(listVal)):
            if((k+1)%50) == 0:
                print(k+1,"\t", rnd(listVal[k][1],2),"\t", o(listVal[k][0].cells))