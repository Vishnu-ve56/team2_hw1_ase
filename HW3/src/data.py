from src.csv import csv
from src.rows import Row
from src.cols import Col

from src.globals import kap,map,mapNew

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

    # def better(self, row1,row2):
    #     s1,s2,ys = 0,0,self.cols.y
    #     for _,col in enumerate(ys):
    #         x = col.norm(row1.cells[col.at])
    #         y = col.norm(row2.cells[col.at])
    #         s1 = s1 - math.exp(col.w * (x-y)/len(ys))
    #         s2 = s2 - math.exp(col.w * (x-y)/len(ys))
    #     return s1/len(ys) < s2/len(ys)
    

    # # incomplete
    # def dist(self, row1, row2, cols):
    #     n,d = 0,0
    #     for _,col in enumerate(cols or self.cols.x):
    #         n+=1
    #         d+=col.dist(row1.cells[col.at],row2.cells[col.at])^the.p
    #     return (d/n) ^ (1/the.p)
    

    # # incomplete
    # def around(self, row1):
    #     return sort(map(self.rows))


    # def half(self, rows, cols, above):
    #     def project(row):
    #         return {row : row, dist : math.cosine(dist(row,A),dist(row,B),c)}
    #     def dist(row1,row2):
    #         return self.dist(row1,row2,cols)
    #     rows = rows or self.rows
    #     some = many(rows, the.Sample)
    #     A = above or any(some)
    #     B = self.around(A,some)[(the.Far * len(rows)//1)].row
    #     c = dist(A,B)
    #     left,right = {},{}
    #     for n,tmp in enumerate(sort(map(rows,project),lt("dist"))):
    #         if n <= len(rows)//2:
    #             push(left, tmp.row)
    #             mid = tmp.row
    #         else:
    #             push(right, tmp.row)
    #     return left, right, A, B, mid, c

        

    # def cluster(self, rows, min, cols, above):
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

    def sway(self, rows, min, cols, above):
        pass

