from src.globals import *
from src.repgrid import repgrid

class Testreprows:

    def testreprows(self):
        rp=repgrid()
        t=dofile('data/repgrid1.csv')
        rows=rp.repRows(t,transpose(t['cols']))
        for i in rows.cols.all:
            allDict = i.__dict__
            allDict["a"] = allDict.__class__.__name__
            allDict["id"] = id(allDict)
            print(o(i.__dict__))
        for i in rows.rows:
            rowDict = i.__dict__
            rowDict["a"] = rowDict.__class__.__name__
            rowDict["id"] = id(rowDict)
            print(o(i.__dict__))
