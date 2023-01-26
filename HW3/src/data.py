from src.csv import csv
from src.rows import Row
from src.cols import Col

from src.globals import kap,map

import math

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

    def clone(self):
        data = Data({self.cols.names})
        map({},lambda x : data.add(x))
        return data

    def better(self, row1,row2):
        s1,s2,ys = 0,0,self.cols.y
        for _,col in enumerate(ys):
            x = col.norm(row1.cells[col.at])
            y = col.norm(row2.cells[col.at])
            s1 = s1 - math.exp(col.w * (x-y)/len(ys))
            s2 = s2 - math.exp(col.w * (x-y)/len(ys))
        return s1/len(ys) < s2/len(ys)
    

    # incomplete
    def dist(self, row1, row2, cols):
        n,d = 0,0
        for _,col in enumerate(cols or self.cols.x):
            n+=1
            d+=col.dist(row1.cells[col.at],row2.cells[col.at])^the.p
        return (d/n) ^ (1/the.p)
    

    # incomplete
    def around(self, row1):
        return sort(map(self.rows))


    def half(self, rows):
        pass

    def cluster(self, rows, min, cols, above):
        pass

    def sway(self, rows, min, cols, above):
        pass
# data = Data("../data/auto93.csv")

# print(data.stats("mid",2))
# print(data.stats("div",2))
