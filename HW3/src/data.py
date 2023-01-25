from src.csv import csv
from src.rows import Row
from src.cols import Col

from src.globals import kap

class Data:
    def __init__(self, src):
        self.rows=[]
        self.cols= None
        if type(src)==str:
            cs=csv(src)
            cs.readFromCsv(self.add)
        
    def add(self, t):
        if self.cols:
            t=Row(t)
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols=Col(t)
    
    def stats(self, what, cols, nPlaces):
        def fun(k, col):
            callable = getattr(col, what)
            return col.rnd(callable(), nPlaces), col.txt
        return kap(cols, fun)


# data = Data("../data/auto93.csv")

# print(data.stats("mid",2))
# print(data.stats("div",2))
            