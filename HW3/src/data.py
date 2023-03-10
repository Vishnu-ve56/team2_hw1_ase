from src.csv import csv
from src.rows import Row
from src.cols import Col

from src.globals import *
from src.misc import Misc
import math

class Data:
    def __init__(self, src):
        self.rows=[]
        self.cols= None
        if type(src)==str:
            cs=csv(src)
            cs.readFromCsv(self.add)
        else:
            mapNew(src, self.add)
        
    def add(self, t):
        if self.cols:
            if(type(t) == list):
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

    def clone(self, init):
        data = Data(self.cols.names)
        mapNew(init,data.add)
        return data
    
    
    def dist(self, row1, row2, cols):
        misc = Misc()
        the= misc.getThe()
        n,d = 0,0
        
        for _,col in enumerate(cols or self.cols.x):
            n+=1
            d+=col.dist(row1.cells[col.at],row2.cells[col.at])**the["p"]
        return (d/n) ** (1/the["p"])

    def around(self, row1,rows = None,cols = None):
        def fun(row2):
            return [row2, self.dist(row1, row2, cols)]
        
        val = list(map(fun, rows or self.rows))

        val = sorted(val, key=lambda x: x[1])
        return val

    def half(self, rows = None, cols = None, above = None):
        misc = Misc()
        the = misc.getThe()
        def project(row):
            return [row, cosine(dist(row,A),dist(row,B),c)]
        def dist(row1,row2):
            return self.dist(row1,row2,cols)

        rows = rows or self.rows
        some = many(rows, the["Sample"])
        A = above or any(some)
        listIndice = int((the["Far"] * len(rows))//1)
        

        B = self.around(A,some)[listIndice-1][0]

        c = dist(A,B)

        val = list(map(project, rows))
        val = sorted(val, key=lambda x: x[1])
        left = []
        right = []

        nums = 0
        mid = None
        for values in val:
            nums+=1
            if nums <= len(rows)/2:
                left.append(values[0])
                mid = values[0]
            else:
                right.append(values[0])
        

        return left, right, A, B, mid, c

    def better(self, row1,row2):
        s1,s2,ys = 0,0,self.cols.y
        for _,col in enumerate(ys):
            x = col.norm(row1.cells[col.at])
            y = col.norm(row2.cells[col.at])
            s1 = s1 - math.exp(col.w * (x-y)/len(ys))
            s2 = s2 - math.exp(col.w * (-x+y)/len(ys))
        return s1 < s2
    


    # def cluster(self, rows, min, cols, above):
    #     misc=Misc()
    #     the=misc.getThe()
    #     rows = rows or self.rows
    #     min = min or len(rows)^the.min
    #     cols = cols or self.cols.x
    #     node = {data : self.clone(rows)}
    #     if len(rows) > 2*min:
    #         left, right, node.A, node.B, node.mid = self.half(rows, cols, above)
    #         if self.better(node.B, node.A):
    #             left,right,node.A,node.B = right,left,node.B,node.A
    #         node.left  = self.sway(left,  min, cols, node.A)
    #     return node
    def cluster(self, rows=None, min=None, cols=None, above=None):
        misc=Misc()
        the=misc.getThe()
        rows=rows or self.rows
        min=min or len(rows)**the["min"]
        cols=cols or self.cols.x
        node = {"data": self.clone(rows)}
        if len(rows)> 2*min:
            left, right, node["A"],node["B"], node["mid"],c = self.half(rows,cols,above)
            node["left"]=self.cluster(left,min,cols,node["A"])
            node["right"]=self.cluster(right,min,cols,node["B"])
        if "left" not in node:
            node["left"]=None
        if "right" not in node:
            node["right"]=None   
        return node

    def sway(self, rows = None, min = None, cols = None, above = None):
        rows = rows or self.rows
        misc=Misc()
        the=misc.getThe()
        min = min or len(rows)**the["min"]
        cols = cols or self.cols.x
        node = {"data": self.clone(rows)}
        if len(rows) > 2*min:
            left, right, node["A"],node["B"], node["mid"],c = self.half(rows,cols,above)

            if self.better(node["B"],node["A"]):
                left,right,node['A'],node["B"] = right,left,node['B'],node["A"]
            node["left"] = self.sway(left,min,cols,node["A"])
        
        if "left" not in node:
            node["left"]=None
        if "right" not in node:
            node["right"]=None 
        
        return node





