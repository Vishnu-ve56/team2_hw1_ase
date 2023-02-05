from src.globals import *
from src.repgrid import repgrid

class TestrepCols:

    def testrepcols(self):
        rep=repgrid()
        t=rep.repCols(dofile("data/repgrid1.csv")["cols"])

        for i in t.cols.all:
            allDict = i.__dict__
            allDict["a"] = allDict.__class__.__name__
            allDict["id"] = id(allDict)
            print(o(i.__dict__))

        for i in t.rows:
            rowDict = i.__dict__
            rowDict["a"] = rowDict.__class__.__name__
            rowDict["id"] = id(rowDict)
            print(o(i.__dict__))
